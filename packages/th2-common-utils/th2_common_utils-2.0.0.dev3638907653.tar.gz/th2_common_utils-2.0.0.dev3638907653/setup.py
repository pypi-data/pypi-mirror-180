# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['th2_common_utils', 'th2_common_utils.converters']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.8.1,<4.0.0',
 'sortedcollections>=2.0.0,<3.0.0',
 'th2-grpc-common==4.0.0.dev3574839741']

setup_kwargs = {
    'name': 'th2-common-utils',
    'version': '2.0.0.dev3638907653',
    'description': 'Python library with useful functions for developers and QA needs',
    'long_description': '# th2-common-utils-py (1.6.0)\nPython library with useful functions for **developers and QA needs**. Check the [Wiki](https://github.com/th2-net/th2-common-utils-py/wiki) for instructions and examples.\n\n## Installation\n```\npip install th2-common-utils\n```\n\n## Release notes\n\n### 1.6.0\n\n* Updated `th2-grpc-common` minimal version to `3.12.0`.\n* Optimized `create_event_id()` function.\n* Optimized `create_event_body()` function (migrated to **orjson** library).\n\n### 1.5.0\n\n* Added the ability to create sorted `TreeTable` (ordered by default).\n* Added `dict_values_to_value_filters` and `dict_to_metadata_filter` functions (can be used to create `PreFilter` object from *th2-grpc-check1*).\n\n### 1.4.3\n\n* Fixed memory leak.\n\n### 1.4.2\n\n* Fixed conversion of `Direction` field of `message_metadata`.\n\n### 1.4.1\n\n* Changed `metadata` conversion in `message_to_dict` function.\n\n### 1.4.0\n\n* Added `json_to_message` function.\n\n\n### 1.3.0\n\n* Changed structure of `message_filter` and `metadata_filter` fields in `dict_to_root_message_filter` function.\n',
    'author': 'TH2-devs',
    'author_email': 'th2-devs@exactprosystems.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/th2-net/th2-common-utils-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
