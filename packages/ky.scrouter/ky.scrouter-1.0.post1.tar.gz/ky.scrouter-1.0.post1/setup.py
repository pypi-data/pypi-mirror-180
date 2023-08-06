# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrouter']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28,<2.29']

setup_kwargs = {
    'name': 'ky.scrouter',
    'version': '1.0.post1',
    'description': 'A tool that looks for relations between users',
    'long_description': "# Scrouter\n\nA tool that looks for relations between users.\n\n## Installing\n\nVia pip:\n\n```\npip install ky.scrouter\n```\n\nYou can also update to the latest version:\n\n```\npip install ky.scrouter --upgrade\n```\n\n**Make sure you have Python 3.8 or above installed!**\n\n## Program launch\n\nVia terminal:\n\n```\npython -m scrouter\n```\n\nAfter that, program will try to find the shortest follower of follower path:\n\n![](https://gyazo.com/c7525a054da578cfb09395093afb1e51.png)\n\n## Library\n\n```python\n>>> import scrouter\n>>> scrouter.route('user1', 'user2')\n...\n```\n\n## License\nThis project follows MIT license (see [LICENSE](LICENSE)).\n",
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
