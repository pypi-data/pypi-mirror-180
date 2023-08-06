# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msb_apis',
 'msb_apis.services',
 'msb_apis.views',
 'msb_apis.wrappers',
 'msb_auth',
 'msb_cipher',
 'msb_config',
 'msb_dataclasses',
 'msb_datetime',
 'msb_db',
 'msb_db.models',
 'msb_devtools',
 'msb_exceptions',
 'msb_ext',
 'msb_files',
 'msb_files.core',
 'msb_logging',
 'msb_testing',
 'msb_validation']

package_data = \
{'': ['*']}

install_requires = \
['cerberus>=1.3.4,<2.0.0',
 'cffi>=1.15.1,<2.0.0',
 'cryptography>=38.0.3,<39.0.0',
 'django>=4.1.3,<5.0.0',
 'djangorestframework-simplejwt==5.1.0',
 'djangorestframework==3.13.1',
 'pandas>=1.5.1,<2.0.0',
 'pdf2docx>=0.5.6,<0.6.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'xhtml2pdf>=0.2.8,<0.3.0']

setup_kwargs = {
    'name': 'hrin-msb',
    'version': '0.1.4',
    'description': '',
    'long_description': '# hrin-msb\n\n## Pre-requisites for setup\n1. `pip install poetry`\n\n## How To Build\n\n1. `poetry build`\n2. `poetry config http-basic.pypi __token__ <access-token>`\n3. `poetry publish`\n\n\n# Change Log\n ### Version 0.1.1\n\n ### Version 0.1.2\n\n ### Version 0.1.3\n\n1.  Default serializer added to ApiView\n2. fixed incorrect import in _validators.py\n3. fixed msb_database_router\n4. fixed Config.is_local_env() not working\n5. moved devscripts -> devtools\n6. File Utils Added to utils/files\n7. "app_label" removed from "TestConfig" & "ApiTest" Classes\n8. Fixed Bug : \'LoggingModelManager\' object has no attribute \'_queryset_class\'\n9. Fixed : Logging Model not showing any records\n10. Fixed : str method for base model, & removed current_timestamp method from base model\n\n ### Version 0.1.4\n1. Fixed : ModuleNotFoundError: No module named \'pdf2docx\'\n2. Renamed “FileGenerator“ => “FileFactory”,\n3. Add `create_` Prefix in FileFactory methods\n4. Renamed MsbMetaModel -> MsbModelMetaFields\n5. Added validation decorators, and fixed bulk validation issuses\n6. Modified Logging Configuration Files\n7. removed utils package\n8. moved msb_core.wrappers.exceptions -> msb_exceptions\n9. Fixed : Base ApiViews and Crud Routes\n10. Searchparameter class refactored, search method added in ApiService Class\n\n',
    'author': 'Prakash Mishra',
    'author_email': 'prakash.mishra@intimetec.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
