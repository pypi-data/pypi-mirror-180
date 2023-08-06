# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jumpstart_projects', 'jumpstart_projects.src']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['jumpstart = jumpstart_projects.__main__:cli']}

setup_kwargs = {
    'name': 'jumpstart-projects',
    'version': '1.1.0',
    'description': 'Project jumpstart utilities',
    'author': 'Aradhya',
    'author_email': 'aradhyatripathi51@gmail.com',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
