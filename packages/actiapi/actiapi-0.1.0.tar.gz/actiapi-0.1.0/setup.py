# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['actiapi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'actiapi',
    'version': '0.1.0',
    'description': 'A python package for accessing ActiGraph data through the official ActiGraph API',
    'long_description': 'ActiAPI\n==============================\nEncapsulate ActiGraph\'s API in an easy-to-use python package.\n\n# Example\n\n## Metadata\n```python\nfrom actiapi.v3 import ActiGraphClientV3\n\napi_client = ActiGraphClientV3(<api_access_key>, <api_secret_key>)\nmetadata = api_client.get_study_metadata(<study_id>)\nmetadata = {x["id"]: x for x in metadata}\n```\n\n## Raw data\n```python\nfrom actiapi.v3 import ActiGraphClientV3\n\napi_client = ActiGraphClientV3(<api_access_key>, <api_secret_key>)\nresults: List[str] = api_client.get_files(\n            user=<user_id>, study_id=<self.study_id>\n        )\n```',
    'author': 'ActiGraph Data Science Team',
    'author_email': 'science@theactigraph.com',
    'maintainer': 'ActiGraph Data Science Team',
    'maintainer_email': 'science@theactigraph.com',
    'url': 'https://github.com/actigraph/actiapi',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)
