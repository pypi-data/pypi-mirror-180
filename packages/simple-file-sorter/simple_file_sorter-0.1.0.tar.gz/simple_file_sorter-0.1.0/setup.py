# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_file_sorter']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['file_sorter = simple_file_sorter:sort']}

setup_kwargs = {
    'name': 'simple-file-sorter',
    'version': '0.1.0',
    'description': 'File sorter',
    'long_description': '# FileSorter - A simple file sorter\n\n## What is it?\n\nSometimes you have a folder with a lot of files and you want \nto sort them into subfolders. This is where FileSorter comes in. \nIt will sort your files into subfolders based on the file extension.\n\n## How do I use it?\n\nChange the path in the script to the folder you want to sort.\n\n```bash\n$ python3 main.py\n```\n',
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
