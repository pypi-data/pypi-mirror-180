# testops_api.TeamApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user_team**](TeamApi.md#assign_user_team) | **POST** /api/v1/users/add | Adds users to a Team. Returns the added User detail.
[**create2**](TeamApi.md#create2) | **POST** /api/v1/teams | Creates a new Team. Returns the created Team detail.
[**delete2**](TeamApi.md#delete2) | **DELETE** /api/v1/teams/{id} | Delete a Team. Returns the delete Team detail.
[**get8**](TeamApi.md#get8) | **GET** /api/v1/teams/{id} | Returns a Team detail.
[**list**](TeamApi.md#list) | **GET** /api/v1/teams | Returns all Teams of the current User.
[**remove_user**](TeamApi.md#remove_user) | **DELETE** /api/v1/users/remove | Removes a User from a Team. Returns the removed User detail.
[**update2**](TeamApi.md#update2) | **PUT** /api/v1/teams | Updates a Team detail. Returns the updated Team detail.
[**update_user_team**](TeamApi.md#update_user_team) | **PUT** /api/v1/permission/team/user | Updates the role of a User in a Team. Returns the updated detail.


# **assign_user_team**
> [UserResource] assign_user_team(team_id, new_user_ids)

Adds users to a Team. Returns the added User detail.

The user issuing this request must be the Admin of the team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.user_resource import UserResource
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
    api_instance = team_api.TeamApi(api_client)
    team_id = 1 # int | 
    new_user_ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Adds users to a Team. Returns the added User detail.
        api_response = api_instance.assign_user_team(team_id, new_user_ids)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->assign_user_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  |
 **new_user_ids** | **[int]**|  |

### Return type

[**[UserResource]**](UserResource.md)

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

# **create2**
> TeamResource create2(team_resource)

Creates a new Team. Returns the created Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    team_resource = TeamResource(
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
                    ProjectResource(
                        id=1,
                        name="name_example",
                        team_id=1,
                        team=TeamResource(TeamResource),
                        timezone="timezone_example",
                        status="ARCHIVE",
                    ),
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
    ) # TeamResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Team. Returns the created Team detail.
        api_response = api_instance.create2(team_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->create2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_resource** | [**TeamResource**](TeamResource.md)|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **delete2**
> TeamResource delete2(id)

Delete a Team. Returns the delete Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Team. Returns the delete Team detail.
        api_response = api_instance.delete2(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **get8**
> TeamResource get8(id)

Returns a Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Team detail.
        api_response = api_instance.get8(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->get8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **list**
> PageTeamResource list(pageable)

Returns all Teams of the current User.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_team_resource import PageTeamResource
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
    api_instance = team_api.TeamApi(api_client)
    pageable = Pageable(
        page=0,
        size=1,
        sort=[
            "sort_example",
        ],
    ) # Pageable | 

    # example passing only required values which don't have defaults set
    try:
        # Returns all Teams of the current User.
        api_response = api_instance.list(pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | **Pageable**|  |

### Return type

[**PageTeamResource**](PageTeamResource.md)

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

# **remove_user**
> UserResource remove_user(team_id, user_id)

Removes a User from a Team. Returns the removed User detail.

The user issuing this request must be the Admin of the team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.user_resource import UserResource
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
    api_instance = team_api.TeamApi(api_client)
    team_id = 1 # int | 
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Removes a User from a Team. Returns the removed User detail.
        api_response = api_instance.remove_user(team_id, user_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  |
 **user_id** | **int**|  |

### Return type

[**UserResource**](UserResource.md)

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

# **update2**
> TeamResource update2(team_resource)

Updates a Team detail. Returns the updated Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    team_resource = TeamResource(
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
                    ProjectResource(
                        id=1,
                        name="name_example",
                        team_id=1,
                        team=TeamResource(TeamResource),
                        timezone="timezone_example",
                        status="ARCHIVE",
                    ),
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
    ) # TeamResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Team detail. Returns the updated Team detail.
        api_response = api_instance.update2(team_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_resource** | [**TeamResource**](TeamResource.md)|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **update_user_team**
> UserTeamResource update_user_team(user_team_resource)

Updates the role of a User in a Team. Returns the updated detail.

The user issuing this request must be the Admin of the team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.user_team_resource import UserTeamResource
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
    api_instance = team_api.TeamApi(api_client)
    user_team_resource = UserTeamResource(
        id=1,
        user_id=1,
        team_id=1,
        role="OWNER",
    ) # UserTeamResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the role of a User in a Team. Returns the updated detail.
        api_response = api_instance.update_user_team(user_team_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->update_user_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_team_resource** | [**UserTeamResource**](UserTeamResource.md)|  |

### Return type

[**UserTeamResource**](UserTeamResource.md)

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

