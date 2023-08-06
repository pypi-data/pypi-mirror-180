# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geolib_plus',
 'geolib_plus.bro_xml_cpt',
 'geolib_plus.cpt_utils',
 'geolib_plus.gef_cpt',
 'geolib_plus.robertson_cpt_interpretation',
 'geolib_plus.shm']

package_data = \
{'': ['*'],
 'geolib_plus.cpt_utils': ['resources/*'],
 'geolib_plus.gef_cpt': ['resources/*'],
 'geolib_plus.robertson_cpt_interpretation': ['resources/*'],
 'geolib_plus.shm': ['resources/*']}

install_requires = \
['d-geolib>=0.2.4,<0.3.0',
 'folium>=0.13.0,<0.14.0',
 'lxml>=4.9.1,<5.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'more-itertools>=9.0.0,<10.0.0',
 'netcdf4>=1.6.2,<2.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyproj>=3.4.0,<4.0.0',
 'pyshp>=2.3.1,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'scipy>=1.9.3,<2.0.0',
 'shapely>=1.8.5.post1,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'd-geolib-plus',
    'version': '0.2.0',
    'description': 'GEOLib+ components',
    'long_description': 'GEOLib+\n=============================\n\nGEOLib+ is a Python package to read, interprent and plot cpt files.\nThe package can also be used to get soil parameters for constitutive models.\n\nInstallation\n------------\n\nInstall GEOLib+ with:\n\n.. code-block:: bash\n\n    $ pip install d-geolib-plus\n\n\nRequirements\n------------\n\nTo install the required dependencies to run GEOLib+ code, run:\n\n.. code-block:: bash\n\n    $ pip install -r requirements\n\nOr, when having poetry installed (you should):\n\n.. code-block:: bash\n\n    $ poetry install\n\n\nTesting & Development\n---------------------\n\nMake sure to have the server dependencies installed: \n\n.. code-block:: bash\n\n    $ poetry install -E server\n\nIn order to run the testcode, from the root of the repository, run:\n\n.. code-block:: bash\n\n    $ pytest\n\nor, in case of using Poetry\n\n.. code-block:: bash\n\n    $ poetry run pytest\n\nRunning flake8, mypy is also recommended. For mypy use:\n\n.. code-block:: bash\n\n    $ mypy --config-file pyproject.toml geolib\n\n\nDocumentation\n-------------\n\nIn order to run the documentation, from the root of the repository, run:\n\n.. code-block:: bash\n\n    $ cd docs\n    $ sphinx-build . build -b html -c .\n\n\nThe documentation is now in the `build` subfolder, where you can open \nthe `index.html` in your browser.\n\nBuild wheel\n-----------\n\nTo build a distributable wheel package, run:\n\n.. code-block:: bash\n\n    $ poetry build\n\nThe distributable packages are now built in the `dist` subfolder.',
    'author': 'Maarten Pronk',
    'author_email': 'git@evetion.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://deltares.github.io/geolib-plus/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
