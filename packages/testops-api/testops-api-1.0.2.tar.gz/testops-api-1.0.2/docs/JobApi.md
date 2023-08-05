# testops_api.JobApi

All URIs are relative to *http://localhost:8443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](JobApi.md#cancel) | **DELETE** /api/v1/jobs/{id} | Cancels a Job.
[**get14**](JobApi.md#get14) | **GET** /api/v1/jobs/{id} | Returns a Job detail.
[**get_job**](JobApi.md#get_job) | **GET** /api/v1/jobs/get-job | Returns the next queued Job of an Agent.
[**get_latest_jobs**](JobApi.md#get_latest_jobs) | **GET** /api/v1/organizations/{id}/latest-jobs | 
[**get_log**](JobApi.md#get_log) | **GET** /api/v1/jobs/{id}/get-log | Returns a Job&#39;s log.
[**get_running_jobs**](JobApi.md#get_running_jobs) | **GET** /api/v1/organizations/{id}/running-jobs | 
[**update_job**](JobApi.md#update_job) | **POST** /api/v1/jobs/update-job | Updates a Job detail. Returns the updated Job detail.


# **cancel**
> cancel(id)

Cancels a Job.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
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
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancels a Job.
        api_instance.cancel(id)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get14**
> JobResource get14(id)

Returns a Job detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
from testops_api.model.job_resource import JobResource
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
    api_instance = job_api.JobApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Job detail.
        api_response = api_instance.get14(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->get14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**JobResource**](JobResource.md)

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

# **get_job**
> JobResource get_job(uuid, team_id)

Returns the next queued Job of an Agent.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
from testops_api.model.job_resource import JobResource
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
    api_instance = job_api.JobApi(api_client)
    uuid = "uuid_example" # str | 
    team_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns the next queued Job of an Agent.
        api_response = api_instance.get_job(uuid, team_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **team_id** | **int**|  |

### Return type

[**JobResource**](JobResource.md)

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

# **get_latest_jobs**
> PageJobResource get_latest_jobs(id, pageable)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_job_resource import PageJobResource
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
    api_instance = job_api.JobApi(api_client)
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
        api_response = api_instance.get_latest_jobs(id, pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->get_latest_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **pageable** | **Pageable**|  |

### Return type

[**PageJobResource**](PageJobResource.md)

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

# **get_log**
> [BuildLog] get_log(id)

Returns a Job's log.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
from testops_api.model.build_log import BuildLog
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
    api_instance = job_api.JobApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Job's log.
        api_response = api_instance.get_log(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->get_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[BuildLog]**](BuildLog.md)

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

# **get_running_jobs**
> PageJobResource get_running_jobs(id, pageable)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_job_resource import PageJobResource
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
    api_instance = job_api.JobApi(api_client)
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
        api_response = api_instance.get_running_jobs(id, pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->get_running_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **pageable** | **Pageable**|  |

### Return type

[**PageJobResource**](PageJobResource.md)

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

# **update_job**
> JobResource update_job(job_resource)

Updates a Job detail. Returns the updated Job detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import job_api
from testops_api.model.job_resource import JobResource
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
    api_instance = job_api.JobApi(api_client)
    job_resource = JobResource(
        id=1,
        build_number=1,
        status="QUEUED",
        queued_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        test_project=TestProjectResource(
            id=1,
            name="name_example",
            description="description_example",
            default_test_project=True,
            upload_file_id=1,
            project_id=1,
            team_id=1,
            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            latest_job=JobResource(JobResource),
            upload_file_name="upload_file_name_example",
            type="KS",
            git_repository=GitRepositoryResource(
                id=1,
                test_project_id=1,
                name="name_example",
                repository="repository_example",
                branch="branch_example",
                username="username_example",
                password="password_example",
                access_key_id="access_key_id_example",
                secret_access_key="secret_access_key_example",
                project_id=1,
                team_id=1,
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                description="description_example",
                vcs_type="GITHUB",
                should_merge_test_results_for_new_script_repo=True,
            ),
            test_suite_collections=[
                TestSuiteCollectionResource(
                    id=1,
                    name="name_example",
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
                    test_suite_collection_configurations=[
                        TestSuiteCollectionConfigurationResource(
                            id=1,
                            profile_name="profile_name_example",
                            browser_type="CHROME",
                            run_enabled=True,
                            sort_order=1,
                            test_suite_entity="test_suite_entity_example",
                        ),
                    ],
                    url_id="url_id_example",
                ),
            ],
            dirty=True,
        ),
        execution=ExecutionResource(
            status="PASSED",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            duration=1,
            elapsed_duration=1,
            total_tests=1,
            total_passed_tests=1,
            total_failed_tests=1,
            total_error_tests=1,
            total_incomplete_tests=1,
            total_skipped_tests=1,
            total_diff_tests=1,
            total_diff_passed_tests=1,
            total_diff_failed_tests=1,
            total_diff_error_tests=1,
            total_diff_incomplete_tests=1,
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
                    users=[],
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
            build_id=1,
            order=1,
            execution_stage="RUNNING",
            web_url="web_url_example",
            test_suite_collections=[
                TestSuiteCollectionEntityResource(
                    id=1,
                    name="name_example",
                    project=ProjectResource(
                        id=1,
                        name="name_example",
                        team_id=1,
                        team=TeamResource(
                            id=1,
                            name="name_example",
                            role="OWNER",
                            users=[],
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
                    path="path_example",
                    url_id="url_id_example",
                ),
            ],
            execution_test_suite_resources=[
                ExecutionTestSuiteResource(
                    status="PASSED",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    duration=1,
                    elapsed_duration=1,
                    total_tests=1,
                    total_passed_tests=1,
                    total_failed_tests=1,
                    total_error_tests=1,
                    total_incomplete_tests=1,
                    total_skipped_tests=1,
                    total_diff_tests=1,
                    total_diff_passed_tests=1,
                    total_diff_failed_tests=1,
                    total_diff_error_tests=1,
                    total_diff_incomplete_tests=1,
                    id=1,
                    execution=ExecutionResource(ExecutionResource),
                    test_suite=TestSuiteResource(
                        id=1,
                        name="name_example",
                        path="path_example",
                        test_results=[
                            ExecutionTestResultResource(
                                id=1,
                                test_case=TestCaseResource(
                                    id=1,
                                    name="name_example",
                                    path="path_example",
                                    previous_status="PASSED",
                                    alias="alias_example",
                                    test_module_id=1,
                                    web_url="web_url_example",
                                    description="description_example",
                                    project=ProjectResource(
                                        id=1,
                                        name="name_example",
                                        team_id=1,
                                        team=TeamResource(
                                            id=1,
                                            name="name_example",
                                            role="OWNER",
                                            users=[],
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
                                    last_execution_test_case=ExecutionTestCaseResource(
                                        status="PASSED",
                                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        duration=1,
                                        elapsed_duration=1,
                                        total_tests=1,
                                        total_passed_tests=1,
                                        total_failed_tests=1,
                                        total_error_tests=1,
                                        total_incomplete_tests=1,
                                        total_skipped_tests=1,
                                        total_diff_tests=1,
                                        total_diff_passed_tests=1,
                                        total_diff_failed_tests=1,
                                        total_diff_error_tests=1,
                                        total_diff_incomplete_tests=1,
                                        execution_id=1,
                                        execution_order=1,
                                        test_case_id=1,
                                        project_id=1,
                                    ),
                                    external_issues=[
                                        ExternalIssueResource(
                                            id=1,
                                            issue_id="issue_id_example",
                                            summary="summary_example",
                                            status="status_example",
                                            issue_type_icon="issue_type_icon_example",
                                            issue_type_name="issue_type_name_example",
                                            url="url_example",
                                            feature_name="feature_name_example",
                                            test_cases=[
                                                TestCaseResource(TestCaseResource),
                                            ],
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
                                    type="TEST_CASE",
                                    average_duration=3.14,
                                    max_duration=1,
                                    min_duration=1,
                                    flakiness=3.14,
                                    platform_statistics={
                                        "key": TestCasePlatformStatisticsResource(
                                            total_tests=1,
                                            total_passed_tests=1,
                                            total_failed_tests=1,
                                            total_error_tests=1,
                                            total_incomplete_tests=1,
                                            total_skipped_tests=1,
                                            platform=PlatformResource(
                                                id=1,
                                                os_name="os_name_example",
                                                os_version="os_version_example",
                                                browser_name="browser_name_example",
                                                browser_version="browser_version_example",
                                                device_name="device_name_example",
                                                app_name="app_name_example",
                                            ),
                                            platform_id=1,
                                        ),
                                    },
                                    maintainer=UserResource(
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
                                            profiles=[],
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
                                            agent_download_urls={},
                                            proxy_tunnel_download_urls={},
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
                                        projects=[],
                                        teams=[],
                                        organizations=[],
                                        organization_feature=[],
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
                                    test_result_assertion=TestResultAssertionResource(
                                        execution_test_result_id=1,
                                        execution_test_result=ExecutionTestResultResource(ExecutionTestResultResource),
                                        total_assertion=1,
                                        passed_assertion=1,
                                        failed_assertion=1,
                                    ),
                                    updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    test_project=TestProjectResource(
                                        id=1,
                                        name="name_example",
                                        description="description_example",
                                        default_test_project=True,
                                        upload_file_id=1,
                                        project_id=1,
                                        team_id=1,
                                        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        latest_job=JobResource(JobResource),
                                        upload_file_name="upload_file_name_example",
                                        type="KS",
                                        git_repository=GitRepositoryResource(
                                            id=1,
                                            test_project_id=1,
                                            name="name_example",
                                            repository="repository_example",
                                            branch="branch_example",
                                            username="username_example",
                                            password="password_example",
                                            access_key_id="access_key_id_example",
                                            secret_access_key="secret_access_key_example",
                                            project_id=1,
                                            team_id=1,
                                            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                            updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                            description="description_example",
                                            vcs_type="GITHUB",
                                            should_merge_test_results_for_new_script_repo=True,
                                        ),
                                        test_suite_collections=[],
                                        dirty=True,
                                    ),
                                    number_of_executions=1,
                                    url_id="url_id_example",
                                ),
                                execution=ExecutionResource(ExecutionResource),
                                platform=PlatformResource(
                                    id=1,
                                    os_name="os_name_example",
                                    os_version="os_version_example",
                                    browser_name="browser_name_example",
                                    browser_version="browser_version_example",
                                    device_name="device_name_example",
                                    app_name="app_name_example",
                                ),
                                status="PASSED",
                                same_status_period=1,
                                error_details_id=1,
                                stdout_id=1,
                                description_id=1,
                                log_id=1,
                                attachments=[
                                    FileResource(
                                        id=1,
                                        upload_file_id=1,
                                        _self="_self_example",
                                        name="name_example",
                                        path="path_example",
                                        url="url_example",
                                        hash="hash_example",
                                        size=1,
                                        upload_url="upload_url_example",
                                        signed_url="signed_url_example",
                                        thumbnail_url="thumbnail_url_example",
                                    ),
                                ],
                                test_result_assertions_failed=[
                                    TestResultAssertionFailedResource(
                                        id=1,
                                        execution_test_result_id=1,
                                        execution_test_result_resource=ExecutionTestResultResource(ExecutionTestResultResource),
                                        stacktrace="stacktrace_example",
                                        message="message_example",
                                        log_time="log_time_example",
                                    ),
                                ],
                                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                duration=1,
                                same_failure_results=[
                                    ExecutionTestResultIdentifyResource(
                                        id=1,
                                        execution_id=1,
                                        url_id="url_id_example",
                                    ),
                                ],
                                test_suite=TestSuiteResource(TestSuiteResource),
                                execution_test_suite=ExecutionTestSuiteResource(ExecutionTestSuiteResource),
                                incidents=[
                                    IncidentResource(
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
                                    ),
                                ],
                                profile="profile_example",
                                has_comment=True,
                                error_message="error_message_example",
                                error_detail="error_detail_example",
                                web_url="web_url_example",
                                external_issues=[],
                                failed_test_result_category="APPLICATION",
                                total_test_object=1,
                                total_defects=1,
                                total_assertion=1,
                                passed_assertion=1,
                                failed_assertion=1,
                                retried=True,
                                last_retry_test_id=1,
                                current_retry=1,
                                original_status="PASSED",
                                last_changed_by=UserResource(
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
                                        profiles=[],
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
                                        agent_download_urls={},
                                        proxy_tunnel_download_urls={},
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
                                    projects=[],
                                    teams=[],
                                    organizations=[],
                                    organization_feature=[],
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
                                error_keyword="error_keyword_example",
                                status_edited=True,
                                url_id="url_id_example",
                            ),
                        ],
                        project=ProjectResource(
                            id=1,
                            name="name_example",
                            team_id=1,
                            team=TeamResource(
                                id=1,
                                name="name_example",
                                role="OWNER",
                                users=[],
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
                        alias="alias_example",
                        last_execution_test_suite=ExecutionTestSuiteResource(ExecutionTestSuiteResource),
                        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        test_cases=[],
                        test_project=TestProjectResource(
                            id=1,
                            name="name_example",
                            description="description_example",
                            default_test_project=True,
                            upload_file_id=1,
                            project_id=1,
                            team_id=1,
                            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            latest_job=JobResource(JobResource),
                            upload_file_name="upload_file_name_example",
                            type="KS",
                            git_repository=GitRepositoryResource(
                                id=1,
                                test_project_id=1,
                                name="name_example",
                                repository="repository_example",
                                branch="branch_example",
                                username="username_example",
                                password="password_example",
                                access_key_id="access_key_id_example",
                                secret_access_key="secret_access_key_example",
                                project_id=1,
                                team_id=1,
                                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                description="description_example",
                                vcs_type="GITHUB",
                                should_merge_test_results_for_new_script_repo=True,
                            ),
                            test_suite_collections=[],
                            dirty=True,
                        ),
                        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        user=UserResource(
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
                                profiles=[],
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
                                agent_download_urls={},
                                proxy_tunnel_download_urls={},
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
                            projects=[],
                            teams=[],
                            organizations=[],
                            organization_feature=[],
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
                        type="KATALON_STUDIO",
                        test_folder=TestFolderResource(
                            id=1,
                            name="name_example",
                            raw_path="raw_path_example",
                            test_project=TestProjectResource(
                                id=1,
                                name="name_example",
                                description="description_example",
                                default_test_project=True,
                                upload_file_id=1,
                                project_id=1,
                                team_id=1,
                                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                latest_job=JobResource(JobResource),
                                upload_file_name="upload_file_name_example",
                                type="KS",
                                git_repository=GitRepositoryResource(
                                    id=1,
                                    test_project_id=1,
                                    name="name_example",
                                    repository="repository_example",
                                    branch="branch_example",
                                    username="username_example",
                                    password="password_example",
                                    access_key_id="access_key_id_example",
                                    secret_access_key="secret_access_key_example",
                                    project_id=1,
                                    team_id=1,
                                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    description="description_example",
                                    vcs_type="GITHUB",
                                    should_merge_test_results_for_new_script_repo=True,
                                ),
                                test_suite_collections=[],
                                dirty=True,
                            ),
                            tree_path="tree_path_example",
                            parent_id=1,
                        ),
                        url_id="url_id_example",
                    ),
                    platform=PlatformResource(
                        id=1,
                        os_name="os_name_example",
                        os_version="os_version_example",
                        browser_name="browser_name_example",
                        browser_version="browser_version_example",
                        device_name="device_name_example",
                        app_name="app_name_example",
                    ),
                    execution_id=1,
                    profiles=[],
                    has_comment=True,
                    url_id="url_id_example",
                ),
            ],
            release=ReleaseResource(
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
                                users=[],
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
            ),
            build=BuildResource(
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
                        users=[],
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
                release=ReleaseResource(
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
                    builds=[],
                    release_status="NOT_READY",
                ),
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
            has_comment=True,
            user=UserResource(
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
                    profiles=[],
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
                    agent_download_urls={},
                    proxy_tunnel_download_urls={},
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
                projects=[],
                teams=[],
                organizations=[],
                organization_feature=[],
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
            session_id="session_id_example",
            build_label="build_label_example",
            build_url="build_url_example",
            type="KATALON",
            jobs=[
                JobResource(JobResource),
            ],
            use_test_cloud_tunnel=True,
            getk_eyes_execution=KEyesExecutionResource(
                id=1,
                status="RUNNING",
                execution=ExecutionResource(ExecutionResource),
                total_checkpoints=1,
                passed_checkpoints=1,
                failed_checkpoints=1,
                unresolved_checkpoints=1,
                unsaved=True,
                baseline_collection=BaselineCollectionResource(
                    id=1,
                    version=1,
                    baselines=[
                        BaselineResource(
                            id=1,
                            upload_file=UploadFileResource(
                                path="path_example",
                                file_name="file_name_example",
                                type="TSC_EXECUTION",
                                base64_content="base64_content_example",
                                file_handle_id=1,
                                thumbnail_id=1,
                            ),
                            screenshot_id=1,
                            execution=ExecutionResource(ExecutionResource),
                            screenshot=ScreenshotResource(
                                name="name_example",
                                width=3.14,
                                height=3.14,
                            ),
                            width=3.14,
                            height=3.14,
                            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            draft_ignoring_zones=[
                                IgnoringZoneResource(
                                    uuid="uuid_example",
                                    x=1,
                                    y=1,
                                    w=1,
                                    h=1,
                                    type="ALL",
                                ),
                            ],
                            ignoring_zones=[
                                IgnoringZoneResource(
                                    uuid="uuid_example",
                                    x=1,
                                    y=1,
                                    w=1,
                                    h=1,
                                    type="ALL",
                                ),
                            ],
                        ),
                    ],
                    number_of_baselines=1,
                    updated_by=UserResource(
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
                            profiles=[],
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
                            agent_download_urls={},
                            proxy_tunnel_download_urls={},
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
                        projects=[],
                        teams=[],
                        organizations=[],
                        organization_feature=[],
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
                    baseline_collection_group=BaselineCollectionGroupResource(
                        id=1,
                        name="name_example",
                        latest_version=BaselineCollectionResource(BaselineCollectionResource),
                        run_configurations=[
                            RunConfigurationResource(
                                id=1,
                                name="name_example",
                                command="command_example",
                                project_id=1,
                                team_id=1,
                                test_project_id=1,
                                release_id=1,
                                test_suite_collection_id=1,
                                test_suite_id=1,
                                execution_profile_id=1,
                                baseline_collection_group_order=1,
                                time_out=1,
                                kobiton_device_id="kobiton_device_id_example",
                                config_type="TSC",
                                test_project=TestProjectResource(
                                    id=1,
                                    name="name_example",
                                    description="description_example",
                                    default_test_project=True,
                                    upload_file_id=1,
                                    project_id=1,
                                    team_id=1,
                                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    latest_job=JobResource(JobResource),
                                    upload_file_name="upload_file_name_example",
                                    type="KS",
                                    git_repository=GitRepositoryResource(
                                        id=1,
                                        test_project_id=1,
                                        name="name_example",
                                        repository="repository_example",
                                        branch="branch_example",
                                        username="username_example",
                                        password="password_example",
                                        access_key_id="access_key_id_example",
                                        secret_access_key="secret_access_key_example",
                                        project_id=1,
                                        team_id=1,
                                        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        description="description_example",
                                        vcs_type="GITHUB",
                                        should_merge_test_results_for_new_script_repo=True,
                                    ),
                                    test_suite_collections=[],
                                    dirty=True,
                                ),
                                agents=[
                                    AgentResource(
                                        id=1,
                                        name="name_example",
                                        ip="ip_example",
                                        uuid="uuid_example",
                                        last_ping=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        os="os_example",
                                        team_id=1,
                                        hostname="hostname_example",
                                        active=True,
                                        threshold=1,
                                        num_executing_jobs=1,
                                        num_assigned_jobs=1,
                                        agent_version="agent_version_example",
                                        deleted=True,
                                    ),
                                ],
                                test_cloud_agents=[
                                    TestCloudAgentResource(
                                        id=1,
                                        name="name_example",
                                        os="os_example",
                                        os_version="os_version_example",
                                        browser="browser_example",
                                        browser_version="browser_version_example",
                                        device_name="device_name_example",
                                        app_id="app_id_example",
                                        app_group_id="app_group_id_example",
                                        app_name="app_name_example",
                                        device_id="device_id_example",
                                        num_executing_jobs=1,
                                        num_assigned_jobs=1,
                                        team_id=1,
                                        deleted=True,
                                        api_key="api_key_example",
                                        total_duration=1,
                                        headless=True,
                                        execution_type="CHROME",
                                    ),
                                ],
                                k8s_agents=[
                                    K8SAgentResource(
                                        id=1,
                                        name="name_example",
                                        certificate_authority="certificate_authority_example",
                                        url="url_example",
                                        namespace="namespace_example",
                                        username="username_example",
                                        password="password_example",
                                        token="token_example",
                                        cluster="cluster_example",
                                        region="region_example",
                                        access_key="access_key_example",
                                        private_access_key="private_access_key_example",
                                        team_id=1,
                                        api_key="api_key_example",
                                        authentication_type="BASIC_AUTH",
                                    ),
                                ],
                                circle_ci_agents=[
                                    CircleCIAgentResource(
                                        id=1,
                                        name="name_example",
                                        url="url_example",
                                        username="username_example",
                                        token="token_example",
                                        project="project_example",
                                        vcs_type="vcs_type_example",
                                        branch="branch_example",
                                        team_id=1,
                                        api_key="api_key_example",
                                    ),
                                ],
                                test_cloud_test_suite_collection_agents=[
                                    TestCloudTestSuiteCollectionAgentResource(
                                        test_suite_collection_configuration_id=1,
                                        test_cloud_agent=TestCloudAgentResource(
                                            id=1,
                                            name="name_example",
                                            os="os_example",
                                            os_version="os_version_example",
                                            browser="browser_example",
                                            browser_version="browser_version_example",
                                            device_name="device_name_example",
                                            app_id="app_id_example",
                                            app_group_id="app_group_id_example",
                                            app_name="app_name_example",
                                            device_id="device_id_example",
                                            num_executing_jobs=1,
                                            num_assigned_jobs=1,
                                            team_id=1,
                                            deleted=True,
                                            api_key="api_key_example",
                                            total_duration=1,
                                            headless=True,
                                            execution_type="CHROME",
                                        ),
                                        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    ),
                                ],
                                cloud_type="K8S",
                                latest_job=JobResource(JobResource),
                                generic_command="generic_command_example",
                                ks_version="ks_version_example",
                                ks_location="ks_location_example",
                                next_run_scheduler=SchedulerResource(
                                    id=1,
                                    name="name_example",
                                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    next_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                    active=True,
                                    interval=1,
                                    interval_unit="MINUTE",
                                    run_configuration_id=1,
                                    run_configuration=RunConfigurationResource(RunConfigurationResource),
                                    exceeded_limit_time=True,
                                ),
                                release=ReleaseResource(
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
                                    builds=[],
                                    release_status="NOT_READY",
                                ),
                                build=BuildResource(
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
                                            users=[],
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
                                    release=ReleaseResource(
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
                                        builds=[],
                                        release_status="NOT_READY",
                                    ),
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
                                execution_mode="SEQUENTIAL",
                                enabled_kobiton_integration=True,
                                enabled_test_cloud_tunnel=True,
                                trigger_mode="TESTOPS_SCHEDULER",
                                browser_type="CHROME",
                                xray_import_report_type="PUSH_MANUALLY",
                                external_test_plan_id="external_test_plan_id_example",
                                custom_field_options=[],
                                tags=[
                                    TagResource(
                                        id=1,
                                        name="name_example",
                                        project_id=1,
                                        organization_id=1,
                                    ),
                                ],
                            ),
                        ],
                        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        order=1,
                        last_run=KEyesExecutionResource(KEyesExecutionResource),
                    ),
                    unsaved=True,
                    default_method="PIXEL",
                    draft_default_method="PIXEL",
                    threshold=1,
                    draft_threshold=1,
                    create_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ),
            data_type="USER_DATA",
        ),
        agent=AgentResource(
            id=1,
            name="name_example",
            ip="ip_example",
            uuid="uuid_example",
            last_ping=dateutil_parser('1970-01-01T00:00:00.00Z'),
            os="os_example",
            team_id=1,
            hostname="hostname_example",
            active=True,
            threshold=1,
            num_executing_jobs=1,
            num_assigned_jobs=1,
            agent_version="agent_version_example",
            deleted=True,
        ),
        test_cloud_agent=TestCloudAgentResource(
            id=1,
            name="name_example",
            os="os_example",
            os_version="os_version_example",
            browser="browser_example",
            browser_version="browser_version_example",
            device_name="device_name_example",
            app_id="app_id_example",
            app_group_id="app_group_id_example",
            app_name="app_name_example",
            device_id="device_id_example",
            num_executing_jobs=1,
            num_assigned_jobs=1,
            team_id=1,
            deleted=True,
            api_key="api_key_example",
            total_duration=1,
            headless=True,
            execution_type="CHROME",
        ),
        k8s_agent=K8SAgentResource(
            id=1,
            name="name_example",
            certificate_authority="certificate_authority_example",
            url="url_example",
            namespace="namespace_example",
            username="username_example",
            password="password_example",
            token="token_example",
            cluster="cluster_example",
            region="region_example",
            access_key="access_key_example",
            private_access_key="private_access_key_example",
            team_id=1,
            api_key="api_key_example",
            authentication_type="BASIC_AUTH",
        ),
        circle_ci_agent=CircleCIAgentResource(
            id=1,
            name="name_example",
            url="url_example",
            username="username_example",
            token="token_example",
            project="project_example",
            vcs_type="vcs_type_example",
            branch="branch_example",
            team_id=1,
            api_key="api_key_example",
        ),
        run_configuration=RunConfigurationResource(
            id=1,
            name="name_example",
            command="command_example",
            project_id=1,
            team_id=1,
            test_project_id=1,
            release_id=1,
            test_suite_collection_id=1,
            test_suite_id=1,
            execution_profile_id=1,
            baseline_collection_group_order=1,
            time_out=1,
            kobiton_device_id="kobiton_device_id_example",
            config_type="TSC",
            test_project=TestProjectResource(
                id=1,
                name="name_example",
                description="description_example",
                default_test_project=True,
                upload_file_id=1,
                project_id=1,
                team_id=1,
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                latest_job=JobResource(JobResource),
                upload_file_name="upload_file_name_example",
                type="KS",
                git_repository=GitRepositoryResource(
                    id=1,
                    test_project_id=1,
                    name="name_example",
                    repository="repository_example",
                    branch="branch_example",
                    username="username_example",
                    password="password_example",
                    access_key_id="access_key_id_example",
                    secret_access_key="secret_access_key_example",
                    project_id=1,
                    team_id=1,
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    description="description_example",
                    vcs_type="GITHUB",
                    should_merge_test_results_for_new_script_repo=True,
                ),
                test_suite_collections=[],
                dirty=True,
            ),
            agents=[],
            test_cloud_agents=[],
            k8s_agents=[],
            circle_ci_agents=[],
            test_cloud_test_suite_collection_agents=[],
            cloud_type="K8S",
            latest_job=JobResource(JobResource),
            generic_command="generic_command_example",
            ks_version="ks_version_example",
            ks_location="ks_location_example",
            next_run_scheduler=SchedulerResource(
                id=1,
                name="name_example",
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                next_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                active=True,
                interval=1,
                interval_unit="MINUTE",
                run_configuration_id=1,
                run_configuration=RunConfigurationResource(RunConfigurationResource),
                exceeded_limit_time=True,
            ),
            release=ReleaseResource(
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
                builds=[],
                release_status="NOT_READY",
            ),
            build=BuildResource(
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
                        users=[],
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
                release=ReleaseResource(
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
                    builds=[],
                    release_status="NOT_READY",
                ),
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
            execution_mode="SEQUENTIAL",
            enabled_kobiton_integration=True,
            enabled_test_cloud_tunnel=True,
            trigger_mode="TESTOPS_SCHEDULER",
            browser_type="CHROME",
            xray_import_report_type="PUSH_MANUALLY",
            external_test_plan_id="external_test_plan_id_example",
            custom_field_options=[],
            tags=[],
        ),
        order=1,
        parameter=TriggerBuildParameter(
            download_url="download_url_example",
            command="command_example",
            environment_variables=[
                EnvironmentVariable(
                    name="name_example",
                    value="value_example",
                ),
            ],
            session_id="session_id_example",
            ks_version="ks_version_example",
            ks_location="ks_location_example",
            config_type="TSC",
            type="KS",
            git_repository_resource=GitRepositoryResource(
                id=1,
                test_project_id=1,
                name="name_example",
                repository="repository_example",
                branch="branch_example",
                username="username_example",
                password="password_example",
                access_key_id="access_key_id_example",
                secret_access_key="secret_access_key_example",
                project_id=1,
                team_id=1,
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                description="description_example",
                vcs_type="GITHUB",
                should_merge_test_results_for_new_script_repo=True,
            ),
            test_ops_download_url="test_ops_download_url_example",
            extra_files=[
                KSFile(
                    content_url="content_url_example",
                    path="path_example",
                    write_mode="OVERRIDE",
                ),
            ],
            organization_id=1,
        ),
        trigger_by="MANUAL",
        duration=1,
        trigger_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        user=UserResource(
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
                profiles=[],
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
                agent_download_urls={},
                proxy_tunnel_download_urls={},
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
            projects=[],
            teams=[],
            organizations=[],
            organization_feature=[],
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
        scheduler=SchedulerResource(
            id=1,
            name="name_example",
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            next_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            active=True,
            interval=1,
            interval_unit="MINUTE",
            run_configuration_id=1,
            run_configuration=RunConfigurationResource(
                id=1,
                name="name_example",
                command="command_example",
                project_id=1,
                team_id=1,
                test_project_id=1,
                release_id=1,
                test_suite_collection_id=1,
                test_suite_id=1,
                execution_profile_id=1,
                baseline_collection_group_order=1,
                time_out=1,
                kobiton_device_id="kobiton_device_id_example",
                config_type="TSC",
                test_project=TestProjectResource(
                    id=1,
                    name="name_example",
                    description="description_example",
                    default_test_project=True,
                    upload_file_id=1,
                    project_id=1,
                    team_id=1,
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    latest_job=JobResource(JobResource),
                    upload_file_name="upload_file_name_example",
                    type="KS",
                    git_repository=GitRepositoryResource(
                        id=1,
                        test_project_id=1,
                        name="name_example",
                        repository="repository_example",
                        branch="branch_example",
                        username="username_example",
                        password="password_example",
                        access_key_id="access_key_id_example",
                        secret_access_key="secret_access_key_example",
                        project_id=1,
                        team_id=1,
                        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        description="description_example",
                        vcs_type="GITHUB",
                        should_merge_test_results_for_new_script_repo=True,
                    ),
                    test_suite_collections=[],
                    dirty=True,
                ),
                agents=[],
                test_cloud_agents=[],
                k8s_agents=[],
                circle_ci_agents=[],
                test_cloud_test_suite_collection_agents=[],
                cloud_type="K8S",
                latest_job=JobResource(JobResource),
                generic_command="generic_command_example",
                ks_version="ks_version_example",
                ks_location="ks_location_example",
                next_run_scheduler=SchedulerResource(SchedulerResource),
                release=ReleaseResource(
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
                    builds=[],
                    release_status="NOT_READY",
                ),
                build=BuildResource(
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
                            users=[],
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
                    release=ReleaseResource(
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
                        builds=[],
                        release_status="NOT_READY",
                    ),
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
                execution_mode="SEQUENTIAL",
                enabled_kobiton_integration=True,
                enabled_test_cloud_tunnel=True,
                trigger_mode="TESTOPS_SCHEDULER",
                browser_type="CHROME",
                xray_import_report_type="PUSH_MANUALLY",
                external_test_plan_id="external_test_plan_id_example",
                custom_field_options=[],
                tags=[],
            ),
            exceeded_limit_time=True,
        ),
        project=ProjectResource(
            id=1,
            name="name_example",
            team_id=1,
            team=TeamResource(
                id=1,
                name="name_example",
                role="OWNER",
                users=[],
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
        process_id=1,
        node_status="PENDING_CANCELED",
        run_configuration_id=1,
    ) # JobResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Job detail. Returns the updated Job detail.
        api_response = api_instance.update_job(job_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling JobApi->update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_resource** | [**JobResource**](JobResource.md)|  |

### Return type

[**JobResource**](JobResource.md)

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

