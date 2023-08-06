# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pcvis']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['pcvis = pcvis.pcvis:main']}

setup_kwargs = {
    'name': 'pcvis',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pcvis\nSimple scripts for visualizing page cache of a given file\n\n# prerequisites\n* install `pcstat` (Page Cache stat: get page cache stats for files, https://github.com/tobert/pcstat)\n  * it has both Linux and macOS binaries since v0.0.1\n\n# installation\n1. Copy the `pcvis/pcvis.py` from this repo\n2. Move `pcvis.py` into your `$PATH` (e.g. `/usr/local/bin`)\n```\nmv pcvis.py /usr/local/bin/pcvis\nchmod +x /usr/local/bin/pcvis\n```\n\n# usage\nVisualize a given file\'s page cache status like below. In the visualized image, the white dots indicate the part of the file that is in the page cache.\n```\npcstat -json -pps /path/to/my_file | pcvis\n```\n\n<img width="1719" alt="image" src="https://user-images.githubusercontent.com/27754/204122521-c17c5b32-82ee-4326-8d15-b39192889eec.png">\n\n# notes\nBefore running the above command for visualization, you need to clean page cache so that the above result is accurate\n\n```\n# for linux\nsync; echo 1 > /proc/sys/vm/drop_caches \n# for macOS\nsudo purge\n```\n\n\n',
    'author': 'Yue Ni',
    'author_email': 'niyue.com@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
