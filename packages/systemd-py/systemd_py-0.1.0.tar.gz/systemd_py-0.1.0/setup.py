# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['systemd_py',
 'systemd_py.builders',
 'systemd_py.core',
 'systemd_py.core.enums',
 'systemd_py.core.models',
 'systemd_py.core.types',
 'systemd_py.utils']

package_data = \
{'': ['*']}

install_requires = \
['mkdocs-gen-files>=0.4.0,<0.5.0',
 'mkdocs-git-committers-plugin-2>=1.1.1,<2.0.0',
 'mkdocs-git-revision-date-localized-plugin>=1.1.0,<2.0.0',
 'mkdocs-literate-nav>=0.5.0,<0.6.0',
 'mkdocs-material>=8.5.11,<9.0.0',
 'mkdocs-section-index>=0.3.4,<0.4.0',
 'mkdocs>=1.4.2,<2.0.0',
 'mkdocstrings[python]>=0.19.0,<0.20.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'systemd-py',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'amiwrpremium',
    'author_email': 'amiwrpremium@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
