# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ffpack']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21,<2.0']

setup_kwargs = {
    'name': 'ffpack',
    'version': '0.1.0',
    'description': 'Fatigue and fracture package',
    'long_description': '# Welcome to FFPACK\n\n![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/dpzhuX/ffpack/Python%20package/main)\n![GitHub](https://img.shields.io/github/license/dpzhuX/ffpack)\n\n## Purpose\n`FFPACK` ( Fatigue and Fracture PACKage ) is an open source Python library for fatigue and fracture evaluation. It supports the standard fatigue counting methods in ASTM E1049-85(2017). A lot of features are under active development.\n\n## Installation\n\n`FFPACK` can be installed via [PyPI](https://pypi.org/project/ffpack/):\n\n```\npip install ffpack\n```\n\n## Status\n\n`FFPACK` is currently under active development. \n\n## Contents\n\n* Load cycle counting methods\n    * ASTM level crossing counting\n    * ASTM peak counting\n    * ASTM simple range counting\n    * ASTM rainflow counting\n* Load spectra and matrices\n    * WIP\n\n## Document\n\nYou can find a complete docummentation for setting up `FFPACK` at the [Read the Docs site](https://ffpack.readthedocs.io/en/latest/).\n',
    'author': 'Dongping Zhu',
    'author_email': 'None',
    'maintainer': 'Dongping Zhu',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/ffpack',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
