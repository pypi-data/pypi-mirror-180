# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_file_sorter']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['simple_file_sorter = simple_file_sorter:sort']}

setup_kwargs = {
    'name': 'simple-file-sorter',
    'version': '0.1.1',
    'description': 'Simple File Sorter',
    'long_description': '# FileSorter - A simple file sorter\n\n## What is it?\n\nSometimes you have a folder with a lot of files, and you want \nto sort them into folders. This is where FileSorter comes in. \nIt will sort your files into folders based on the file extension.\n\n## How to install\n\n```bash\n$ pip install simple_file_sorter\n```\n\n## How to use\n```bash\nusage: simple_file_sorter [-h] [-s SRC] [-d DST]\n\nFile sorter\n\noptions:\n  -h, --help         show this help message and exit\n  -s SRC, --src SRC  Source dir\n  -d DST, --dst DST  Destination dir\n```\n\n## Example\n\n```bash\n$ simple_file_sorter -s ~/Downloads\n```',
    'author': 'Vitalii Shishorin',
    'author_email': 'moskrc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
