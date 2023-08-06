# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ecoindex']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'ecoindex',
    'version': '5.4.1',
    'description': 'Ecoindex module provides a simple way to measure the Ecoindex score based on the 3 parameters: The DOM elements of the page, the size of the page and the number of external requests of the page',
    'long_description': "# ECOINDEX PYTHON\n\n![Quality check](https://github.com/cnumr/ecoindex_python/workflows/Quality%20checks/badge.svg)\n[![PyPI version](https://badge.fury.io/py/ecoindex.svg)](https://badge.fury.io/py/ecoindex)\n\nThis basic module provides a simple interface to get the [Ecoindex](http://www.ecoindex.fr) based on 3 parameters:\n\n- The number of DOM elements in the page\n- The size of the page\n- The number of external requests of the page\n\n## Requirements\n\n- Python ^3.10 with [pip](https://pip.pypa.io/en/stable/installation/)\n\n## Install\n\n```shell\npip install ecoindex\n```\n\n## Use\n\n### Get ecoindex\n\nYou can easily get the ecoindex by calling the function `get_ecoindex()`:\n\n```python\n(function) get_ecoindex: (dom: int, size: float, requests: int) -> Coroutine[Any, Any, Ecoindex]\n```\n\nExample:\n\n```python\nimport asyncio\nfrom pprint import pprint\n\nfrom ecoindex import get_ecoindex\n\n# Get ecoindex from DOM elements, size of page and requests of the page\necoindex = asyncio.run(get_ecoindex(dom=100, size=100, requests=100))\npprint(ecoindex)\n```\n\nResult example:\n\n```python\nEcoindex(grade='B', score=72.0, ges=1.56, water=2.34, ecoindex_version='3.0.0')\n```\n\n## Contribute\n\nYou need [poetry](https://python-poetry.org/) to install and manage dependencies. Once poetry installed, run :\n\n```bash\npoetry install\n```\n\n## Tests\n\n```shell\npoetry run pytest\n```\n\n## Disclaimer\n\nThe LCA values used by [ecoindex](https://github.com/cnumr/ecoindex_python) to evaluate environmental impacts are not under free license - ©Frédéric Bordage\nPlease also refer to the mentions provided in the code files for specifics on the IP regime.\n\n## [License](LICENSE)\n\n## [Contributing](CONTRIBUTING.md)\n\n## [Code of conduct](CODE_OF_CONDUCT.md)\n",
    'author': 'Vincent Vatelot',
    'author_email': 'vincent.vatelot@ik.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://www.ecoindex.fr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
