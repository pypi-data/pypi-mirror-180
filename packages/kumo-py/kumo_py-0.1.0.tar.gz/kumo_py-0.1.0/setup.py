# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kumo', 'kumo.storage']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'kumo-py',
    'version': '0.1.0',
    'description': 'A small experimental framework for exploring graph-structured data.',
    'long_description': 'Small experimental library for exploring graph-structured data.\n\nTODO: Add a description of the project.\n',
    'author': 'marcinplatek',
    'author_email': 'maruplat@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/marcinplatek/kumo',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
