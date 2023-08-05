# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tile_operator']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'geopandas>=0.12.1,<0.13.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pillow>=9.3.0,<10.0.0',
 'rasterio>=1.3.4,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'tile-operator',
    'version': '0.0.1',
    'description': 'Tile Operation tool',
    'long_description': '# tile-operator\n\n## usage\n\n```bash\n$ python to.py --help        \nUsage: to.py [OPTIONS] COMMAND [ARGS]...\n\n  Tile operator v0.0.1\n\nOptions:\n  --version                 Show the version and exit.\n  -v, --verbose             verbose mode\n  --help                    Show this message and exit.\n\nCommands:\n  operate  Tile Operation\n```\n\n## test\n\n```bash\n$ pytest -qs tests\n```',
    'author': 'nokonoko1203',
    'author_email': 'nokonoko.1203.777@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
