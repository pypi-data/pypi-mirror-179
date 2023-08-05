# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owl_graph']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'regression-framework']

setup_kwargs = {
    'name': 'owl-graph',
    'version': '0.1.0',
    'description': 'Create Graph Structure for OWL Models and OWL Parse Results',
    'long_description': '',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/owl-graph',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.5,<4.0.0',
}


setup(**setup_kwargs)
