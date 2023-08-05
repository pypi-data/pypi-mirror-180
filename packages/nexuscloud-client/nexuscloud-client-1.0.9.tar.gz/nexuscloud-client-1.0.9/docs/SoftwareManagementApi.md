# nexuscloud_client.SoftwareManagementApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_software_management_affected_endpoints_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_affected_endpoints_get) | **GET** /nexus/insights/api/v1/softwareManagement/affectedEndpoints | Get affected endpoints after upgrade
[**nexus_insights_api_v1_software_management_customize_groups_post**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_customize_groups_post) | **POST** /nexus/insights/api/v1/softwareManagement/customizeGroups | Post customized groups
[**nexus_insights_api_v1_software_management_forecast_cleared_advisories_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_forecast_cleared_advisories_get) | **GET** /nexus/insights/api/v1/softwareManagement/forecastClearedAdvisories | Get forecast cleared advisories
[**nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get) | **GET** /nexus/insights/api/v1/softwareManagement/forecastClearedAnomalies | Get forecast cleared bug anomalies
[**nexus_insights_api_v1_software_management_postvalidation_details_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_postvalidation_details_get) | **GET** /nexus/insights/api/v1/softwareManagement/postvalidationDetails | Get post-upgrade check results
[**nexus_insights_api_v1_software_management_prevalidations_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_prevalidations_get) | **GET** /nexus/insights/api/v1/softwareManagement/prevalidations | Get pre-upgrade check results
[**nexus_insights_api_v1_software_management_recommended_plan_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_recommended_plan_get) | **GET** /nexus/insights/api/v1/softwareManagement/recommendedPlan | Get update plan
[**nexus_insights_api_v1_software_management_recommended_plan_post**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_recommended_plan_post) | **POST** /nexus/insights/api/v1/softwareManagement/recommendedPlan | Cancel Software update
[**nexus_insights_api_v1_software_management_sites_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_sites_get) | **GET** /nexus/insights/api/v1/softwareManagement/sites | Get upgrade status
[**nexus_insights_api_v1_software_management_sites_post**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_sites_post) | **POST** /nexus/insights/api/v1/softwareManagement/sites | Software update
[**nexus_insights_api_v1_software_management_upgrade_post**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_upgrade_post) | **POST** /nexus/insights/api/v1/softwareManagement/upgrade | Software update
[**nexus_insights_api_v1_software_management_versions_get**](SoftwareManagementApi.md#nexus_insights_api_v1_software_management_versions_get) | **GET** /nexus/insights/api/v1/softwareManagement/versions | Get software versions


# **nexus_insights_api_v1_software_management_affected_endpoints_get**
> NexusInsightsApiV1SoftwareManagementAffectedEndpointsGet200Response nexus_insights_api_v1_software_management_affected_endpoints_get(config_id, instance_id)

Get affected endpoints after upgrade

Get affected endpoints after an upgrade

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_affected_endpoints_get200_response import NexusInsightsApiV1SoftwareManagementAffectedEndpointsGet200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    config_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | config id for a previous run of pre-validation check
    instance_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | instance id for a previous run of pre-validation check

    # example passing only required values which don't have defaults set
    try:
        # Get affected endpoints after upgrade
        api_response = api_instance.nexus_insights_api_v1_software_management_affected_endpoints_get(config_id, instance_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_affected_endpoints_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| config id for a previous run of pre-validation check |
 **instance_id** | **str**| instance id for a previous run of pre-validation check |

### Return type

[**NexusInsightsApiV1SoftwareManagementAffectedEndpointsGet200Response**](NexusInsightsApiV1SoftwareManagementAffectedEndpointsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_customize_groups_post**
> NexusInsightsApiV1SoftwareManagementCustomizeGroupsPost200Response nexus_insights_api_v1_software_management_customize_groups_post()

Post customized groups

Post customized groups for a site(s)

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_customize_groups_post200_response import NexusInsightsApiV1SoftwareManagementCustomizeGroupsPost200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_customize_groups_post_request_inner import NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInner
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    nexus_insights_api_v1_software_management_customize_groups_post_request_inner = [
        NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInner(
            config_id="config_id_example",
            groups=[
                NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInnerGroupsInner(
                    devices=[
                        NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInnerGroupsInnerDevicesInner(
                            model="N9K-C9336C-FX",
                            node_id="112",
                            node_name="ifav96-leaf1",
                            node_role="leaf",
                            pod_id="1",
                            serial="FDO22041MU1",
                            status="NOT_COMPLETED",
                            version="16.0(0.166)",
                        ),
                    ],
                    group_name="group_name_example",
                    group_order=1,
                    instance_id="instance_id_example",
                    job_name="job_name_example",
                    post_update_status="COMPLETED",
                    pre_update_status="NOT_STARTED",
                    target_version="6.0(0.216)",
                    tenant_id="6266d9dc7564612d30fc16cc",
                    user_name="user_name_example",
                    validation_type="SITE",
                    vendor="CISCO_ACI",
                ),
            ],
        ),
    ] # [NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInner] | Parameters for software update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Post customized groups
        api_response = api_instance.nexus_insights_api_v1_software_management_customize_groups_post(nexus_insights_api_v1_software_management_customize_groups_post_request_inner=nexus_insights_api_v1_software_management_customize_groups_post_request_inner)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_customize_groups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_software_management_customize_groups_post_request_inner** | [**[NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInner]**](NexusInsightsApiV1SoftwareManagementCustomizeGroupsPostRequestInner.md)| Parameters for software update | [optional]

### Return type

[**NexusInsightsApiV1SoftwareManagementCustomizeGroupsPost200Response**](NexusInsightsApiV1SoftwareManagementCustomizeGroupsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_forecast_cleared_advisories_get**
> NexusInsightsApiV1SoftwareManagementForecastClearedAdvisoriesGet200Response nexus_insights_api_v1_software_management_forecast_cleared_advisories_get(instance_id)

Get forecast cleared advisories

Get the list of advisories that will be cleared on upgrade 

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_forecast_cleared_advisories_get200_response import NexusInsightsApiV1SoftwareManagementForecastClearedAdvisoriesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    instance_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d_Pod1Controllers1" # str | Instance id for the group in a site

    # example passing only required values which don't have defaults set
    try:
        # Get forecast cleared advisories
        api_response = api_instance.nexus_insights_api_v1_software_management_forecast_cleared_advisories_get(instance_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_forecast_cleared_advisories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance id for the group in a site |

### Return type

[**NexusInsightsApiV1SoftwareManagementForecastClearedAdvisoriesGet200Response**](NexusInsightsApiV1SoftwareManagementForecastClearedAdvisoriesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get**
> NexusInsightsApiV1SoftwareManagementForecastClearedAnomaliesGet200Response nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get(instance_id)

Get forecast cleared bug anomalies

Get the list of bug anomalies that will be cleared on upgrade 

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get200_response import NexusInsightsApiV1SoftwareManagementForecastClearedAnomaliesGet200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    instance_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d_Pod1Controllers1" # str | Instance id for the group in a site

    # example passing only required values which don't have defaults set
    try:
        # Get forecast cleared bug anomalies
        api_response = api_instance.nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get(instance_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_forecast_cleared_anomalies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance id for the group in a site |

### Return type

[**NexusInsightsApiV1SoftwareManagementForecastClearedAnomaliesGet200Response**](NexusInsightsApiV1SoftwareManagementForecastClearedAnomaliesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_postvalidation_details_get**
> NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200Response nexus_insights_api_v1_software_management_postvalidation_details_get(config_id, instance_id)

Get post-upgrade check results

Get detailed results for the validation checks after an upgrade

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_postvalidation_details_get200_response import NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    config_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | config id for a previous run of pre-validation check
    instance_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | instance id for a previous run of pre-validation check

    # example passing only required values which don't have defaults set
    try:
        # Get post-upgrade check results
        api_response = api_instance.nexus_insights_api_v1_software_management_postvalidation_details_get(config_id, instance_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_postvalidation_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| config id for a previous run of pre-validation check |
 **instance_id** | **str**| instance id for a previous run of pre-validation check |

### Return type

[**NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200Response**](NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**500** | Internal Server Error, The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**502** | Bad Gateway, Site is down. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_prevalidations_get**
> NexusInsightsApiV1SoftwareManagementPrevalidationsGet200Response nexus_insights_api_v1_software_management_prevalidations_get(config_id)

Get pre-upgrade check results

Get detailed results for the validation checks before an upgrade

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_prevalidations_get200_response import NexusInsightsApiV1SoftwareManagementPrevalidationsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    config_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | config id for a previous run of pre-validation check
    instance_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | instance id for a previous run of pre-validation check (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get pre-upgrade check results
        api_response = api_instance.nexus_insights_api_v1_software_management_prevalidations_get(config_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_prevalidations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get pre-upgrade check results
        api_response = api_instance.nexus_insights_api_v1_software_management_prevalidations_get(config_id, instance_id=instance_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_prevalidations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| config id for a previous run of pre-validation check |
 **instance_id** | **str**| instance id for a previous run of pre-validation check | [optional]

### Return type

[**NexusInsightsApiV1SoftwareManagementPrevalidationsGet200Response**](NexusInsightsApiV1SoftwareManagementPrevalidationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_recommended_plan_get**
> NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response nexus_insights_api_v1_software_management_recommended_plan_get(config_id)

Get update plan

Get detailed status of an update in progress

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_recommended_plan_get200_response import NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    config_id = "e0156700-bb61-4e88-9ff3-25ed1427f01d" # str | Instance id for the group in a site

    # example passing only required values which don't have defaults set
    try:
        # Get update plan
        api_response = api_instance.nexus_insights_api_v1_software_management_recommended_plan_get(config_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_recommended_plan_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| Instance id for the group in a site |

### Return type

[**NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response**](NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_recommended_plan_post**
> NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response1 nexus_insights_api_v1_software_management_recommended_plan_post()

Cancel Software update

Cancel software update for site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_recommended_plan_get_request_inner import NexusInsightsApiV1SoftwareManagementRecommendedPlanGetRequestInner
from nexuscloud_client.model.nexus_insights_api_v1_software_management_recommended_plan_get200_response1 import NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response1
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    nexus_insights_api_v1_software_management_recommended_plan_get_request_inner = [
        NexusInsightsApiV1SoftwareManagementRecommendedPlanGetRequestInner(
            site_name="ni-apic-sjc18",
        ),
    ] # [NexusInsightsApiV1SoftwareManagementRecommendedPlanGetRequestInner] | Parameters for cancelling software update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel Software update
        api_response = api_instance.nexus_insights_api_v1_software_management_recommended_plan_post(nexus_insights_api_v1_software_management_recommended_plan_get_request_inner=nexus_insights_api_v1_software_management_recommended_plan_get_request_inner)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_recommended_plan_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_software_management_recommended_plan_get_request_inner** | [**[NexusInsightsApiV1SoftwareManagementRecommendedPlanGetRequestInner]**](NexusInsightsApiV1SoftwareManagementRecommendedPlanGetRequestInner.md)| Parameters for cancelling software update | [optional]

### Return type

[**NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response1**](NexusInsightsApiV1SoftwareManagementRecommendedPlanGet200Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**401** | The server could not verify that you are authorized to access the URL requested. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_sites_get**
> NexusInsightsApiV1SoftwareManagementSitesGet200Response nexus_insights_api_v1_software_management_sites_get()

Get upgrade status

Get status of upgrades in progress

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_sites_get200_response import NexusInsightsApiV1SoftwareManagementSitesGet200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    site_group_name = "CISCO_ACI" # str | Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName (optional)
    site_name = "5.2(3e)" # str | Name of the fabric - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    offset = 1 # int | Pagination index into response. (optional)
    count = 10 # int | Limit the number of records in the response (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get upgrade status
        api_response = api_instance.nexus_insights_api_v1_software_management_sites_get(site_group_name=site_group_name, site_name=site_name, offset=offset, count=count)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_sites_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | [optional]
 **site_name** | **str**| Name of the fabric - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **offset** | **int**| Pagination index into response. | [optional]
 **count** | **int**| Limit the number of records in the response | [optional]

### Return type

[**NexusInsightsApiV1SoftwareManagementSitesGet200Response**](NexusInsightsApiV1SoftwareManagementSitesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_sites_post**
> NexusInsightsApiV1SoftwareManagementSitesGet200Response1 nexus_insights_api_v1_software_management_sites_post()

Software update

Start software update for site(s)

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_sites_get_request_inner import NexusInsightsApiV1SoftwareManagementSitesGetRequestInner
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_sites_get200_response1 import NexusInsightsApiV1SoftwareManagementSitesGet200Response1
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    nexus_insights_api_v1_software_management_sites_get_request_inner = [
        NexusInsightsApiV1SoftwareManagementSitesGetRequestInner(
            analyze=True,
            prepare=True,
            site_group_name="e0156700-bb61-4e88-9ff3-25ed1427f01d",
            site_name="ni-apic-sjc18",
            source_version="5.1(1e)",
            target_version="5.2(3e)",
            vendor="CISCO_ACI",
        ),
    ] # [NexusInsightsApiV1SoftwareManagementSitesGetRequestInner] | Parameters for software update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Software update
        api_response = api_instance.nexus_insights_api_v1_software_management_sites_post(nexus_insights_api_v1_software_management_sites_get_request_inner=nexus_insights_api_v1_software_management_sites_get_request_inner)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_sites_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_software_management_sites_get_request_inner** | [**[NexusInsightsApiV1SoftwareManagementSitesGetRequestInner]**](NexusInsightsApiV1SoftwareManagementSitesGetRequestInner.md)| Parameters for software update | [optional]

### Return type

[**NexusInsightsApiV1SoftwareManagementSitesGet200Response1**](NexusInsightsApiV1SoftwareManagementSitesGet200Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**401** | The server could not verify that you are authorized to access the URL requested. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_upgrade_post**
> NexusInsightsApiV1SoftwareManagementUpgradePost200Response nexus_insights_api_v1_software_management_upgrade_post()

Software update

Start software update install for site(s)

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_software_management_upgrade_post500_response import NexusInsightsApiV1SoftwareManagementUpgradePost500Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_upgrade_post_request import NexusInsightsApiV1SoftwareManagementUpgradePostRequest
from nexuscloud_client.model.nexus_insights_api_v1_software_management_upgrade_post200_response import NexusInsightsApiV1SoftwareManagementUpgradePost200Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_upgrade_post502_response import NexusInsightsApiV1SoftwareManagementUpgradePost502Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_upgrade_post400_response import NexusInsightsApiV1SoftwareManagementUpgradePost400Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    nexus_insights_api_v1_software_management_upgrade_post_request = NexusInsightsApiV1SoftwareManagementUpgradePostRequest(
        config_id="e0156700-bb61-4e88-9ff3-25ed1427f01d",
        target_version="5.2(3e)",
        vendor="CISCO_ACI",
    ) # NexusInsightsApiV1SoftwareManagementUpgradePostRequest | Parameters for software update (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Software update
        api_response = api_instance.nexus_insights_api_v1_software_management_upgrade_post(nexus_insights_api_v1_software_management_upgrade_post_request=nexus_insights_api_v1_software_management_upgrade_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_upgrade_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_software_management_upgrade_post_request** | [**NexusInsightsApiV1SoftwareManagementUpgradePostRequest**](NexusInsightsApiV1SoftwareManagementUpgradePostRequest.md)| Parameters for software update | [optional]

### Return type

[**NexusInsightsApiV1SoftwareManagementUpgradePost200Response**](NexusInsightsApiV1SoftwareManagementUpgradePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**500** | Internal Server Error, The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**502** | Bad Gateway, Site is down. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_software_management_versions_get**
> NexusInsightsApiV1SoftwareManagementVersionsGet200Response nexus_insights_api_v1_software_management_versions_get(vendor)

Get software versions

Get software versions, release-notes URL and their recommended or latest tag

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import software_management_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_software_management_versions_get200_response import NexusInsightsApiV1SoftwareManagementVersionsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = software_management_api.SoftwareManagementApi(api_client)
    vendor = "CISCO_ACI" # str | vendor
    minimum_version = "5.2(3e)" # str | Exclude versions that are higher than the minimum version specified (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get software versions
        api_response = api_instance.nexus_insights_api_v1_software_management_versions_get(vendor)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_versions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get software versions
        api_response = api_instance.nexus_insights_api_v1_software_management_versions_get(vendor, minimum_version=minimum_version)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SoftwareManagementApi->nexus_insights_api_v1_software_management_versions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | **str**| vendor |
 **minimum_version** | **str**| Exclude versions that are higher than the minimum version specified | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SoftwareManagementVersionsGet200Response**](NexusInsightsApiV1SoftwareManagementVersionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

