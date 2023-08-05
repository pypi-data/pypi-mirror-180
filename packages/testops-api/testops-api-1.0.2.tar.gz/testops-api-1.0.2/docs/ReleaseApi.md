# testops_api.ReleaseApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_release**](ReleaseApi.md#active_release) | **POST** /api/v1/releases/{id}/active | Open or close a Release. Returns the updated Release detail.
[**create_or_update1**](ReleaseApi.md#create_or_update1) | **POST** /api/v1/releases | Creates a Release. Returns the Release details.
[**delete4**](ReleaseApi.md#delete4) | **DELETE** /api/v1/releases/{id} | Deletes a Release. Returns the Release details.
[**link_release**](ReleaseApi.md#link_release) | **POST** /api/v1/run-configurations/{id}/link-release | Link an Run Configuration to a Release. Returns the updated Run Configuration detail.
[**link_release1**](ReleaseApi.md#link_release1) | **POST** /api/v1/executions/{id}/link-release | Link an Execution to a Release. Returns the updated Execution detail.
[**unlink_release**](ReleaseApi.md#unlink_release) | **POST** /api/v1/run-configurations/{id}/unlink-release | Unlink an Run Configuration from a Release or a Build. Returns the updated Run Configuration detail.
[**unlink_release_and_build**](ReleaseApi.md#unlink_release_and_build) | **POST** /api/v1/executions/{id}/unlink-release | Unlink an Execution to a Release and Build. Returns the updated Execution detail.
[**update3**](ReleaseApi.md#update3) | **PUT** /api/v1/releases | Updates a Release. Returns the Release details.


# **active_release**
> ReleaseResource active_release(id, closed)

Open or close a Release. Returns the updated Release detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 
    closed = True # bool | 

    # example passing only required values which don't have defaults set
    try:
        # Open or close a Release. Returns the updated Release detail.
        api_response = api_instance.active_release(id, closed)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->active_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **closed** | **bool**|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

# **create_or_update1**
> ReleaseResource create_or_update1(release_resource)

Creates a Release. Returns the Release details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    release_resource = ReleaseResource(
        id=1,
        name="name_example",
        start_time=dateutil_parser('1970-01-01').date(),
        end_time=dateutil_parser('1970-01-01').date(),
        description="description_example",
        project_id=1,
        closed=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        external_release=ExternalReleaseResource(
            id=1,
            release_id="release_id_example",
            description="description_example",
            name="name_example",
            archived=True,
            released=True,
            project_id="project_id_example",
            external_project=ExternalProjectResource(
                id=1,
                external_project_id="external_project_id_example",
                external_project_key="external_project_key_example",
                name="name_example",
            ),
            web_url="web_url_example",
            jira_release_status="RELEASED",
            start_date=dateutil_parser('1970-01-01').date(),
            release_date=dateutil_parser('1970-01-01').date(),
        ),
        release_statistics=ReleaseStatisticsResource(
            id=1,
            release=ReleaseResource(ReleaseResource),
            total_passed=1,
            total_failed=1,
            total_execution=1,
            total_defect=1,
            total_duration=1,
        ),
        builds=[
            BuildResource(
                id=1,
                project_id=1,
                project=ProjectResource(
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
                ),
                release_id=1,
                release=ReleaseResource(ReleaseResource),
                build_statistics=BuildStatisticsResource(
                    id=1,
                    build=BuildResource(BuildResource),
                    total_execution=1,
                    total_passed=1,
                    total_failed=1,
                ),
                name="name_example",
                description="description_example",
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        release_status="NOT_READY",
    ) # ReleaseResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a Release. Returns the Release details.
        api_response = api_instance.create_or_update1(release_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->create_or_update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

# **delete4**
> ReleaseResource delete4(id)

Deletes a Release. Returns the Release details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Release. Returns the Release details.
        api_response = api_instance.delete4(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->delete4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

# **link_release**
> RunConfigurationResource link_release(id, project_id, release_id)

Link an Run Configuration to a Release. Returns the updated Run Configuration detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.run_configuration_resource import RunConfigurationResource
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 
    project_id = 1 # int | 
    release_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Run Configuration to a Release. Returns the updated Run Configuration detail.
        api_response = api_instance.link_release(id, project_id, release_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->link_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **project_id** | **int**|  |
 **release_id** | **int**|  |

### Return type

[**RunConfigurationResource**](RunConfigurationResource.md)

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
from testops_api.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 
    project_id = 1 # int | 
    release_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Execution to a Release. Returns the updated Execution detail.
        api_response = api_instance.link_release1(id, project_id, release_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->link_release1: %s\n" % e)
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

# **unlink_release**
> RunConfigurationResource unlink_release(id)

Unlink an Run Configuration from a Release or a Build. Returns the updated Run Configuration detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.run_configuration_resource import RunConfigurationResource
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink an Run Configuration from a Release or a Build. Returns the updated Run Configuration detail.
        api_response = api_instance.unlink_release(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->unlink_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**RunConfigurationResource**](RunConfigurationResource.md)

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
from testops_api.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink an Execution to a Release and Build. Returns the updated Execution detail.
        api_response = api_instance.unlink_release_and_build(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->unlink_release_and_build: %s\n" % e)
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

# **update3**
> ReleaseResource update3(release_resource)

Updates a Release. Returns the Release details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    release_resource = ReleaseResource(
        id=1,
        name="name_example",
        start_time=dateutil_parser('1970-01-01').date(),
        end_time=dateutil_parser('1970-01-01').date(),
        description="description_example",
        project_id=1,
        closed=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        external_release=ExternalReleaseResource(
            id=1,
            release_id="release_id_example",
            description="description_example",
            name="name_example",
            archived=True,
            released=True,
            project_id="project_id_example",
            external_project=ExternalProjectResource(
                id=1,
                external_project_id="external_project_id_example",
                external_project_key="external_project_key_example",
                name="name_example",
            ),
            web_url="web_url_example",
            jira_release_status="RELEASED",
            start_date=dateutil_parser('1970-01-01').date(),
            release_date=dateutil_parser('1970-01-01').date(),
        ),
        release_statistics=ReleaseStatisticsResource(
            id=1,
            release=ReleaseResource(ReleaseResource),
            total_passed=1,
            total_failed=1,
            total_execution=1,
            total_defect=1,
            total_duration=1,
        ),
        builds=[
            BuildResource(
                id=1,
                project_id=1,
                project=ProjectResource(
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
                ),
                release_id=1,
                release=ReleaseResource(ReleaseResource),
                build_statistics=BuildStatisticsResource(
                    id=1,
                    build=BuildResource(BuildResource),
                    total_execution=1,
                    total_passed=1,
                    total_failed=1,
                ),
                name="name_example",
                description="description_example",
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        release_status="NOT_READY",
    ) # ReleaseResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Release. Returns the Release details.
        api_response = api_instance.update3(release_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->update3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

