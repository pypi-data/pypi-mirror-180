# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlpyquil']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16,<2.0',
 'pyquil>=2.9,<3.0',
 'qctrl-open-controls>=9.1.1,<10.0.0',
 'scipy>=1.3,<2.0',
 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'qctrl-pyquil',
    'version': '0.1.0',
    'description': 'Q-CTRL Python PyQuil',
    'long_description': '# ⚠️ (DEPRECATED) This package has been deprecated ⚠️\nVisit https://docs.q-ctrl.com for updated information about how to integrate Q-CTRL software with PyQuil.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<3.9',
}


setup(**setup_kwargs)
