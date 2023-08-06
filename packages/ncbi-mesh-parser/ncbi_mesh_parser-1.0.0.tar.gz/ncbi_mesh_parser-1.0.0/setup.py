# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ncbi_mesh_parser']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'ncbi-mesh-parser',
    'version': '1.0.0',
    'description': 'Parse NCBI MeSH XML files',
    'long_description': None,
    'author': 'Sean Davis',
    'author_email': 'seandavi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
