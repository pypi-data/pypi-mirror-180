# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tdmat', 'tdmat._data', 'tdmat._data.DHW_sizing', 'tdmat._data.Tabula']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.0.0', 'pandas>=1']

setup_kwargs = {
    'name': 'tdmat',
    'version': '0.1.0',
    'description': 'Thermal Demand Model Adapted from Tabula',
    'long_description': '# tdmat\n\n## What does "tdmat" stand for?\n"tdmat" stands for Thermal Demand Model Adapted from Tabula.\n\n## What is it?\n`tdmat` is a non-GUI tool that implements a simple thermal demand prediction model for european residential buildings.  \n`tdmat` follows an approach similar to the one of the Tabula-Episcope research project [^1].\nIt covers the space heating and space cooling demands and presents additional tools regarding domestic hot water demand. Load profiles follow an hourly time step.\n\n[^1]: https://episcope.eu/building-typology/tabula-webtool/\n\n## How does it work? \nThe typical procedure is as follow:\n1. `tdmat` reads buildings properties from the Tabula-Episcope database [^2]. Data is stored locally, no internet connection needed.\n\n[^2]: https://webtool.building-typology.eu/#bm\n\n2. `tdmat` computes solar, transmission and ventilation contributions based on indoor setpoint temperature and weather data\n3. `tdmat` put contributions together to create hourly profile of thermal demands\n\n##  Installation notes\nThe packaged version of `tamos`is available on PyPi. Please run:\n`pip install tamos`\n\n\n## Where is the project hosted?\nSources are managed on GitHub: https://github.com/BNerot/tdmat\n\n\n## Is it difficult to use?\nPlease follow the example in `examples` as a quick start guide. \nYou can also find a web version of the documentation in `docs/build/html`. Once this directory is downloaded, please open \'index.html\'. \n\n## Copyright\nThe code is distributed under an Apache-2.0 license. \nMost of the development work was done in the context of a PhD thesis. \nThis thesis was funded by two French institutions:\n- Commissariat à l\'Energie Atomique: https://www.cea.fr/english\n- Agence de la transition écologique: https://www.ademe.fr/en/frontpage/\n\n',
    'author': 'BNerot',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
