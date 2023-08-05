from __future__ import annotations
import json
import re
import mimetypes
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
from mutagen.mp4 import MP4, MP4Cover


class progress:
    def __init__(self, size) -> None:
        self.size = size
        self.pbar = tqdm(total=size, unit="B", unit_scale=True)

    def update(self, size):
        self.pbar.update(size)

    def close(self):
        self.pbar.close()


class Element:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup

    @property
    def innerHTML(self) -> str:
        return self.soup.decode_contents(formatter="html")

    @property
    def outerHTML(self) -> str:
        return str(self.soup)

    @property
    def children(self) -> list[Element]:
        return [Element(el) for el in self.soup.children]

    @property
    def parentNode(self) -> Element:
        return Element(self.soup.parent)

    @property
    def textContent(self):
        return self.soup.text

    def getElementsByClassName(self, className) -> list[Element]:
        return [Element(el) for el in self.soup.select(f".{className}")]

    def getElementsByTagName(self, tag) -> list[Element]:
        return [Element(el) for el in self.soup.select(tag)]

    def getElementById(self, id) -> Element:
        return Element(self.soup.select(f"#{id}"))

    def querySelectorAll(self, query) -> list[Element]:
        return [Element(el) for el in self.soup.select(query)]

    def querySelector(self, query) -> Element:
        return Element(self.soup.select_one(query))

    def __truediv__(self, query) -> Element:
        return Element(self.soup.select_one(query))

    def __getitem__(self, key) -> str:
        return self.soup[key]

    def __str__(self) -> str:
        return self.innerHTML


class Document(Element):
    def __init__(self, html=None, url=None, headers={}) -> None:
        if not html:
            html = requests.get(url, headers=headers).text
        super().__init__(BeautifulSoup(html, "html.parser"))
        self.body = Element(self.soup.body)
        self.head = Element(self.soup.head)

    @property
    def title(self) -> str:
        return self.soup.title.text


class IwaraUrl:
    ROOT = "https://iwara.tv"
    ROOT_ECCHI = "https://ecchi.iwara.tv"
    USER = "/users/{key}"
    VIDEO = "/videos/{key}"
    PLAYLIST = "/playlist/{key}"
    API = "/api/video/{key}"

    def __init__(self, url: str, type="") -> None:
        self.url = str(url)
        path = url.split("?")[0].split("/")
        if len(path) < 2:
            self.type = type
        else:
            self.type = path[-2]
        self.key = path[-1]
        if "ecchi" in url:
            self.ecchi = True
        else:
            self.ecchi = False
        self.language = None
        if "?" in url:
            params = url.split("?")[-1]
            for param in params.split("&"):
                if "language=" in param:
                    self.language = param.replace("language=", "")
                    break

    @property
    def param(self):
        if self.language:
            return f"?langage={self.language}"
        return ""

    @property
    def api(self) -> str:
        return self.ROOT+self.API.format(key=self.key)

    @property
    def playlist(self) -> str:
        return self.ROOT_ECCHI+self.PLAYLIST.format(key=self.key)+self.param

    @property
    def video(self) -> str:
        return self.ROOT_ECCHI+self.VIDEO.format(key=self.key)+self.param

    @property
    def user(self) -> str:
        return self.ROOT_ECCHI+self.USER.format(key=self.key)+self.param

    def __str__(self) -> str:
        return self.url


class File:
    def __init__(self, data: dict, src: Video) -> None:
        self.__src = src
        self.quality = data["resolution"]
        self.url = "https:"+data["uri"]
        self.mimetype = data["mime"]
        self.ext = mimetypes.guess_extension(self.mimetype).lstrip(".")

    def download(self, path: str, ext=True, meta=True, callback=progress):
        if ext:
            path = str(path)+f".{self.ext}"
        path: Path = Path(str(path)+"")
        path.parent.mkdir(exist_ok=True, parents=True)
        size = int(requests.head(self.url).headers["content-length"])
        pbar = callback(size)
        res = requests.get(self.url, stream=True)
        with path.open(mode="wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                f.write(chunk)
                pbar.update(len(chunk))
        pbar.close()
        if meta and self.ext == "mp4":
            self.__src.damp_meta_data(path)

    def __str__(self) -> str:
        return f"Quality:{self.quality},URL:{self.url}"


class Video:
    __RE_DATE = re.compile(r"\d+-\d{2}-\d{2} \d{2}:\d{2}")

    class __Iterator:
        def __init__(self, files):
            self.__files = files
            self.__count = -1
            self.__max = len(files)

        def __iter__(self):
            return self

        def __next__(self) -> File:
            self.__count += 1
            if self.__count == self.__max:
                raise StopIteration
            return self.__files[self.__count]

    def __init__(self, url) -> None:
        self.url: str = url
        self.__url = IwaraUrl(url, type="videos")
        self.id: str = self.__url.key
        self.__title: str = None
        self.__date: datetime = None
        self.__files: list[File] = None
        self.__user: str = None
        self.__user_url: str = None
        self.__thumbnail_url: str = None
        self.__likes: int = None
        self.__views: int = None
        self.__private: bool = None
        self.__comment: str = None

    def __collect_video_info(self) -> None:
        document = Document(url=self.__url.video)
        self.__title = document.title.rstrip(" | Iwara")
        self.__private = False
        if (document.body/"h1").textContent == "Private video":
            self.__private = True
            return None
        user_data = document/"a.username"
        self.__user = user_data.textContent
        self.__user_url = IwaraUrl(user_data["href"]).user
        self.__date = datetime.strptime(self.__RE_DATE.search(
            (document/".node-info").textContent).group(), "%Y-%m-%d %H:%M")
        nums: list[str] = re.findall(
            r"[\d,]+", (document/".node-views").innerHTML)
        self.__likes = int(nums[0].replace(",", ""))
        self.__views = int(nums[1].replace(",", ""))
        self.__comment = (document/".node-info" /
                          "div.field-type-text-with-summary").textContent
        self.__thumbnail_url = "https:"+(document/"#video-player")["poster"]

    def __collect_download_info(self):
        self.__files = []
        datas = json.loads(requests.get(self.__url.api).text)
        for data in datas:
            self.__files.append(File(data, self))

    def __private_err(self) -> None:
        if self.__private:
            raise Exception("Private video information cannot be obtained")

    @property
    def title(self):
        if self.__title == None:
            self.__collect_video_info()
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def private(self):
        if self.__private == None:
            self.__collect_video_info()
        return self.__private

    @private.setter
    def private(self, private):
        self.__private = private

    @property
    def user(self):
        self.__private_err()
        if self.__user == None:
            self.__collect_video_info()
            self.__private_err()
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def user_url(self):
        self.__private_err()
        if self.__user_url == None:
            self.__collect_video_info()
            self.__private_err()
        return self.__user_url

    @user_url.setter
    def user_url(self, user_url):
        self.__user_url = user_url

    @property
    def likes(self):
        self.__private_err()
        if self.__likes == None:
            self.__collect_video_info()
            self.__private_err()
        return self.__likes

    @likes.setter
    def likes(self, likes):
        self.__likes = likes

    @property
    def views(self):
        self.__private_err()
        if self.__views == None:
            self.__collect_video_info()
            self.__private_err()
        return self.__views

    @views.setter
    def views(self, views):
        self.__views = views

    @property
    def thumbnail_url(self):
        self.__private_err()
        if self.__thumbnail_url == None:
            self.__collect_video_info()
            self.__private_err()
        return self.__thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        self.__thumbnail_url = thumbnail_url

    @property
    def date(self):
        self.__private_err()
        if self.__date == None:
            self.__collect_video_info()
        self.__private_err()
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def comment(self):
        self.__private_err()
        if self.__comment == None:
            self.__collect_video_info()
            self.__private_err()
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment

    @property
    def files(self) -> list[File]:
        if self.__private:
            return []
        else:
            if self.__files == None:
                self.__collect_download_info()
            return self.__files

    @property
    def thumbnail(self) -> bytes:
        return requests.get(self.thumbnail_url).content

    def __meta_thumbnail(self) -> MP4Cover:
        ext = MP4Cover.FORMAT_JPEG
        if self.thumbnail_url.split(".")[-1] == "png":
            ext = MP4Cover.FORMAT_PNG
        return MP4Cover(self.thumbnail, imageformat=ext)

    def damp_meta_data(self, path):
        video = MP4(path)
        video["\xa9nam"] = self.title
        video["\xa9ART"] = self.user
        video["purl"] = self.__url.video
        video["covr"] = [self.__meta_thumbnail()]
        video["\xa9day"] = str(self.date.year)
        video["\xa9cmt"] = self.comment
        video.save()

    def __getitem__(self, quality) -> File:
        if type(quality) == int:
            if quality > 10:
                quality = f"{quality}p"
            else:
                return self.files[quality]
        for file in self.files:
            if file.quality == quality:
                return file
        raise KeyError(quality)

    def __iter__(self) -> __Iterator:
        return self.__Iterator(self.files)

    def __len__(self) -> int:
        return len(self.files)


class Videos:
    class __Iterator:
        def __init__(self, videos):
            self.__videos = videos
            self.__count = -1
            self.__max = len(videos)

        def __iter__(self):
            return self

        def __next__(self) -> Video:
            self.__count += 1
            if self.__count == self.__max:
                raise StopIteration
            return self.__videos[self.__count]

    def __init__(self, videos: list[Video] = []) -> None:
        self.videos = videos

    @property
    def urls(self) -> list[str]:
        return [v.url for v in self.videos]

    def __len__(self) -> int:
        return len(self.videos)

    def __str__(self) -> str:
        return f"Videos:{len(self)}item"

    def __getitem__(self, n) -> Video:
        return self.videos[n]

    def __iter__(self) -> __Iterator:
        return self.__Iterator(self.videos)

    def __conteins__(self, url: str) -> bool:
        iurl = IwaraUrl(url)
        for v in self.videos:
            if v.id == iurl.key:
                return True
        return False


class User(Videos):
    __RE_DATE = re.compile(r"\d+-\d{2}-\d{2}")

    def __init__(self, url: str) -> None:
        self.__url = IwaraUrl(url, "users")
        self.__name: str = None
        self.__join: datetime = None
        self.__comment: str = None
        self.__thumbnail_url: str = None
        self.__videos_url: str = None
        self.url = url
        self.__videos: list[Video] = None

    def __collect_info(self) -> None:
        document = Document(url=self.__url.user)
        self.__name = document.title.rstrip(" | Iwara")
        info = document/".view-content"
        self.__join = datetime.strptime(
            self.__RE_DATE.search(info.textContent).group(), "%Y-%m-%d")
        self.__thumbnail_url = "https:"+(info/"img")["src"]
        try:
            self.__comment = (
                document/"div.views-field-field-about").textContent
        except:
            self.__comment = ""
        video_info = document/".view-videos"
        more_link = video_info.getElementsByClassName("more-link")
        if more_link:
            self.__videos_url = IwaraUrl.ROOT_ECCHI+(more_link[0]/"a")["href"]
        else:
            self.__videos = []
            for video in video_info.getElementsByClassName("node-video"):
                title = (video/"h3"/"a").textContent
                url = (video/"h3"/"a")["href"]
                v = Video(url)
                v.title = title
                v.user = self.name
                v.user_url = self.__url.user
                self.__videos.append(v)

    def __collect_videos(self) -> list[Videos]:
        if self.__videos_url == None:
            self.__collect_info()
        if self.__videos_url:
            self.__videos = []
            page_url = self.__videos_url
            while page_url:
                document = Document(url=page_url)
                videos, after = self.__collect_videos_from_page(document)
                self.__videos.extend(videos)
                page_url = after

    def __collect_videos_from_page(self, document: Document) -> tuple(list[Videos], str):
        after = document.querySelectorAll("li.pager-next")
        if after:
            after = IwaraUrl.ROOT_ECCHI+(after[0]/"a")["href"]
        else:
            after = None
        videos = []
        for video in document.getElementsByClassName("node-video"):
            title = (video/"h3"/"a").textContent
            url = (video/"h3"/"a")["href"]
            v = Video(url)
            v.title = title
            v.user = self.name
            v.user_url = self.__url.user
            videos.append(v)
        return (videos, after)

    @property
    def videos(self):
        if self.__videos == None:
            self.__collect_videos()
        return self.__videos

    @videos.setter
    def videos(self, videos):
        self.__videos = videos

    @property
    def comment(self):
        if self.__comment == None:
            self.__collect_info()
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment

    @property
    def name(self):
        if self.__name == None:
            self.__collect_info()
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def join(self):
        if self.__join == None:
            self.__collect_info()
        return self.__join

    @join.setter
    def join(self, join):
        self.__join = join

    @property
    def thumbnail_url(self):
        if self.__thumbnail_url == None:
            self.__collect_info()
        return self.__thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        self.__thumbnail_url = thumbnail_url

    @property
    def thumbnail(self) -> bytes:
        return requests.get(self.thumbnail_url).content

    def __str__(self) -> str:
        return f"User:{self.url}"


class Playlist(Videos):
    __RE_DATE = re.compile(r"\d+-\d{2}-\d{2} \d{2}:\d{2}")

    def __init__(self, url: str) -> None:
        self.url: str = url
        self.__url: IwaraUrl = IwaraUrl(url, "playlist")
        self.__title: str = None
        self.__user: str = None
        self.__user_url: str = None
        self.__videos: list[Video] = None

    def __collect_info(self):
        document = Document(url=self.__url.playlist)
        self.__title = document.title.rstrip(" | Iwara")
        user_data = document/".view-profile"
        self.__user = (user_data/"h2").textContent
        self.__user_url = IwaraUrl(self.__user).user
        self.__videos = []
        for video in (document/"#content").getElementsByClassName("node-video"):
            link = video/"h3"/"a"
            v = Video(link["href"])
            v.title = link.textContent
            submitted = video/".submitted"
            submit_user = submitted/"a"
            v.user = submit_user.textContent
            v.user_url = IwaraUrl(submit_user["href"]).user
            v.date = datetime.strptime(self.__RE_DATE.search(
                submitted.textContent).group(), "%Y-%m-%d %H:%M")
            v.comment = (video/".field-type-text-with-summary").textContent
            nums: list[str] = re.findall(
                r"[\d,]+", (video/".video-info").innerHTML)
            v.likes = int(nums[0].replace(",", ""))
            v.views = int(nums[1].replace(",", ""))
            self.__videos.append(v)

    @property
    def title(self):
        if self.__title == None:
            self.__collect_info()
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def user(self):
        if self.__user == None:
            self.__collect_info()
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def user_url(self):
        if self.__user_url == None:
            self.__collect_info()
        return self.__user_url

    @user_url.setter
    def user_url(self, user_url):
        self.__user_url = user_url

    @property
    def videos(self):
        if self.__videos == None:
            self.__collect_info()
        return self.__videos

    @videos.setter
    def videos(self, videos):
        self.__videos = videos

    def __str__(self) -> str:
        return f"Playlist:{self.url}"


def Auto(url):
    iurl = IwaraUrl(url)
    match iurl.type:
        case "users":
            return User(url)
        case "videos":
            return Video(url)
        case "playlist":
            return Playlist(url)
    return None


if __name__ == "__main__":
    pass
