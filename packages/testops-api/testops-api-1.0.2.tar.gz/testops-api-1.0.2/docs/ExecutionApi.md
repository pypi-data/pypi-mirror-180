# testops_api.ExecutionApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_download**](ExecutionApi.md#bulk_download) | **GET** /api/v1/executions/download | Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.
[**delete6**](ExecutionApi.md#delete6) | **DELETE** /api/v1/executions | Deletes multiple Executions. Returns the deleted Execution details.
[**delete_tag1**](ExecutionApi.md#delete_tag1) | **DELETE** /api/v1/executions/{id}/tags | Delete tag of a Execution.
[**download6**](ExecutionApi.md#download6) | **GET** /api/v1/executions/{id}/download | Exports and downloads an Execution. Returns the Execution summary file.
[**download_file**](ExecutionApi.md#download_file) | **GET** /api/v1/executions/{id}/download-file | Downloads all uploaded files of an Execution. Returns the archive file comprising all Execution&#39;s files.
[**get16**](ExecutionApi.md#get16) | **GET** /api/v1/executions/{id} | Returns an Execution detail.
[**get_latest_executions**](ExecutionApi.md#get_latest_executions) | **GET** /api/v1/organizations/{id}/latest-executions | 
[**link_build1**](ExecutionApi.md#link_build1) | **POST** /api/v1/executions/{id}/link-build | Link an Execution to a Build. Returns the updated Execution detail.
[**link_release1**](ExecutionApi.md#link_release1) | **POST** /api/v1/executions/{id}/link-release | Link an Execution to a Release. Returns the updated Execution detail.
[**list2**](ExecutionApi.md#list2) | **GET** /api/v1/executions | 
[**push_to_xray**](ExecutionApi.md#push_to_xray) | **POST** /api/v1/executions/{id}/push-to-xray | Push an Execution to xray.
[**re_import_execution1**](ExecutionApi.md#re_import_execution1) | **POST** /api/v1/executions/reimport | Re-imports an Execution. Returns the newly imported Execution detail.
[**rerun_execution**](ExecutionApi.md#rerun_execution) | **POST** /api/v1/executions/{id}/rerun | Rerun an Execution.
[**share_execution_report**](ExecutionApi.md#share_execution_report) | **POST** /api/v1/executions/{id}/share-report | Allow users to send email with attached execution reports [PDF].
[**terminated_execution**](ExecutionApi.md#terminated_execution) | **POST** /api/v1/executions/terminate | Terminates a running Execution. Returns the terminated Execution detail.
[**unlink_release_and_build**](ExecutionApi.md#unlink_release_and_build) | **POST** /api/v1/executions/{id}/unlink-release | Unlink an Execution to a Release and Build. Returns the updated Execution detail.
[**update_custom_fields**](ExecutionApi.md#update_custom_fields) | **POST** /api/v1/executions/{id}/custom-fields | Update custom fields for execution.
[**update_tag1**](ExecutionApi.md#update_tag1) | **PUT** /api/v1/executions/{id}/tags | Update tag of a Execution.


# **bulk_download**
> bulk_download(id, project_id)

Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = [
        1,
    ] # [int] | 
    project_id = 1 # int | 
    file_type = "csv" # str |  (optional) if omitted the server will use the default value of "csv"

    # example passing only required values which don't have defaults set
    try:
        # Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.
        api_instance.bulk_download(id, project_id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->bulk_download: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.
        api_instance.bulk_download(id, project_id, file_type=file_type)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->bulk_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[int]**|  |
 **project_id** | **int**|  |
 **file_type** | **str**|  | [optional] if omitted the server will use the default value of "csv"

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

# **delete6**
> [ExecutionResource] delete6(project_id, order)

Deletes multiple Executions. Returns the deleted Execution details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    project_id = 1 # int | 
    order = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes multiple Executions. Returns the deleted Execution details.
        api_response = api_instance.delete6(project_id, order)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->delete6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **order** | **[int]**|  |

### Return type

[**[ExecutionResource]**](ExecutionResource.md)

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

# **delete_tag1**
> TagResource delete_tag1(id, tag_resource)

Delete tag of a Execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.tag_resource import TagResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    tag_resource = TagResource(
        id=1,
        name="name_example",
        project_id=1,
        organization_id=1,
    ) # TagResource | 

    # example passing only required values which don't have defaults set
    try:
        # Delete tag of a Execution.
        api_response = api_instance.delete_tag1(id, tag_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->delete_tag1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **tag_resource** | [**TagResource**](TagResource.md)|  |

### Return type

[**TagResource**](TagResource.md)

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

# **download6**
> download6(id)

Exports and downloads an Execution. Returns the Execution summary file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    file_type = "CSV" # str |  (optional) if omitted the server will use the default value of "CSV"

    # example passing only required values which don't have defaults set
    try:
        # Exports and downloads an Execution. Returns the Execution summary file.
        api_instance.download6(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->download6: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exports and downloads an Execution. Returns the Execution summary file.
        api_instance.download6(id, file_type=file_type)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->download6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **file_type** | **str**|  | [optional] if omitted the server will use the default value of "CSV"

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

# **download_file**
> download_file(id)

Downloads all uploaded files of an Execution. Returns the archive file comprising all Execution's files.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Downloads all uploaded files of an Execution. Returns the archive file comprising all Execution's files.
        api_instance.download_file(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

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

# **get16**
> ExecutionResource get16(id)

Returns an Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns an Execution detail.
        api_response = api_instance.get16(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->get16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **get_latest_executions**
> PageExecutionResource get_latest_executions(id, pageable)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_execution_resource import PageExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    pageable = Pageable(
        page=0,
        size=1,
        sort=[
            "sort_example",
        ],
    ) # Pageable | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_latest_executions(id, pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->get_latest_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **pageable** | **Pageable**|  |

### Return type

[**PageExecutionResource**](PageExecutionResource.md)

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

# **link_build1**
> ExecutionResource link_build1(id, build_id)

Link an Execution to a Build. Returns the updated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    build_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Execution to a Build. Returns the updated Execution detail.
        api_response = api_instance.link_build1(id, build_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->link_build1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **build_id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **link_release1**
> ExecutionResource link_release1(id, project_id, release_id)

Link an Execution to a Release. Returns the updated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    project_id = 1 # int | 
    release_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Execution to a Release. Returns the updated Execution detail.
        api_response = api_instance.link_release1(id, project_id, release_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->link_release1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **project_id** | **int**|  |
 **release_id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **list2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list2(pageable)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.pageable import Pageable
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
    api_instance = execution_api.ExecutionApi(api_client)
    pageable = Pageable(
        page=0,
        size=1,
        sort=[
            "sort_example",
        ],
    ) # Pageable | 
    batch = "batch_example" # str |  (optional)
    project_id = 1 # int |  (optional)
    order = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list2(pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->list2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list2(pageable, batch=batch, project_id=project_id, order=order)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->list2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | **Pageable**|  |
 **batch** | **str**|  | [optional]
 **project_id** | **int**|  | [optional]
 **order** | **int**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **push_to_xray**
> ExternalIssueResource push_to_xray(id)

Push an Execution to xray.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.external_issue_resource import ExternalIssueResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    xray_test_plan_id = "xrayTestPlanId_example" # str |  (optional)
    external_release_id = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Push an Execution to xray.
        api_response = api_instance.push_to_xray(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->push_to_xray: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Push an Execution to xray.
        api_response = api_instance.push_to_xray(id, xray_test_plan_id=xray_test_plan_id, external_release_id=external_release_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->push_to_xray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **xray_test_plan_id** | **str**|  | [optional]
 **external_release_id** | **int**|  | [optional]

### Return type

[**ExternalIssueResource**](ExternalIssueResource.md)

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

# **re_import_execution1**
> ExecutionResource re_import_execution1(id)

Re-imports an Execution. Returns the newly imported Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Re-imports an Execution. Returns the newly imported Execution detail.
        api_response = api_instance.re_import_execution1(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->re_import_execution1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **rerun_execution**
> rerun_execution(id)

Rerun an Execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Rerun an Execution.
        api_instance.rerun_execution(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->rerun_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

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

# **share_execution_report**
> share_execution_report(id, execution_share_report_resource)

Allow users to send email with attached execution reports [PDF].

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_share_report_resource import ExecutionShareReportResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    execution_share_report_resource = ExecutionShareReportResource(
        emails=[
            "emails_example",
        ],
        execution_id=1,
    ) # ExecutionShareReportResource | 

    # example passing only required values which don't have defaults set
    try:
        # Allow users to send email with attached execution reports [PDF].
        api_instance.share_execution_report(id, execution_share_report_resource)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->share_execution_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **execution_share_report_resource** | [**ExecutionShareReportResource**](ExecutionShareReportResource.md)|  |

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

# **terminated_execution**
> ExecutionResource terminated_execution(project_id, order)

Terminates a running Execution. Returns the terminated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    project_id = 1 # int | 
    order = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Terminates a running Execution. Returns the terminated Execution detail.
        api_response = api_instance.terminated_execution(project_id, order)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->terminated_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **order** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **unlink_release_and_build**
> ExecutionResource unlink_release_and_build(id)

Unlink an Execution to a Release and Build. Returns the updated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink an Execution to a Release and Build. Returns the updated Execution detail.
        api_response = api_instance.unlink_release_and_build(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->unlink_release_and_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **update_custom_fields**
> ExecutionResource update_custom_fields(id, custom_field_option_resource)

Update custom fields for execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
from testops_api.model.custom_field_option_resource import CustomFieldOptionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    custom_field_option_resource = [
        CustomFieldOptionResource(
            id=1,
            value="value_example",
            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            definition_id=1,
        ),
    ] # [CustomFieldOptionResource] | 

    # example passing only required values which don't have defaults set
    try:
        # Update custom fields for execution.
        api_response = api_instance.update_custom_fields(id, custom_field_option_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->update_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **custom_field_option_resource** | [**[CustomFieldOptionResource]**](CustomFieldOptionResource.md)|  |

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

# **update_tag1**
> TagResource update_tag1(id, tag_resource)

Update tag of a Execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.tag_resource import TagResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    tag_resource = TagResource(
        id=1,
        name="name_example",
        project_id=1,
        organization_id=1,
    ) # TagResource | 

    # example passing only required values which don't have defaults set
    try:
        # Update tag of a Execution.
        api_response = api_instance.update_tag1(id, tag_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->update_tag1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **tag_resource** | [**TagResource**](TagResource.md)|  |

### Return type

[**TagResource**](TagResource.md)

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

