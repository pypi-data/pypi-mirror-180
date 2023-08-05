# testops_api.ProjectApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create4**](ProjectApi.md#create4) | **POST** /api/v1/projects | Creates a new Project. Returns the created Project detail.
[**create_default_custom_fields**](ProjectApi.md#create_default_custom_fields) | **POST** /api/v1/projects/{id}/default-custom-fields | Create default custom field for project.
[**create_or_update2**](ProjectApi.md#create_or_update2) | **POST** /api/v1/project-settings | 
[**create_sample_data**](ProjectApi.md#create_sample_data) | **POST** /api/v1/projects/{id}/sample-data | Create sample data for project.
[**delete5**](ProjectApi.md#delete5) | **DELETE** /api/v1/projects/{id} | Deletes a Project. Returns the deleted Project detail.
[**get10**](ProjectApi.md#get10) | **GET** /api/v1/projects/{id} | Returns a Project detail.
[**get11**](ProjectApi.md#get11) | **GET** /api/v1/project-settings/{id} | 
[**get_by_user_with_repository_info**](ProjectApi.md#get_by_user_with_repository_info) | **GET** /api/v1/projects/platform-projects | Returns all Projects of User, include repository information.
[**is_required_git_repository**](ProjectApi.md#is_required_git_repository) | **GET** /api/v1/projects/{id}/check-required-git-repo | Check is required git repository for a project
[**list1**](ProjectApi.md#list1) | **GET** /api/v1/projects | Returns all Projects of a Team.
[**update4**](ProjectApi.md#update4) | **PUT** /api/v1/projects | Updates a Project detail. Returns the updated Project detail.
[**update_status**](ProjectApi.md#update_status) | **PUT** /api/v1/projects/update-status | Updates a Project status. Returns the updated Project detail.


# **create4**
> ProjectResource create4(project_resource)

Creates a new Project. Returns the created Project detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_resource import ProjectResource
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
    api_instance = project_api.ProjectApi(api_client)
    project_resource = ProjectResource(
        id=1,
        name="name_example",
        team_id=1,
        team=TeamResource(
            id=1,
            name="name_example",
            role="OWNER",
            users=[
                UserResource(
                    id=1,
                    email="email_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    password="password_example",
                    inviting_url="inviting_url_example",
                    avatar="avatar_example",
                    configs=ConfigResource(
                        web_socket_url="web_socket_url_example",
                        store_url="store_url_example",
                        profiles=[
                            "profiles_example",
                        ],
                        stripe_public_api="stripe_public_api_example",
                        build_version="build_version_example",
                        commit_id="commit_id_example",
                        sentry_dsn="sentry_dsn_example",
                        sentry_env="sentry_env_example",
                        sentry_traces_sample_rate="sentry_traces_sample_rate_example",
                        server_url="server_url_example",
                        io_server_url="io_server_url_example",
                        proxy_tunnel_server_url="proxy_tunnel_server_url_example",
                        max_execution_comparison=1,
                        max_execution_download=1,
                        agent_download_urls={
                            "key": "key_example",
                        },
                        proxy_tunnel_download_urls={
                            "key": "key_example",
                        },
                        report_uploader_download_url="report_uploader_download_url_example",
                        report_uploader_latest_version="report_uploader_latest_version_example",
                        sub_domain_pattern="sub_domain_pattern_example",
                        cancellation_survey_url="cancellation_survey_url_example",
                        launch_darkly_client_id="launch_darkly_client_id_example",
                        launch_darkly_default_user="launch_darkly_default_user_example",
                        launch_darkly_prefix="launch_darkly_prefix_example",
                        min_test_execution_ordered=1,
                        user_flow_token="user_flow_token_example",
                        demo_project_url="demo_project_url_example",
                        advanced_feature_enabled=True,
                        using_sub_domain=True,
                        test_ops_subscription_enabled=True,
                        frameworks_integration_enabled=True,
                    ),
                    projects=[
                        ProjectResource(ProjectResource),
                    ],
                    teams=[
                        TeamResource(TeamResource),
                    ],
                    organizations=[
                        OrganizationResource(
                            id=1,
                            name="name_example",
                            role="OWNER",
                            org_feature_flag=OrganizationFeatureFlagResource(
                                organization_id=1,
                                sub_domain=True,
                                strict_domain=True,
                                sso=True,
                                whitelist_ip=True,
                                circle_ci=True,
                                test_ops_integration=True,
                            ),
                            quota_kse=1,
                            machine_quota_kse=1,
                            quota_unlimited_kse=1,
                            quota_engine=1,
                            machine_quota_engine=1,
                            quota_unlimited_engine=1,
                            used_kse=1,
                            used_unlimited_kse=1,
                            used_engine=1,
                            used_unlimited_engine=1,
                            quota_test_ops=1,
                            used_test_ops=1,
                            number_user=1,
                            quota_floating_engine=1,
                            used_floating_engine=1,
                            can_create_offline_kse=True,
                            can_create_offline_unlimited_kse=True,
                            can_create_offline_re=True,
                            can_create_offline_unlimited_engine=True,
                            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscribed=True,
                            kse_paygo=True,
                            kre_paygo=True,
                            paygo_quota=1,
                            domain="domain_example",
                            subdomain_url="subdomain_url_example",
                            strict_domain=True,
                            logo_url="logo_url_example",
                            saml_sso=True,
                            kre_license=True,
                            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            account_id=1,
                            test_ops_feature="KSE",
                            platform_feature="KSE",
                            tier="FREE",
                            requested_user_verified=True,
                        ),
                    ],
                    organization_feature=[
                        UserOrganizationFeatureResource(
                            user=UserResource(UserResource),
                            user_id=1,
                            organization_id=1,
                            user_email="user_email_example",
                            organization=OrganizationResource(
                                id=1,
                                name="name_example",
                                role="OWNER",
                                org_feature_flag=OrganizationFeatureFlagResource(
                                    organization_id=1,
                                    sub_domain=True,
                                    strict_domain=True,
                                    sso=True,
                                    whitelist_ip=True,
                                    circle_ci=True,
                                    test_ops_integration=True,
                                ),
                                quota_kse=1,
                                machine_quota_kse=1,
                                quota_unlimited_kse=1,
                                quota_engine=1,
                                machine_quota_engine=1,
                                quota_unlimited_engine=1,
                                used_kse=1,
                                used_unlimited_kse=1,
                                used_engine=1,
                                used_unlimited_engine=1,
                                quota_test_ops=1,
                                used_test_ops=1,
                                number_user=1,
                                quota_floating_engine=1,
                                used_floating_engine=1,
                                can_create_offline_kse=True,
                                can_create_offline_unlimited_kse=True,
                                can_create_offline_re=True,
                                can_create_offline_unlimited_engine=True,
                                subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscribed=True,
                                kse_paygo=True,
                                kre_paygo=True,
                                paygo_quota=1,
                                domain="domain_example",
                                subdomain_url="subdomain_url_example",
                                strict_domain=True,
                                logo_url="logo_url_example",
                                saml_sso=True,
                                kre_license=True,
                                most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                account_id=1,
                                test_ops_feature="KSE",
                                platform_feature="KSE",
                                tier="FREE",
                                requested_user_verified=True,
                            ),
                            feature="KSE",
                        ),
                    ],
                    trial_expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    system_role="USER",
                    survey_status="NOT_SUBMITTED",
                    session_timeout=1,
                    business_user=True,
                    can_create_offline_kse=True,
                    can_create_offline_re=True,
                    saml_sso=True,
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    full_name="full_name_example",
                ),
            ],
            organization=OrganizationResource(
                id=1,
                name="name_example",
                role="OWNER",
                org_feature_flag=OrganizationFeatureFlagResource(
                    organization_id=1,
                    sub_domain=True,
                    strict_domain=True,
                    sso=True,
                    whitelist_ip=True,
                    circle_ci=True,
                    test_ops_integration=True,
                ),
                quota_kse=1,
                machine_quota_kse=1,
                quota_unlimited_kse=1,
                quota_engine=1,
                machine_quota_engine=1,
                quota_unlimited_engine=1,
                used_kse=1,
                used_unlimited_kse=1,
                used_engine=1,
                used_unlimited_engine=1,
                quota_test_ops=1,
                used_test_ops=1,
                number_user=1,
                quota_floating_engine=1,
                used_floating_engine=1,
                can_create_offline_kse=True,
                can_create_offline_unlimited_kse=True,
                can_create_offline_re=True,
                can_create_offline_unlimited_engine=True,
                subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscribed=True,
                kse_paygo=True,
                kre_paygo=True,
                paygo_quota=1,
                domain="domain_example",
                subdomain_url="subdomain_url_example",
                strict_domain=True,
                logo_url="logo_url_example",
                saml_sso=True,
                kre_license=True,
                most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                account_id=1,
                test_ops_feature="KSE",
                platform_feature="KSE",
                tier="FREE",
                requested_user_verified=True,
            ),
            organization_id=1,
        ),
        timezone="timezone_example",
        status="ARCHIVE",
    ) # ProjectResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Project. Returns the created Project detail.
        api_response = api_instance.create4(project_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->create4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource** | [**ProjectResource**](ProjectResource.md)|  |

### Return type

[**ProjectResource**](ProjectResource.md)

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

# **create_default_custom_fields**
> create_default_custom_fields(id)

Create default custom field for project.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
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
    api_instance = project_api.ProjectApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Create default custom field for project.
        api_instance.create_default_custom_fields(id)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->create_default_custom_fields: %s\n" % e)
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

# **create_or_update2**
> ProjectSettingResource create_or_update2(project_setting_resource)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_setting_resource import ProjectSettingResource
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
    api_instance = project_api.ProjectApi(api_client)
    project_setting_resource = ProjectSettingResource(
        project_id=1,
        bdd=True,
    ) # ProjectSettingResource | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_update2(project_setting_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->create_or_update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_setting_resource** | [**ProjectSettingResource**](ProjectSettingResource.md)|  |

### Return type

[**ProjectSettingResource**](ProjectSettingResource.md)

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

# **create_sample_data**
> create_sample_data(id)

Create sample data for project.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
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
    api_instance = project_api.ProjectApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Create sample data for project.
        api_instance.create_sample_data(id)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->create_sample_data: %s\n" % e)
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

# **delete5**
> ProjectResource delete5(id)

Deletes a Project. Returns the deleted Project detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_resource import ProjectResource
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
    api_instance = project_api.ProjectApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Project. Returns the deleted Project detail.
        api_response = api_instance.delete5(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->delete5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ProjectResource**](ProjectResource.md)

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

# **get10**
> ProjectResource get10(id)

Returns a Project detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_resource import ProjectResource
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
    api_instance = project_api.ProjectApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Project detail.
        api_response = api_instance.get10(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->get10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ProjectResource**](ProjectResource.md)

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

# **get11**
> ProjectSettingResource get11(id)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_setting_resource import ProjectSettingResource
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
    api_instance = project_api.ProjectApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get11(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->get11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ProjectSettingResource**](ProjectSettingResource.md)

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

# **get_by_user_with_repository_info**
> [PlatformProjectResource] get_by_user_with_repository_info()

Returns all Projects of User, include repository information.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.platform_project_resource import PlatformProjectResource
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
    api_instance = project_api.ProjectApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all Projects of User, include repository information.
        api_response = api_instance.get_by_user_with_repository_info()
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->get_by_user_with_repository_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[PlatformProjectResource]**](PlatformProjectResource.md)

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

# **is_required_git_repository**
> bool is_required_git_repository(id)

Check is required git repository for a project

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
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
    api_instance = project_api.ProjectApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Check is required git repository for a project
        api_response = api_instance.is_required_git_repository(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->is_required_git_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

**bool**

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

# **list1**
> PageProjectResource list1(pageable)

Returns all Projects of a Team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_project_resource import PageProjectResource
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
    api_instance = project_api.ProjectApi(api_client)
    pageable = Pageable(
        page=0,
        size=1,
        sort=[
            "sort_example",
        ],
    ) # Pageable | 
    team_id = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns all Projects of a Team.
        api_response = api_instance.list1(pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->list1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all Projects of a Team.
        api_response = api_instance.list1(pageable, team_id=team_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | **Pageable**|  |
 **team_id** | **int**|  | [optional]

### Return type

[**PageProjectResource**](PageProjectResource.md)

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

# **update4**
> ProjectResource update4(project_resource)

Updates a Project detail. Returns the updated Project detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_resource import ProjectResource
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
    api_instance = project_api.ProjectApi(api_client)
    project_resource = ProjectResource(
        id=1,
        name="name_example",
        team_id=1,
        team=TeamResource(
            id=1,
            name="name_example",
            role="OWNER",
            users=[
                UserResource(
                    id=1,
                    email="email_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    password="password_example",
                    inviting_url="inviting_url_example",
                    avatar="avatar_example",
                    configs=ConfigResource(
                        web_socket_url="web_socket_url_example",
                        store_url="store_url_example",
                        profiles=[
                            "profiles_example",
                        ],
                        stripe_public_api="stripe_public_api_example",
                        build_version="build_version_example",
                        commit_id="commit_id_example",
                        sentry_dsn="sentry_dsn_example",
                        sentry_env="sentry_env_example",
                        sentry_traces_sample_rate="sentry_traces_sample_rate_example",
                        server_url="server_url_example",
                        io_server_url="io_server_url_example",
                        proxy_tunnel_server_url="proxy_tunnel_server_url_example",
                        max_execution_comparison=1,
                        max_execution_download=1,
                        agent_download_urls={
                            "key": "key_example",
                        },
                        proxy_tunnel_download_urls={
                            "key": "key_example",
                        },
                        report_uploader_download_url="report_uploader_download_url_example",
                        report_uploader_latest_version="report_uploader_latest_version_example",
                        sub_domain_pattern="sub_domain_pattern_example",
                        cancellation_survey_url="cancellation_survey_url_example",
                        launch_darkly_client_id="launch_darkly_client_id_example",
                        launch_darkly_default_user="launch_darkly_default_user_example",
                        launch_darkly_prefix="launch_darkly_prefix_example",
                        min_test_execution_ordered=1,
                        user_flow_token="user_flow_token_example",
                        demo_project_url="demo_project_url_example",
                        advanced_feature_enabled=True,
                        using_sub_domain=True,
                        test_ops_subscription_enabled=True,
                        frameworks_integration_enabled=True,
                    ),
                    projects=[
                        ProjectResource(ProjectResource),
                    ],
                    teams=[
                        TeamResource(TeamResource),
                    ],
                    organizations=[
                        OrganizationResource(
                            id=1,
                            name="name_example",
                            role="OWNER",
                            org_feature_flag=OrganizationFeatureFlagResource(
                                organization_id=1,
                                sub_domain=True,
                                strict_domain=True,
                                sso=True,
                                whitelist_ip=True,
                                circle_ci=True,
                                test_ops_integration=True,
                            ),
                            quota_kse=1,
                            machine_quota_kse=1,
                            quota_unlimited_kse=1,
                            quota_engine=1,
                            machine_quota_engine=1,
                            quota_unlimited_engine=1,
                            used_kse=1,
                            used_unlimited_kse=1,
                            used_engine=1,
                            used_unlimited_engine=1,
                            quota_test_ops=1,
                            used_test_ops=1,
                            number_user=1,
                            quota_floating_engine=1,
                            used_floating_engine=1,
                            can_create_offline_kse=True,
                            can_create_offline_unlimited_kse=True,
                            can_create_offline_re=True,
                            can_create_offline_unlimited_engine=True,
                            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscribed=True,
                            kse_paygo=True,
                            kre_paygo=True,
                            paygo_quota=1,
                            domain="domain_example",
                            subdomain_url="subdomain_url_example",
                            strict_domain=True,
                            logo_url="logo_url_example",
                            saml_sso=True,
                            kre_license=True,
                            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            account_id=1,
                            test_ops_feature="KSE",
                            platform_feature="KSE",
                            tier="FREE",
                            requested_user_verified=True,
                        ),
                    ],
                    organization_feature=[
                        UserOrganizationFeatureResource(
                            user=UserResource(UserResource),
                            user_id=1,
                            organization_id=1,
                            user_email="user_email_example",
                            organization=OrganizationResource(
                                id=1,
                                name="name_example",
                                role="OWNER",
                                org_feature_flag=OrganizationFeatureFlagResource(
                                    organization_id=1,
                                    sub_domain=True,
                                    strict_domain=True,
                                    sso=True,
                                    whitelist_ip=True,
                                    circle_ci=True,
                                    test_ops_integration=True,
                                ),
                                quota_kse=1,
                                machine_quota_kse=1,
                                quota_unlimited_kse=1,
                                quota_engine=1,
                                machine_quota_engine=1,
                                quota_unlimited_engine=1,
                                used_kse=1,
                                used_unlimited_kse=1,
                                used_engine=1,
                                used_unlimited_engine=1,
                                quota_test_ops=1,
                                used_test_ops=1,
                                number_user=1,
                                quota_floating_engine=1,
                                used_floating_engine=1,
                                can_create_offline_kse=True,
                                can_create_offline_unlimited_kse=True,
                                can_create_offline_re=True,
                                can_create_offline_unlimited_engine=True,
                                subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscribed=True,
                                kse_paygo=True,
                                kre_paygo=True,
                                paygo_quota=1,
                                domain="domain_example",
                                subdomain_url="subdomain_url_example",
                                strict_domain=True,
                                logo_url="logo_url_example",
                                saml_sso=True,
                                kre_license=True,
                                most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                account_id=1,
                                test_ops_feature="KSE",
                                platform_feature="KSE",
                                tier="FREE",
                                requested_user_verified=True,
                            ),
                            feature="KSE",
                        ),
                    ],
                    trial_expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    system_role="USER",
                    survey_status="NOT_SUBMITTED",
                    session_timeout=1,
                    business_user=True,
                    can_create_offline_kse=True,
                    can_create_offline_re=True,
                    saml_sso=True,
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    full_name="full_name_example",
                ),
            ],
            organization=OrganizationResource(
                id=1,
                name="name_example",
                role="OWNER",
                org_feature_flag=OrganizationFeatureFlagResource(
                    organization_id=1,
                    sub_domain=True,
                    strict_domain=True,
                    sso=True,
                    whitelist_ip=True,
                    circle_ci=True,
                    test_ops_integration=True,
                ),
                quota_kse=1,
                machine_quota_kse=1,
                quota_unlimited_kse=1,
                quota_engine=1,
                machine_quota_engine=1,
                quota_unlimited_engine=1,
                used_kse=1,
                used_unlimited_kse=1,
                used_engine=1,
                used_unlimited_engine=1,
                quota_test_ops=1,
                used_test_ops=1,
                number_user=1,
                quota_floating_engine=1,
                used_floating_engine=1,
                can_create_offline_kse=True,
                can_create_offline_unlimited_kse=True,
                can_create_offline_re=True,
                can_create_offline_unlimited_engine=True,
                subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscribed=True,
                kse_paygo=True,
                kre_paygo=True,
                paygo_quota=1,
                domain="domain_example",
                subdomain_url="subdomain_url_example",
                strict_domain=True,
                logo_url="logo_url_example",
                saml_sso=True,
                kre_license=True,
                most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                account_id=1,
                test_ops_feature="KSE",
                platform_feature="KSE",
                tier="FREE",
                requested_user_verified=True,
            ),
            organization_id=1,
        ),
        timezone="timezone_example",
        status="ARCHIVE",
    ) # ProjectResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Project detail. Returns the updated Project detail.
        api_response = api_instance.update4(project_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->update4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource** | [**ProjectResource**](ProjectResource.md)|  |

### Return type

[**ProjectResource**](ProjectResource.md)

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

# **update_status**
> ProjectResource update_status(project_resource)

Updates a Project status. Returns the updated Project detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_api
from testops_api.model.project_resource import ProjectResource
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
    api_instance = project_api.ProjectApi(api_client)
    project_resource = ProjectResource(
        id=1,
        name="name_example",
        team_id=1,
        team=TeamResource(
            id=1,
            name="name_example",
            role="OWNER",
            users=[
                UserResource(
                    id=1,
                    email="email_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    password="password_example",
                    inviting_url="inviting_url_example",
                    avatar="avatar_example",
                    configs=ConfigResource(
                        web_socket_url="web_socket_url_example",
                        store_url="store_url_example",
                        profiles=[
                            "profiles_example",
                        ],
                        stripe_public_api="stripe_public_api_example",
                        build_version="build_version_example",
                        commit_id="commit_id_example",
                        sentry_dsn="sentry_dsn_example",
                        sentry_env="sentry_env_example",
                        sentry_traces_sample_rate="sentry_traces_sample_rate_example",
                        server_url="server_url_example",
                        io_server_url="io_server_url_example",
                        proxy_tunnel_server_url="proxy_tunnel_server_url_example",
                        max_execution_comparison=1,
                        max_execution_download=1,
                        agent_download_urls={
                            "key": "key_example",
                        },
                        proxy_tunnel_download_urls={
                            "key": "key_example",
                        },
                        report_uploader_download_url="report_uploader_download_url_example",
                        report_uploader_latest_version="report_uploader_latest_version_example",
                        sub_domain_pattern="sub_domain_pattern_example",
                        cancellation_survey_url="cancellation_survey_url_example",
                        launch_darkly_client_id="launch_darkly_client_id_example",
                        launch_darkly_default_user="launch_darkly_default_user_example",
                        launch_darkly_prefix="launch_darkly_prefix_example",
                        min_test_execution_ordered=1,
                        user_flow_token="user_flow_token_example",
                        demo_project_url="demo_project_url_example",
                        advanced_feature_enabled=True,
                        using_sub_domain=True,
                        test_ops_subscription_enabled=True,
                        frameworks_integration_enabled=True,
                    ),
                    projects=[
                        ProjectResource(ProjectResource),
                    ],
                    teams=[
                        TeamResource(TeamResource),
                    ],
                    organizations=[
                        OrganizationResource(
                            id=1,
                            name="name_example",
                            role="OWNER",
                            org_feature_flag=OrganizationFeatureFlagResource(
                                organization_id=1,
                                sub_domain=True,
                                strict_domain=True,
                                sso=True,
                                whitelist_ip=True,
                                circle_ci=True,
                                test_ops_integration=True,
                            ),
                            quota_kse=1,
                            machine_quota_kse=1,
                            quota_unlimited_kse=1,
                            quota_engine=1,
                            machine_quota_engine=1,
                            quota_unlimited_engine=1,
                            used_kse=1,
                            used_unlimited_kse=1,
                            used_engine=1,
                            used_unlimited_engine=1,
                            quota_test_ops=1,
                            used_test_ops=1,
                            number_user=1,
                            quota_floating_engine=1,
                            used_floating_engine=1,
                            can_create_offline_kse=True,
                            can_create_offline_unlimited_kse=True,
                            can_create_offline_re=True,
                            can_create_offline_unlimited_engine=True,
                            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscribed=True,
                            kse_paygo=True,
                            kre_paygo=True,
                            paygo_quota=1,
                            domain="domain_example",
                            subdomain_url="subdomain_url_example",
                            strict_domain=True,
                            logo_url="logo_url_example",
                            saml_sso=True,
                            kre_license=True,
                            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            account_id=1,
                            test_ops_feature="KSE",
                            platform_feature="KSE",
                            tier="FREE",
                            requested_user_verified=True,
                        ),
                    ],
                    organization_feature=[
                        UserOrganizationFeatureResource(
                            user=UserResource(UserResource),
                            user_id=1,
                            organization_id=1,
                            user_email="user_email_example",
                            organization=OrganizationResource(
                                id=1,
                                name="name_example",
                                role="OWNER",
                                org_feature_flag=OrganizationFeatureFlagResource(
                                    organization_id=1,
                                    sub_domain=True,
                                    strict_domain=True,
                                    sso=True,
                                    whitelist_ip=True,
                                    circle_ci=True,
                                    test_ops_integration=True,
                                ),
                                quota_kse=1,
                                machine_quota_kse=1,
                                quota_unlimited_kse=1,
                                quota_engine=1,
                                machine_quota_engine=1,
                                quota_unlimited_engine=1,
                                used_kse=1,
                                used_unlimited_kse=1,
                                used_engine=1,
                                used_unlimited_engine=1,
                                quota_test_ops=1,
                                used_test_ops=1,
                                number_user=1,
                                quota_floating_engine=1,
                                used_floating_engine=1,
                                can_create_offline_kse=True,
                                can_create_offline_unlimited_kse=True,
                                can_create_offline_re=True,
                                can_create_offline_unlimited_engine=True,
                                subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                subscribed=True,
                                kse_paygo=True,
                                kre_paygo=True,
                                paygo_quota=1,
                                domain="domain_example",
                                subdomain_url="subdomain_url_example",
                                strict_domain=True,
                                logo_url="logo_url_example",
                                saml_sso=True,
                                kre_license=True,
                                most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                account_id=1,
                                test_ops_feature="KSE",
                                platform_feature="KSE",
                                tier="FREE",
                                requested_user_verified=True,
                            ),
                            feature="KSE",
                        ),
                    ],
                    trial_expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    system_role="USER",
                    survey_status="NOT_SUBMITTED",
                    session_timeout=1,
                    business_user=True,
                    can_create_offline_kse=True,
                    can_create_offline_re=True,
                    saml_sso=True,
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    full_name="full_name_example",
                ),
            ],
            organization=OrganizationResource(
                id=1,
                name="name_example",
                role="OWNER",
                org_feature_flag=OrganizationFeatureFlagResource(
                    organization_id=1,
                    sub_domain=True,
                    strict_domain=True,
                    sso=True,
                    whitelist_ip=True,
                    circle_ci=True,
                    test_ops_integration=True,
                ),
                quota_kse=1,
                machine_quota_kse=1,
                quota_unlimited_kse=1,
                quota_engine=1,
                machine_quota_engine=1,
                quota_unlimited_engine=1,
                used_kse=1,
                used_unlimited_kse=1,
                used_engine=1,
                used_unlimited_engine=1,
                quota_test_ops=1,
                used_test_ops=1,
                number_user=1,
                quota_floating_engine=1,
                used_floating_engine=1,
                can_create_offline_kse=True,
                can_create_offline_unlimited_kse=True,
                can_create_offline_re=True,
                can_create_offline_unlimited_engine=True,
                subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_unlimited_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_unlimited_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                subscribed=True,
                kse_paygo=True,
                kre_paygo=True,
                paygo_quota=1,
                domain="domain_example",
                subdomain_url="subdomain_url_example",
                strict_domain=True,
                logo_url="logo_url_example",
                saml_sso=True,
                kre_license=True,
                most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                account_id=1,
                test_ops_feature="KSE",
                platform_feature="KSE",
                tier="FREE",
                requested_user_verified=True,
            ),
            organization_id=1,
        ),
        timezone="timezone_example",
        status="ARCHIVE",
    ) # ProjectResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Project status. Returns the updated Project detail.
        api_response = api_instance.update_status(project_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectApi->update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource** | [**ProjectResource**](ProjectResource.md)|  |

### Return type

[**ProjectResource**](ProjectResource.md)

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

