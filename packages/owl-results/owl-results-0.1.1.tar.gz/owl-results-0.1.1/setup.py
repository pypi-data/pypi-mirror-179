# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owl_results',
 'owl_results.bp',
 'owl_results.dmo',
 'owl_results.dto',
 'owl_results.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'regression-framework']

setup_kwargs = {
    'name': 'owl-results',
    'version': '0.1.1',
    'description': 'Manipulate Complex OWL Parse Results',
    'long_description': '',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/owl-results',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.5,<4.0.0',
}


setup(**setup_kwargs)
