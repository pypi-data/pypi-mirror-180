# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrouter']

package_data = \
{'': ['*']}

install_requires = \
['requests']

setup_kwargs = {
    'name': 'ky.scrouter',
    'version': '1.0',
    'description': 'A tool that looks for relations between users',
    'long_description': '# Scrouter\n\nA tool that looks for relations between users.\n\n## Installing\n\nVia pip:\n\n```\npip install ky.scrouter\n```\n\nYou can also update to the latest version:\n\n```\npip install ky.scrouter --upgrade\n```\n\n**Make sure you have Python 3.8 or above installed!**\n\n## Program launch\n\nVia terminal:\n\n```\npython -m ky.scrouter\n```\n\n## License\nThis project follows MIT license (see [LICENSE](LICENSE)).\n',
    'author': 'Leon "Procybit" Shepelev',
    'author_email': 'kyleusnaff@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
