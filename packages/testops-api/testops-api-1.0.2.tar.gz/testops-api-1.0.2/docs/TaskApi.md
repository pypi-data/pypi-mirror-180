# testops_api.TaskApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_incident**](TaskApi.md#create_incident) | **POST** /api/v1/incidents | Creates a Task for the test results. Returns the created Task detail.
[**get15**](TaskApi.md#get15) | **GET** /api/v1/incidents/{id} | Returns a Task detail.
[**link_incidents**](TaskApi.md#link_incidents) | **POST** /api/v1/test-results/{id}/incidents | Link an Execution Test Result to a Task. Returns the created binding detail.
[**unlink_incidents**](TaskApi.md#unlink_incidents) | **DELETE** /api/v1/test-results/{id}/incidents | Unlink an Execution Test Result to a Task. Returns the deleted binding detail.
[**update6**](TaskApi.md#update6) | **PUT** /api/v1/incidents | Updates a Task detail. Returns the updated Task detail.


# **create_incident**
> IncidentResource create_incident(incident_resource)

Creates a Task for the test results. Returns the created Task detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_resource import IncidentResource
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
    api_instance = task_api.TaskApi(api_client)
    incident_resource = IncidentResource(
        id=1,
        name="name_example",
        description="description_example",
        project_id=1,
        team_id=1,
        url_ids=[
            "url_ids_example",
        ],
        execution_test_result_ids=[
            1,
        ],
        order=1,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # IncidentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a Task for the test results. Returns the created Task detail.
        api_response = api_instance.create_incident(incident_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->create_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_resource** | [**IncidentResource**](IncidentResource.md)|  |

### Return type

[**IncidentResource**](IncidentResource.md)

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

# **get15**
> IncidentResource get15(id)

Returns a Task detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_resource import IncidentResource
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
    api_instance = task_api.TaskApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Task detail.
        api_response = api_instance.get15(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->get15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**IncidentResource**](IncidentResource.md)

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

# **link_incidents**
> IncidentExecutionTestResultResource link_incidents(id, incident_execution_test_result_resource)

Link an Execution Test Result to a Task. Returns the created binding detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_execution_test_result_resource import IncidentExecutionTestResultResource
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
    api_instance = task_api.TaskApi(api_client)
    id = "id_example" # str | 
    incident_execution_test_result_resource = IncidentExecutionTestResultResource(
        id=1,
        incident_id=1,
        project_id=1,
        incident_order=1,
        execution_test_result_id=1,
    ) # IncidentExecutionTestResultResource | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Execution Test Result to a Task. Returns the created binding detail.
        api_response = api_instance.link_incidents(id, incident_execution_test_result_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->link_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **incident_execution_test_result_resource** | [**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)|  |

### Return type

[**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)

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

# **unlink_incidents**
> IncidentExecutionTestResultResource unlink_incidents(id, incident_execution_test_result_resource)

Unlink an Execution Test Result to a Task. Returns the deleted binding detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_execution_test_result_resource import IncidentExecutionTestResultResource
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
    api_instance = task_api.TaskApi(api_client)
    id = "id_example" # str | 
    incident_execution_test_result_resource = IncidentExecutionTestResultResource(
        id=1,
        incident_id=1,
        project_id=1,
        incident_order=1,
        execution_test_result_id=1,
    ) # IncidentExecutionTestResultResource | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink an Execution Test Result to a Task. Returns the deleted binding detail.
        api_response = api_instance.unlink_incidents(id, incident_execution_test_result_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->unlink_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **incident_execution_test_result_resource** | [**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)|  |

### Return type

[**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)

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

# **update6**
> IncidentResource update6(incident_resource)

Updates a Task detail. Returns the updated Task detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_resource import IncidentResource
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
    api_instance = task_api.TaskApi(api_client)
    incident_resource = IncidentResource(
        id=1,
        name="name_example",
        description="description_example",
        project_id=1,
        team_id=1,
        url_ids=[
            "url_ids_example",
        ],
        execution_test_result_ids=[
            1,
        ],
        order=1,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # IncidentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Task detail. Returns the updated Task detail.
        api_response = api_instance.update6(incident_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->update6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_resource** | [**IncidentResource**](IncidentResource.md)|  |

### Return type

[**IncidentResource**](IncidentResource.md)

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

