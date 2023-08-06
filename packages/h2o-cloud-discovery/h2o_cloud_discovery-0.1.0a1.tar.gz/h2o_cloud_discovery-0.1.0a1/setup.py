# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['h2o_discovery']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.16']

setup_kwargs = {
    'name': 'h2o-cloud-discovery',
    'version': '0.1.0a1',
    'description': 'H2O Cloud Discovery Python CLient',
    'long_description': '# `h2o-cloud-discovery`\n\n[![licence](https://img.shields.io/github/license/h2oai/cloud-discovery-py?style=flat-square)](https://github.com/h2oai/cloud-discovery-py/main/LICENSE)\n[![pypi](https://img.shields.io/pypi/v/h2o-cloud-discovery?style=flat-square)](https://pypi.org/project/h2o-cloud-discovery/)\n\nH2O Cloud Discovery Client.\n\n## Installation\n\n```sh\npip install h2o-cloud-discovery\n```\n\n## Usage\n\nPackage provides single async function `h2o_discovery.discover()` that returns\na discovery object that can be used to obtain the information the H2O Cloud\nenvironment, its services and clients.\n\nIt accepts a `environment` argument that can be used to specify the H2O Cloud\nenvironment for which the discovery should be performed. It\'s handy when for\nlocal development.\nAlternatively, the `H2O_CLOUD_ENVIRONMENT` environment variable can be used.\n\n```python\nimport h2o_discovery\n\ndiscovery = await h2o_discovery.discover()\n\n# Print the H2O Cloud environment that was discovered.\nprint(discovery.environment.h2o_cloud_environment)\n\n# Connect to the my service.\nmy_service_client = my_service.client(address=discovery.services["my-service"].uri)\n```\n\n## Examples\n\n### Example: Use with H2O.ai MLOps Python Client within the Wave App\n\n```python\nimport h2o_authn\nimport h2o_discovery\nimport h2o_mlops_client as mlops\nfrom h2o_wave import Q, app, ui\nfrom h2o_wave import main\n\n@app("/")\nasync def serve(q: Q):\n    discovery = await h2o_discovery.discover()\n\n    token_provider = h2o_authn.AsyncTokenProvider(\n        refresh_token=q.auth.refresh_token,\n        issuer_url=discovery.environment.issuer_url,\n        client_id=discovery.clients["platform"].oauth2_client_id,\n    )\n\n    mlops_client = mlops.Client(\n        gateway_url=discovery.services["mlops-api"].uri,\n        token_provider=token_provider,\n    )\n\n    ...\n\n```\n',
    'author': 'H2O.ai',
    'author_email': 'support@h2o.ai',
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
