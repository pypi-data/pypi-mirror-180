# testops_api.TestReportApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download2**](TestReportApi.md#download2) | **GET** /api/v1/katalon/download | 
[**process_multiple_s3_file**](TestReportApi.md#process_multiple_s3_file) | **POST** /api/v1/katalon/test-reports/multiple | Saves and processes multiple uploaded Katalon reports.
[**process_multiple_s3_file_v2**](TestReportApi.md#process_multiple_s3_file_v2) | **POST** /api/v1/katalon/test-reports/multiple-v2 | Saves and processes multiple uploaded Katalon reports.
[**process_s3_file**](TestReportApi.md#process_s3_file) | **POST** /api/v1/katalon/test-reports | Saves and processes the uploaded Katalon reports.
[**process_test_ops_reports**](TestReportApi.md#process_test_ops_reports) | **POST** /api/v1/testops-reports | Saves and processes multiple uploaded TestOps reports.
[**update_result**](TestReportApi.md#update_result) | **POST** /api/v1/katalon/test-reports/update-result | 
[**upload**](TestReportApi.md#upload) | **POST** /api/v1/katalon-recorder/test-reports | Uploads and processes a Katalon Recorder report.
[**upload_j_unit_reports**](TestReportApi.md#upload_j_unit_reports) | **POST** /api/v1/junit/test-reports | Uploads and processes the JUnit reports to an Execution.
[**upload_j_unit_reports_v2**](TestReportApi.md#upload_j_unit_reports_v2) | **POST** /api/v1/junit/test-reports-v2 | Uploads and processes the JUnit reports to an Execution with tag and custom field.
[**upload_test_ng_reports**](TestReportApi.md#upload_test_ng_reports) | **POST** /api/v1/testng/test-reports | Uploads and processes the TestNG reports to an execution.


# **download2**
> download2()



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    platform = "win_64" # str |  (optional) if omitted the server will use the default value of "win_64"
    type = "kse_pe" # str |  (optional) if omitted the server will use the default value of "kse_pe"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.download2(platform=platform, type=type)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->download2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | [optional] if omitted the server will use the default value of "win_64"
 **type** | **str**|  | [optional] if omitted the server will use the default value of "kse_pe"

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_multiple_s3_file**
> [UploadBatchResource] process_multiple_s3_file(project_id, batch, upload_batch_file_resource)

Saves and processes multiple uploaded Katalon reports.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from testops_api.model.upload_batch_file_resource import UploadBatchFileResource
from testops_api.model.upload_batch_resource import UploadBatchResource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = 1 # int | 
    batch = "batch_example" # str | 
    upload_batch_file_resource = [
        UploadBatchFileResource(
            folder_path="folder_path_example",
            end=True,
            file_name="file_name_example",
            uploaded_path="uploaded_path_example",
            full_path="full_path_example",
            session_id="session_id_example",
        ),
    ] # [UploadBatchFileResource] | 
    batch_type = "KATALON_STUDIO" # str |  (optional) if omitted the server will use the default value of "KATALON_STUDIO"

    # example passing only required values which don't have defaults set
    try:
        # Saves and processes multiple uploaded Katalon reports.
        api_response = api_instance.process_multiple_s3_file(project_id, batch, upload_batch_file_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->process_multiple_s3_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Saves and processes multiple uploaded Katalon reports.
        api_response = api_instance.process_multiple_s3_file(project_id, batch, upload_batch_file_resource, batch_type=batch_type)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->process_multiple_s3_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **batch** | **str**|  |
 **upload_batch_file_resource** | [**[UploadBatchFileResource]**](UploadBatchFileResource.md)|  |
 **batch_type** | **str**|  | [optional] if omitted the server will use the default value of "KATALON_STUDIO"

### Return type

[**[UploadBatchResource]**](UploadBatchResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_multiple_s3_file_v2**
> [UploadBatchResource] process_multiple_s3_file_v2(project_id, batch, multiple_s3_file_resource)

Saves and processes multiple uploaded Katalon reports.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from testops_api.model.multiple_s3_file_resource import MultipleS3FileResource
from testops_api.model.upload_batch_resource import UploadBatchResource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = 1 # int | 
    batch = "batch_example" # str | 
    multiple_s3_file_resource = MultipleS3FileResource(
        upload_batch_file_resources=[
            UploadBatchFileResource(
                folder_path="folder_path_example",
                end=True,
                file_name="file_name_example",
                uploaded_path="uploaded_path_example",
                full_path="full_path_example",
                session_id="session_id_example",
            ),
        ],
        tags=[
            TagResource(
                id=1,
                name="name_example",
                project_id=1,
                organization_id=1,
            ),
        ],
        custom_field_options=[
            CustomFieldOptionResource(
                id=1,
                value="value_example",
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                definition_id=1,
            ),
        ],
    ) # MultipleS3FileResource | 

    # example passing only required values which don't have defaults set
    try:
        # Saves and processes multiple uploaded Katalon reports.
        api_response = api_instance.process_multiple_s3_file_v2(project_id, batch, multiple_s3_file_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->process_multiple_s3_file_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **batch** | **str**|  |
 **multiple_s3_file_resource** | [**MultipleS3FileResource**](MultipleS3FileResource.md)|  |

### Return type

[**[UploadBatchResource]**](UploadBatchResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_s3_file**
> [UploadBatchResource] process_s3_file(project_id, batch, folder_path, is_end, file_name, uploaded_path)

Saves and processes the uploaded Katalon reports.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from testops_api.model.upload_batch_resource import UploadBatchResource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = "projectId_example" # str | 
    batch = "batch_example" # str | 
    folder_path = "folderPath_example" # str | 
    is_end = "isEnd_example" # str | 
    file_name = "fileName_example" # str | 
    uploaded_path = "uploadedPath_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Saves and processes the uploaded Katalon reports.
        api_response = api_instance.process_s3_file(project_id, batch, folder_path, is_end, file_name, uploaded_path)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->process_s3_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch** | **str**|  |
 **folder_path** | **str**|  |
 **is_end** | **str**|  |
 **file_name** | **str**|  |
 **uploaded_path** | **str**|  |

### Return type

[**[UploadBatchResource]**](UploadBatchResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_test_ops_reports**
> UploadBatchResource process_test_ops_reports(project_id, batch, upload_batch_file_resource)

Saves and processes multiple uploaded TestOps reports.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from testops_api.model.upload_batch_file_resource import UploadBatchFileResource
from testops_api.model.upload_batch_resource import UploadBatchResource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = 1 # int | 
    batch = "batch_example" # str | 
    upload_batch_file_resource = [
        UploadBatchFileResource(
            folder_path="folder_path_example",
            end=True,
            file_name="file_name_example",
            uploaded_path="uploaded_path_example",
            full_path="full_path_example",
            session_id="session_id_example",
        ),
    ] # [UploadBatchFileResource] | 

    # example passing only required values which don't have defaults set
    try:
        # Saves and processes multiple uploaded TestOps reports.
        api_response = api_instance.process_test_ops_reports(project_id, batch, upload_batch_file_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->process_test_ops_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **batch** | **str**|  |
 **upload_batch_file_resource** | [**[UploadBatchFileResource]**](UploadBatchFileResource.md)|  |

### Return type

[**UploadBatchResource**](UploadBatchResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_result**
> ExecutionResource update_result(project_id, test_run_result)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from testops_api.model.execution_resource import ExecutionResource
from testops_api.model.test_run_result import TestRunResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = 1 # int | 
    test_run_result = TestRunResult(
        name="name_example",
        status="status_example",
        session_id="session_id_example",
        test_suite_id="test_suite_id_example",
        end=True,
    ) # TestRunResult | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_result(project_id, test_run_result)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->update_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **test_run_result** | [**TestRunResult**](TestRunResult.md)|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> upload(project_id, batch, is_end, file_name, uploaded_path)

Uploads and processes a Katalon Recorder report.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = "projectId_example" # str | 
    batch = "batch_example" # str | 
    is_end = "isEnd_example" # str | 
    file_name = "fileName_example" # str | 
    uploaded_path = "uploadedPath_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Uploads and processes a Katalon Recorder report.
        api_instance.upload(project_id, batch, is_end, file_name, uploaded_path)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch** | **str**|  |
 **is_end** | **str**|  |
 **file_name** | **str**|  |
 **uploaded_path** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_j_unit_reports**
> upload_j_unit_reports(project_id, batch, folder_path, is_end, file_name, uploaded_path)

Uploads and processes the JUnit reports to an Execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = "projectId_example" # str | 
    batch = "batch_example" # str | 
    folder_path = "folderPath_example" # str | 
    is_end = "isEnd_example" # str | 
    file_name = "fileName_example" # str | 
    uploaded_path = "uploadedPath_example" # str | 
    session_id = "sessionId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Uploads and processes the JUnit reports to an Execution.
        api_instance.upload_j_unit_reports(project_id, batch, folder_path, is_end, file_name, uploaded_path)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->upload_j_unit_reports: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Uploads and processes the JUnit reports to an Execution.
        api_instance.upload_j_unit_reports(project_id, batch, folder_path, is_end, file_name, uploaded_path, session_id=session_id)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->upload_j_unit_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch** | **str**|  |
 **folder_path** | **str**|  |
 **is_end** | **str**|  |
 **file_name** | **str**|  |
 **uploaded_path** | **str**|  |
 **session_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_j_unit_reports_v2**
> upload_j_unit_reports_v2(project_id, batch, folder_path, is_end, file_name, uploaded_path)

Uploads and processes the JUnit reports to an Execution with tag and custom field.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from testops_api.model.upload_j_unit_report_resource import UploadJUnitReportResource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    project_id = "projectId_example" # str | 
    batch = "batch_example" # str | 
    folder_path = "folderPath_example" # str | 
    is_end = "isEnd_example" # str | 
    file_name = "fileName_example" # str | 
    uploaded_path = "uploadedPath_example" # str | 
    session_id = "sessionId_example" # str |  (optional)
    upload_j_unit_report_resource = UploadJUnitReportResource(
        tags=[
            TagResource(
                id=1,
                name="name_example",
                project_id=1,
                organization_id=1,
            ),
        ],
        custom_field_options=[
            CustomFieldOptionResource(
                id=1,
                value="value_example",
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                definition_id=1,
            ),
        ],
    ) # UploadJUnitReportResource |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Uploads and processes the JUnit reports to an Execution with tag and custom field.
        api_instance.upload_j_unit_reports_v2(project_id, batch, folder_path, is_end, file_name, uploaded_path)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->upload_j_unit_reports_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Uploads and processes the JUnit reports to an Execution with tag and custom field.
        api_instance.upload_j_unit_reports_v2(project_id, batch, folder_path, is_end, file_name, uploaded_path, session_id=session_id, upload_j_unit_report_resource=upload_j_unit_report_resource)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->upload_j_unit_reports_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch** | **str**|  |
 **folder_path** | **str**|  |
 **is_end** | **str**|  |
 **file_name** | **str**|  |
 **uploaded_path** | **str**|  |
 **session_id** | **str**|  | [optional]
 **upload_j_unit_report_resource** | [**UploadJUnitReportResource**](UploadJUnitReportResource.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_test_ng_reports**
> upload_test_ng_reports(execution_id, project_id, batch, folder_path, is_end, file_name, uploaded_path)

Uploads and processes the TestNG reports to an execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import test_report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8443
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "http://localhost:8443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_report_api.TestReportApi(api_client)
    execution_id = 1 # int | 
    project_id = 1 # int | 
    batch = "batch_example" # str | 
    folder_path = "folderPath_example" # str | 
    is_end = True # bool | 
    file_name = "fileName_example" # str | 
    uploaded_path = "uploadedPath_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Uploads and processes the TestNG reports to an execution.
        api_instance.upload_test_ng_reports(execution_id, project_id, batch, folder_path, is_end, file_name, uploaded_path)
    except testops_api.ApiException as e:
        print("Exception when calling TestReportApi->upload_test_ng_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **int**|  |
 **project_id** | **int**|  |
 **batch** | **str**|  |
 **folder_path** | **str**|  |
 **is_end** | **bool**|  |
 **file_name** | **str**|  |
 **uploaded_path** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

