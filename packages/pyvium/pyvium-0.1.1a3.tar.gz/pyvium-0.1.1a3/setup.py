# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyvium']

package_data = \
{'': ['*']}

install_requires = \
['cffi>=1.15.1,<2.0.0']

setup_kwargs = {
    'name': 'pyvium',
    'version': '0.1.1a3',
    'description': 'A tiny Python wrapper around the <Software development driver DLL> for IviumSoft.',
    'long_description': '# PYVIUM\n\nTiny Python wrapper around the "Software development driver DLL" for IviumSoft.\n\n# Important:\nThis module uses a dll from the IviumSoft application. You need to have this software installed on a Windows machine. The IviumSoft application can be downloaded from here: https://www.ivium.com/support/#Software%20update\n\n## Installation\n\nInstall PYVIUM CORE easily with pip:\n\n```\npip install pyvium\n```\n\nOr with poetry:\n\n```\npoetry add pyvium\n```\n\n## Usage Example (Using IviumSoft Core functions)\n\nTo use the same functions available in the "IviumSoft driver DLL" you can import the Core class as follows. All functions return a result code (integer) and a result value if available. For further information you can check the IviumSoft documentation.\n\n```\nfrom pyvium import Core\n\napp = Core()\n\napp.IV_open()\napp.IV_getdevicestatus()\napp.IV_close()\n```\n\n<!-- ## Usage Example (Using Pyvium methods)\n\nThis is a wrapper around the Core functions that adds a few things:\n- Exception management\n- New functionalities\n\n```\nfrom pyvium import Pyvium\n\napp = Pyvium()\n\napp.connect_device()\n``` -->\n\n\n## Not working functions\n- IV_getcurrentWE2trace\n- IV_getpotentialtrace\n\n## Links\n\n* [See on GitHub](https://github.com/sftec/pyvium)\n* [See on PyPI](https://pypi.org/project/pyvium)',
    'author': 'Alejandro Gutiérrez',
    'author_email': 'agutierrez@stec.es',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SF-Tec/pyvium',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
