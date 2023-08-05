# nexuscloud_client.IntegrationsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_vcenter_browse_get**](IntegrationsApi.md#nexus_insights_api_v1_vcenter_browse_get) | **GET** /nexus/insights/api/v1/vcenter/browse | Browse API for different vcenter objects
[**nexus_insights_api_v1_vcenter_details_get**](IntegrationsApi.md#nexus_insights_api_v1_vcenter_details_get) | **GET** /nexus/insights/api/v1/vcenter/details | Details API for different vcenter objects
[**nexus_insights_api_v1_vcenter_summary_get**](IntegrationsApi.md#nexus_insights_api_v1_vcenter_summary_get) | **GET** /nexus/insights/api/v1/vcenter/summary | Get summary of vms
[**nexus_insights_api_v1_vcenter_top_entities_get**](IntegrationsApi.md#nexus_insights_api_v1_vcenter_top_entities_get) | **GET** /nexus/insights/api/v1/vcenter/topEntities | Top Entities API for different vcenter objects
[**nexus_insights_api_v1_vcenter_topology_get**](IntegrationsApi.md#nexus_insights_api_v1_vcenter_topology_get) | **GET** /nexus/insights/api/v1/vcenter/topology | Get topology of a vcenter entity


# **nexus_insights_api_v1_vcenter_browse_get**
> NexusInsightsApiV1VcenterBrowseGet200Response nexus_insights_api_v1_vcenter_browse_get(object)

Browse API for different vcenter objects

Browse API for different vcenter objects

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import integrations_api
from nexuscloud_client.model.nexus_insights_api_v1_vcenter_browse_get200_response import NexusInsightsApiV1VcenterBrowseGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    object = "vm" # str | Object in the vcenter hierarchy
    start_date = "2021-04-15T15:52:29-07:00" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-15m"
    end_date = "2021-04-15T16:07:29-07:00" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "swmp3-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "swmp3" # str | Name of the Site - limit the records pertaining to the site (optional)
    filter = "filter_example" # str | Lucene format filter - Filter the response based on this filter field (optional)
    count = 10 # int | Num of nodes in response. (optional)
    offset = 0 # int | Pagination index into response. (optional) if omitted the server will use the default value of 0
    sort = "-anomalyScore" # str | Sort the reponse by which attribute and which order. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Browse API for different vcenter objects
        api_response = api_instance.nexus_insights_api_v1_vcenter_browse_get(object)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_browse_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Browse API for different vcenter objects
        api_response = api_instance.nexus_insights_api_v1_vcenter_browse_get(object, start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, filter=filter, count=count, offset=offset, sort=sort)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_browse_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object in the vcenter hierarchy |
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-15m"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **count** | **int**| Num of nodes in response. | [optional]
 **offset** | **int**| Pagination index into response. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| Sort the reponse by which attribute and which order. | [optional]

### Return type

[**NexusInsightsApiV1VcenterBrowseGet200Response**](NexusInsightsApiV1VcenterBrowseGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Either missing a mandatory param or provided an unsupported param |  -  |
**417** | No sites in given Insights Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_vcenter_details_get**
> NexusInsightsApiV1VcenterDetailsGet200Response nexus_insights_api_v1_vcenter_details_get(object)

Details API for different vcenter objects

Details API for different vcenter objects

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import integrations_api
from nexuscloud_client.model.nexus_insights_api_v1_vcenter_details_get200_response import NexusInsightsApiV1VcenterDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    object = "vm" # str | Object in the vcenter hierarchy
    start_date = "2021-04-15T15:52:29-07:00" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-15m"
    end_date = "2021-04-15T16:07:29-07:00" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "swmp3-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "swmp3" # str | Name of the Site - limit the records pertaining to the site (optional)
    filter = "filter_example" # str | Lucene format filter - Filter the response based on this filter field (optional)
    count = 10 # int | Limit the number of records in the response (optional)
    offset = 0 # int | Pagination index into response. (optional) if omitted the server will use the default value of 0
    stat_name = "netUsageAverage,cpuUsagePct" # str | Limit statistics in the response (optional)
    granularity = "10m" # str | Granularity of the timeseries data w.r.t duration (optional) if omitted the server will use the default value of "5m"

    # example passing only required values which don't have defaults set
    try:
        # Details API for different vcenter objects
        api_response = api_instance.nexus_insights_api_v1_vcenter_details_get(object)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Details API for different vcenter objects
        api_response = api_instance.nexus_insights_api_v1_vcenter_details_get(object, start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, filter=filter, count=count, offset=offset, stat_name=stat_name, granularity=granularity)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object in the vcenter hierarchy |
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-15m"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **count** | **int**| Limit the number of records in the response | [optional]
 **offset** | **int**| Pagination index into response. | [optional] if omitted the server will use the default value of 0
 **stat_name** | **str**| Limit statistics in the response | [optional]
 **granularity** | **str**| Granularity of the timeseries data w.r.t duration | [optional] if omitted the server will use the default value of "5m"

### Return type

[**NexusInsightsApiV1VcenterDetailsGet200Response**](NexusInsightsApiV1VcenterDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Either missing a mandatory param or provided an unsupported param |  -  |
**417** | No sites in given Insights Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_vcenter_summary_get**
> NexusInsightsApiV1VcenterSummaryGet200Response nexus_insights_api_v1_vcenter_summary_get()

Get summary of vms

Get aggregated count of vms

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import integrations_api
from nexuscloud_client.model.nexus_insights_api_v1_vcenter_summary_get200_response import NexusInsightsApiV1VcenterSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    start_date = "2021-04-15T15:52:29-07:00" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-15m"
    end_date = "2021-04-15T16:07:29-07:00" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "swmp3-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "swmp3" # str | Name of the Site - limit the records pertaining to the site (optional)
    aggr = "anomalyScore" # str | Aggregate records by this field (optional) if omitted the server will use the default value of "anomalyScore"

    # example passing only required values which don't have defaults set
    try:
        # Get summary of vms
        api_response = api_instance.nexus_insights_api_v1_vcenter_summary_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get summary of vms
        api_response = api_instance.nexus_insights_api_v1_vcenter_summary_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, aggr=aggr)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Integration type - limit the records pertaining to this type of integration | defaults to "vm"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-15m"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **aggr** | **str**| Aggregate records by this field | [optional] if omitted the server will use the default value of "anomalyScore"

### Return type

[**NexusInsightsApiV1VcenterSummaryGet200Response**](NexusInsightsApiV1VcenterSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Either missing a mandatory param or provided an unsupported param |  -  |
**417** | No sites in given Insights Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_vcenter_top_entities_get**
> NexusInsightsApiV1VcenterTopEntitiesGet200Response nexus_insights_api_v1_vcenter_top_entities_get(object, stat_name, sort)

Top Entities API for different vcenter objects

Top Entities API for different vcenter objects

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import integrations_api
from nexuscloud_client.model.nexus_insights_api_v1_vcenter_top_entities_get200_response import NexusInsightsApiV1VcenterTopEntitiesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    object = "vm" # str | Object in the application hierarchy
    stat_name = "netUsageAverage,cpuUsagePct" # str | Limit statistics in the response
    sort = "-anomalyScore" # str | Sort the reponse by which attribute and which order.
    start_date = "2021-04-15T15:52:29-07:00" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-15m"
    end_date = "2021-04-15T16:07:29-07:00" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "swmp3-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "swmp3" # str | Name of the Site - limit the records pertaining to the site (optional)
    filter = "controllerName:test-cntl" # str | Lucene format filter - Filter the response based on this filter field (optional)
    count = 10 # int | Limit the number of records in the response (optional) if omitted the server will use the default value of 1
    granularity = "10m" # str | Granularity of statistics in the response (optional) if omitted the server will use the default value of "5m"

    # example passing only required values which don't have defaults set
    try:
        # Top Entities API for different vcenter objects
        api_response = api_instance.nexus_insights_api_v1_vcenter_top_entities_get(object, stat_name, sort)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_top_entities_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Top Entities API for different vcenter objects
        api_response = api_instance.nexus_insights_api_v1_vcenter_top_entities_get(object, stat_name, sort, start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, filter=filter, count=count, granularity=granularity)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_top_entities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object in the application hierarchy |
 **stat_name** | **str**| Limit statistics in the response |
 **sort** | **str**| Sort the reponse by which attribute and which order. |
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-15m"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **count** | **int**| Limit the number of records in the response | [optional] if omitted the server will use the default value of 1
 **granularity** | **str**| Granularity of statistics in the response | [optional] if omitted the server will use the default value of "5m"

### Return type

[**NexusInsightsApiV1VcenterTopEntitiesGet200Response**](NexusInsightsApiV1VcenterTopEntitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Either missing a mandatory param or provided an unsupported param |  -  |
**417** | No sites in given Insights Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_vcenter_topology_get**
> NexusInsightsApiV1VcenterTopologyGet200Response nexus_insights_api_v1_vcenter_topology_get(filter, object)

Get topology of a vcenter entity

Get topology of a vcenter entity

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import integrations_api
from nexuscloud_client.model.nexus_insights_api_v1_vcenter_topology_get200_response import NexusInsightsApiV1VcenterTopologyGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    filter = "entityDn:/controller-swmp3vcenter/host-131/vm-180" # str | Lucene format filter - Filter the response based on this filter field
    object = "vm" # str | Object in the application hierarchy
    start_date = "2021-04-15T15:52:29-07:00" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-15m"
    end_date = "2021-04-15T16:07:29-07:00" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "swmp3-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "swmp3" # str | Name of the Site - limit the records pertaining to the site (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get topology of a vcenter entity
        api_response = api_instance.nexus_insights_api_v1_vcenter_topology_get(filter, object)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_topology_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get topology of a vcenter entity
        api_response = api_instance.nexus_insights_api_v1_vcenter_topology_get(filter, object, start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling IntegrationsApi->nexus_insights_api_v1_vcenter_topology_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field |
 **object** | **str**| Object in the application hierarchy |
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-15m"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]

### Return type

[**NexusInsightsApiV1VcenterTopologyGet200Response**](NexusInsightsApiV1VcenterTopologyGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Either missing a mandatory param or provided an unsupported param |  -  |
**417** | No sites in given Insights Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

