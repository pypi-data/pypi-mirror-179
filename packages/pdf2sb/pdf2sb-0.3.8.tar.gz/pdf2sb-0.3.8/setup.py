# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdf2sb']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.4.0,<9.0.0',
 'click>=8.0,<9.0',
 'pdf2image>=1.4,<2.0',
 'pypdf2>=1.26,<2.0',
 'python-gyazo>=1.1,<2.0']

entry_points = \
{'console_scripts': ['pdf2sb = pdf2sb:main']}

setup_kwargs = {
    'name': 'pdf2sb',
    'version': '0.3.8',
    'description': 'Upload PDF file to Gyazo as images then convert Scrapbox format',
    'long_description': '# pdf2sb\n\n![PyPI](https://img.shields.io/pypi/v/pdf2sb.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pdf2sb.svg) ![PyPI - License](https://img.shields.io/pypi/l/pdf2sb.svg)\n\nUpload PDF file to Gyazo as images then convert Scrapbox format.\n\n## Usage\n\nDownload slides (e.g. https://speakerdeck.com/reiyw/effective-modern-python-2018).\nRun:\n\n```sh\npdf2sb ~/Downloads/presentation.pdf | pbcopy\n```\n\nPaste copied text to a Scrapbox page:\n\n[![Image from Gyazo](https://i.gyazo.com/0417c51246c401de8725393d7c78f715.png)](https://gyazo.com/0417c51246c401de8725393d7c78f715)\n\n## Installation\n\n- [poppler](https://poppler.freedesktop.org/) is required to generate images from a PDF file. Install poppler via Homebrew:\n\n```sh\nbrew install poppler\n```\n\n- Install pdf2sb:\n\n```sh\npip install pdf2sb\n```\n\n- Get Gyazo access token from [here](https://gyazo.com/oauth/applications).\n    - Follow the instructions in [this article (in Japanese)](https://blog.naichilab.com/entry/gyazo-access-token).\n- Set `$GYAZO_ACCESS_TOKEN`:\n\n```sh\nexport GYAZO_ACCESS_TOKEN=<access token>\n```\n\n## Running via Docker\n\nYou can run pdf2sb also via Docker:\n\n```sh\nFILE=<your pdf file>; docker run --env GYAZO_ACCESS_TOKEN=$GYAZO_ACCESS_TOKEN -v $(readlink -f $FILE):/app/${FILE##*/} ghcr.io/reiyw/pdf2sb ${FILE##*/}\n# or\ndocker run --env GYAZO_ACCESS_TOKEN=$GYAZO_ACCESS_TOKEN ghcr.io/reiyw/pdf2sb <URL>\n```\n',
    'author': 'reiyw',
    'author_email': 'reiyw.setuve@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/reiyw/pdf2sb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
