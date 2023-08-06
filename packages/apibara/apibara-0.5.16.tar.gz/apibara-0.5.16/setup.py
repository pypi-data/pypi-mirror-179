# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['apibara', 'apibara.indexer']

package_data = \
{'': ['*']}

install_requires = \
['aiochannel>=1.1.1,<2.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'backoff>=2.1.2,<3.0.0',
 'click-help-colors>=0.9.1,<0.10.0',
 'click>=8.1.3,<9.0.0',
 'eth-hash[pysha3]>=0.3.2,<0.4.0',
 'grpc-requests>=0.1.3,<0.2.0',
 'grpcio-tools>=1.47.0,<2.0.0',
 'grpcio>=1.47.0,<2.0.0',
 'pymongo[srv]>=4.1.1,<5.0.0',
 'starknet-py==0.6.1a0']

entry_points = \
{'console_scripts': ['apibara = apibara.cli:cli']}

setup_kwargs = {
    'name': 'apibara',
    'version': '0.5.16',
    'description': 'Apibara cliend SDK. Build web3-powered applications.',
    'long_description': 'Apibara Python SDK\n==================\n\n.. warning::\n    This SDK is alpha software. The API will change drastically until the beta.\n\n    `Open an issue on GitHub <https://github.com/apibara/python-sdk>`_ to report bugs or provide feedback.\n\n\nBuild web3-powered applications in Python. \n\n\nLicense\n-------\n\n   Copyright 2022 GNC Labs Limited\n\n   Licensed under the Apache License, Version 2.0 (the "License");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an "AS IS" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n',
    'author': 'Francesco Ceccon',
    'author_email': 'francesco@apibara.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.apibara.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
