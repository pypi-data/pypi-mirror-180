# hrin-msb

## Pre-requisites for setup
1. `pip install poetry`

## How To Build

1. `poetry build`
2. `poetry config http-basic.pypi __token__ <access-token>`
3. `poetry publish`


# Change Log
 ### Version 0.1.1

 ### Version 0.1.2

 ### Version 0.1.3

1.  Default serializer added to ApiView
2. fixed incorrect import in _validators.py
3. fixed msb_database_router
4. fixed Config.is_local_env() not working
5. moved devscripts -> devtools
6. File Utils Added to utils/files
7. "app_label" removed from "TestConfig" & "ApiTest" Classes
8. Fixed Bug : 'LoggingModelManager' object has no attribute '_queryset_class'
9. Fixed : Logging Model not showing any records
10. Fixed : str method for base model, & removed current_timestamp method from base model

 ### Version 0.1.4
1. Fixed : ModuleNotFoundError: No module named 'pdf2docx'
2. Renamed “FileGenerator“ => “FileFactory”,
3. Add `create_` Prefix in FileFactory methods
4. Renamed MsbMetaModel -> MsbModelMetaFields
5. Added validation decorators, and fixed bulk validation issuses
6. Modified Logging Configuration Files
7. removed utils package
8. moved msb_core.wrappers.exceptions -> msb_exceptions
9. Fixed : Base ApiViews and Crud Routes
10. Searchparameter class refactored, search method added in ApiService Class

