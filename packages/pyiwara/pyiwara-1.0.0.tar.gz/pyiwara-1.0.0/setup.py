import pyiwara
from setuptools import setup
from pathlib import Path

DESCRIPTION = "iwaraの情報を取得、ダウンロードができます。"
NAME = 'pyiwara'
AUTHOR = 'kazutora'
AUTHOR_EMAIL = 'kazutora1006@gmail.com'
URL = 'https://github.com/kazutora1006/pyiwara'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/kazutora1006/pyiwara'
VERSION = pyiwara.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'mutagen>=1.2.0',
    'beautifulsoup4>=4.0.0',
]

PACKAGES = [
    'pyiwara'
]

long_description = """pyiwara
##########
`詳細 <https://github.com/kazutora1006/pyiwara>`_
"""

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      )
