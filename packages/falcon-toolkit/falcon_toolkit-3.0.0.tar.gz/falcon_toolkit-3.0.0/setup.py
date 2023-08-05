# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['falcon_toolkit',
 'falcon_toolkit.common',
 'falcon_toolkit.common.auth_backends',
 'falcon_toolkit.hosts',
 'falcon_toolkit.shell',
 'falcon_toolkit.shell.cmd_generators']

package_data = \
{'': ['*']}

install_requires = \
['caracara>=0.2,<0.3',
 'click-option-group>=0.5.3,<0.6.0',
 'click-spinner>=0.1.10,<0.2.0',
 'click>=8.1.3,<9.0.0',
 'cmd2>=2.4,<3.0',
 'colorama>=0.4.5,<0.5.0',
 'keyring>=23,<24',
 'pick>=2.0.2,<3.0.0']

entry_points = \
{'console_scripts': ['falcon = falcon_toolkit.falcon:cli']}

setup_kwargs = {
    'name': 'falcon-toolkit',
    'version': '3.0.0',
    'description': 'Toolkit to interface with CrowdStrike Falcon via the API',
    'long_description': 'None',
    'author': 'Chris Hammond',
    'author_email': 'chris.hammond@crowdstrike.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
