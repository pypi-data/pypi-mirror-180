# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mundipy', 'mundipy.api', 'mundipy.cache', 'mundipy.pcs']

package_data = \
{'': ['*']}

install_requires = \
['Fiona>=1.8.21,<2.0.0',
 'SQLAlchemy>=1.4.40,<2.0.0',
 'fiona>=1.8.21,<2.0.0',
 'numpy>=1.23.3,<2.0.0',
 'psycopg-binary>=3.0.16,<4.0.0',
 'psycopg-pool>=3.1.1,<4.0.0',
 'psycopg>=3.0.16,<4.0.0',
 'pyproj>=3.4.0,<4.0.0',
 'shapely==2.0b2',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'mundipy',
    'version': '0.8.0',
    'description': 'mundipy is a Python framework for spatial data analysis',
    'long_description': "# [![mundi.py](docs/logo/light.svg)](https://docs.mundi.ai)\n\n[![PyPI version](https://badge.fury.io/py/mundipy.svg)](https://pypi.org/project/mundipy/) ![GitHub issues](https://img.shields.io/github/issues/BuntingLabs/mundipy) ![PyPI - License](https://img.shields.io/pypi/l/mundipy)\n\nmundipy is a Python framework for spatial data manipulation. Built on top of\n[geopandas](https://geopandas.org/en/stable/), [GDAL](https://gdal.org/),\nand [shapely](https://shapely.readthedocs.io/en/stable/manual.html), mundi.py\nprovides a useful abstraction to eliminate the hassles of spatial data.\n\n# Features\n\n- [Spatial caching](https://docs.mundi.ai/spatial-lru-cache)\n- [Automatically projection management](https://docs.mundi.ai/projected-coordinate-systems)\n- [Layer management](https://docs.mundi.ai/layer-management)\n- Automatic spatial indexing for lookups\n- Automatic spatial joins\n\n# Project Roadmap\n\n- Jupyter notebook native (\\_repr\\_html\\_) that doesn't explode with massive data\n- Nearest neighbor/distance queries\n- Dissolving into h3/s2\n\n## License\n\nMundi.py is MIT licensed.\n",
    'author': 'Brendan Ashworth',
    'author_email': 'brendan@buntinglabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://buntinglabs.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
