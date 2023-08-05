# testops_api.OrganizationTrialRequestResourceControllerApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trial_request**](OrganizationTrialRequestResourceControllerApi.md#get_trial_request) | **GET** /api/v1/organizations/{id}/trial-request | Get organization trial request data
[**submit_trial_request**](OrganizationTrialRequestResourceControllerApi.md#submit_trial_request) | **POST** /api/v1/organizations/{id}/trial-request | Submit organization trial request


# **get_trial_request**
> OrganizationTrialRequestResource get_trial_request(id)

Get organization trial request data

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import organization_trial_request_resource_controller_api
from testops_api.model.organization_trial_request_resource import OrganizationTrialRequestResource
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
    api_instance = organization_trial_request_resource_controller_api.OrganizationTrialRequestResourceControllerApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get organization trial request data
        api_response = api_instance.get_trial_request(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling OrganizationTrialRequestResourceControllerApi->get_trial_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**OrganizationTrialRequestResource**](OrganizationTrialRequestResource.md)

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

# **submit_trial_request**
> OrganizationTrialRequestResource submit_trial_request(id, feature)

Submit organization trial request

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import organization_trial_request_resource_controller_api
from testops_api.model.organization_trial_request_resource import OrganizationTrialRequestResource
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
    api_instance = organization_trial_request_resource_controller_api.OrganizationTrialRequestResourceControllerApi(api_client)
    id = 1 # int | 
    feature = "KSE" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Submit organization trial request
        api_response = api_instance.submit_trial_request(id, feature)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling OrganizationTrialRequestResourceControllerApi->submit_trial_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **feature** | **str**|  |

### Return type

[**OrganizationTrialRequestResource**](OrganizationTrialRequestResource.md)

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

