# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stenocaptioner']

package_data = \
{'': ['*']}

install_requires = \
['ffmpeg-python==0.2.0',
 'more-itertools>=9.0.0,<10.0.0',
 'moviepy>=1.0.3,<2.0.0',
 'numpy>=1.23.5,<2.0.0',
 'torch>=1.13.0,<2.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'transformers>=4.25.1,<5.0.0',
 'whisper @ git+https://github.com/openai/whisper.git',
 'youtube-dl>=2021.12.17,<2022.0.0']

entry_points = \
{'console_scripts': ['stenocaptioner = stenocaptioner.core:cli']}

setup_kwargs = {
    'name': 'stenocaptioner',
    'version': '0.1.0',
    'description': '',
    'long_description': '# stenocaptioner\n\nAutomatic subtitling tool using whisper.\n\n## Installation\n\n### Ubuntu\n\n```sh\nsudo apt-get -y install imagemagick fonts-vlgothic\n```\n\nYou will also need to modify the ImageMagick configuration file to comment out the following policy.\n\n```\nsudo vi /etc/ImageMagick-6/policy.xml\n  <!--\n  <policy domain="path" pattern="@*" rights="none">\n  -->\n```\n\nInstall with pip.\n\n```sh\npip install stenocaptioner\n```\n\n## Usage\n\n```sh\nstenocaptioner https://www.youtube.com/watch?v=Ozvq6Poj8iQ --language ja --text-color red\n```\n',
    'author': 'nekanat',
    'author_email': 'nekanat.stock@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
