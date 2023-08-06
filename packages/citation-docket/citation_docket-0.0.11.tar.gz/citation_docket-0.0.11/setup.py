# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citation_docket', 'citation_docket.base', 'citation_docket.regexes']

package_data = \
{'': ['*']}

install_requires = \
['citation-date>=0.0.3,<0.0.4',
 'pydantic>=1.10.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'citation-docket',
    'version': '0.0.11',
    'description': 'Docket citation regexes from Philippine Supreme Court decisions',
    'long_description': 'None',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
