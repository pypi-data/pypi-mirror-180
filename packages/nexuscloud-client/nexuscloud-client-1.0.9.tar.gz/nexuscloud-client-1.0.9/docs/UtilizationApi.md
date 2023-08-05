# nexuscloud_client.UtilizationApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_utilization_energy_get**](UtilizationApi.md#nexus_insights_api_v1_utilization_energy_get) | **GET** /nexus/insights/api/v1/utilization/energy | Get Energy Consumption data
[**nexus_insights_api_v1_utilization_node_details_get**](UtilizationApi.md#nexus_insights_api_v1_utilization_node_details_get) | **GET** /nexus/insights/api/v1/utilization/nodeDetails | Utilization details of fabric nodes
[**nexus_insights_api_v1_utilization_resources_get**](UtilizationApi.md#nexus_insights_api_v1_utilization_resources_get) | **GET** /nexus/insights/api/v1/utilization/resources | Get resources list
[**nexus_insights_api_v1_utilization_sites_summary_get**](UtilizationApi.md#nexus_insights_api_v1_utilization_sites_summary_get) | **GET** /nexus/insights/api/v1/utilization/sitesSummary | Get fabric utilization stats summary
[**nexus_insights_api_v1_utilization_top_nodes_get**](UtilizationApi.md#nexus_insights_api_v1_utilization_top_nodes_get) | **GET** /nexus/insights/api/v1/utilization/topNodes | Get utilization top nodes


# **nexus_insights_api_v1_utilization_energy_get**
> NexusInsightsApiV1UtilizationEnergyGet200Response nexus_insights_api_v1_utilization_energy_get()

Get Energy Consumption data

Get energy consumed timeseries in Kilowat-hour

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import utilization_api
from nexuscloud_client.model.nexus_insights_api_v1_utilization_energy_get200_response import NexusInsightsApiV1UtilizationEnergyGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utilization_api.UtilizationApi(api_client)
    start_date = "now-1d" # str | Start Date, to collect the records from the specified date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "now" # str | End Date, to collect the records till the specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name (optional) if omitted the server will use the default value of "None"
    granularity = "3h" # str | Granularity of the values w.r.t duration (optional) if omitted the server will use the default value of "5m"
    history = "1" # str | Require the timeseries data or not (optional) if omitted the server will use the default value of "0"
    filter = "nodeName:tel1-leaf1" # str | Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Energy Consumption data
        api_response = api_instance.nexus_insights_api_v1_utilization_energy_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, granularity=granularity, history=history, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling UtilizationApi->nexus_insights_api_v1_utilization_energy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start Date, to collect the records from the specified date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End Date, to collect the records till the specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Site name - limit the records pertaining to given site name | [optional] if omitted the server will use the default value of "None"
 **granularity** | **str**| Granularity of the values w.r.t duration | [optional] if omitted the server will use the default value of "5m"
 **history** | **str**| Require the timeseries data or not | [optional] if omitted the server will use the default value of "0"
 **filter** | **str**| Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1UtilizationEnergyGet200Response**](NexusInsightsApiV1UtilizationEnergyGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_utilization_node_details_get**
> NexusInsightsApiV1UtilizationNodeDetailsGet200Response nexus_insights_api_v1_utilization_node_details_get()

Utilization details of fabric nodes

Gives the Environmental and Resource utilization details of the fabric nodes

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import utilization_api
from nexuscloud_client.model.nexus_insights_api_v1_utilization_node_details_get200_response import NexusInsightsApiV1UtilizationNodeDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utilization_api.UtilizationApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    node_name = "ifav-leaf1" # str | Name of the fabric node, limit the anamaloy score to given nodeName (optional) if omitted the server will use the default value of "None"
    stat_name = "hardware" # str | Stats type, either or combination of [operational, config, hardware, environmental, ALL]  (optional) if omitted the server will use the default value of "ALL"
    sub_resource_name = "None" # str | default value: None (optional) if omitted the server will use the default value of "None"
    history = 1 # int | Defines whether records need to be added with timeseries or not in response (optional) if omitted the server will use the default value of 0
    granularity = "2m" # str | Granularity of the values w.r.t duration (optional) if omitted the server will use the default value of "5m"
    scope = "subResource" # str | Node or subResource : if scope=subResource, then response is with sub-resources in same level as other resourcces (optional) if omitted the server will use the default value of "node"
    sub_tree = "None" # str | Requires the sub-resources data or not (sub-resources are available for only limited resources) (optional) if omitted the server will use the default value of "None"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr" # str | Name of the Site, Limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    anomaly_score = "no" # str | Furnish anomaly score in the response or not\" (optional) if omitted the server will use the default value of "yes"
    sort = "anomalyScore" # str | Sort results in response by fields like anomalyScore, nodeName. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "None"
    count = 1000 # int | Limits the number of entries (optional) if omitted the server will use the default value of 10000
    offset = 10 # int | Offset from which records are returned (optional) if omitted the server will use the default value of 0
    filter = "nodeName:tel1-leaf1" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Utilization details of fabric nodes
        api_response = api_instance.nexus_insights_api_v1_utilization_node_details_get(start_date=start_date, end_date=end_date, node_name=node_name, stat_name=stat_name, sub_resource_name=sub_resource_name, history=history, granularity=granularity, scope=scope, sub_tree=sub_tree, site_group_name=site_group_name, site_name=site_name, anomaly_score=anomaly_score, sort=sort, count=count, offset=offset, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling UtilizationApi->nexus_insights_api_v1_utilization_node_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **node_name** | **str**| Name of the fabric node, limit the anamaloy score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **stat_name** | **str**| Stats type, either or combination of [operational, config, hardware, environmental, ALL]  | [optional] if omitted the server will use the default value of "ALL"
 **sub_resource_name** | **str**| default value: None | [optional] if omitted the server will use the default value of "None"
 **history** | **int**| Defines whether records need to be added with timeseries or not in response | [optional] if omitted the server will use the default value of 0
 **granularity** | **str**| Granularity of the values w.r.t duration | [optional] if omitted the server will use the default value of "5m"
 **scope** | **str**| Node or subResource : if scope&#x3D;subResource, then response is with sub-resources in same level as other resourcces | [optional] if omitted the server will use the default value of "node"
 **sub_tree** | **str**| Requires the sub-resources data or not (sub-resources are available for only limited resources) | [optional] if omitted the server will use the default value of "None"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site, Limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **anomaly_score** | **str**| Furnish anomaly score in the response or not\&quot; | [optional] if omitted the server will use the default value of "yes"
 **sort** | **str**| Sort results in response by fields like anomalyScore, nodeName. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limits the number of entries | [optional] if omitted the server will use the default value of 10000
 **offset** | **int**| Offset from which records are returned | [optional] if omitted the server will use the default value of 0
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1UtilizationNodeDetailsGet200Response**](NexusInsightsApiV1UtilizationNodeDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_utilization_resources_get**
> NexusInsightsApiV1UtilizationResourcesGet200Response nexus_insights_api_v1_utilization_resources_get()

Get resources list

Get all resources list having resource name and respective category like BD:config, CPU:environmental etc

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import utilization_api
from nexuscloud_client.model.nexus_insights_api_v1_utilization_resources_get200_response import NexusInsightsApiV1UtilizationResourcesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utilization_api.UtilizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get resources list
        api_response = api_instance.nexus_insights_api_v1_utilization_resources_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling UtilizationApi->nexus_insights_api_v1_utilization_resources_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NexusInsightsApiV1UtilizationResourcesGet200Response**](NexusInsightsApiV1UtilizationResourcesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_utilization_sites_summary_get**
> NexusInsightsApiV1UtilizationSitesSummaryGet200Response nexus_insights_api_v1_utilization_sites_summary_get(site_name)

Get fabric utilization stats summary

Get fabric stats summary of utilization resources like Bridge Domains, Endpoint Groups, L4/L7 Devices etc

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import utilization_api
from nexuscloud_client.model.nexus_insights_api_v1_utilization_sites_summary_get200_response import NexusInsightsApiV1UtilizationSitesSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utilization_api.UtilizationApi(api_client)
    site_name = "ifav-blr" # str | Name of the Site, limit the records pertaining to this siteName
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    granularity = "2m" # str | Granularity of the values w.r.t duration (optional) if omitted the server will use the default value of "5m"

    # example passing only required values which don't have defaults set
    try:
        # Get fabric utilization stats summary
        api_response = api_instance.nexus_insights_api_v1_utilization_sites_summary_get(site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling UtilizationApi->nexus_insights_api_v1_utilization_sites_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get fabric utilization stats summary
        api_response = api_instance.nexus_insights_api_v1_utilization_sites_summary_get(site_name, start_date=start_date, end_date=end_date, granularity=granularity)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling UtilizationApi->nexus_insights_api_v1_utilization_sites_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Name of the Site, limit the records pertaining to this siteName |
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **granularity** | **str**| Granularity of the values w.r.t duration | [optional] if omitted the server will use the default value of "5m"

### Return type

[**NexusInsightsApiV1UtilizationSitesSummaryGet200Response**](NexusInsightsApiV1UtilizationSitesSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_utilization_top_nodes_get**
> NexusInsightsApiV1UtilizationTopNodesGet200Response nexus_insights_api_v1_utilization_top_nodes_get()

Get utilization top nodes

Get Top Nodes based on Utilization and Environmental resources

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import utilization_api
from nexuscloud_client.model.nexus_insights_api_v1_utilization_top_nodes_get200_response import NexusInsightsApiV1UtilizationTopNodesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utilization_api.UtilizationApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    score_type = "trendScore" # str | Score type, either of [totalScore, anomalyScore, trendScore, rawAnomalyScore, ALL] (optional) if omitted the server will use the default value of "ALL"
    stat_name = "environmental" # str | Type of the stats, either of [config, operational, hardware, environmental, ALL] (optional) if omitted the server will use the default value of "ALL"
    granularity = "1m" # str | Granularity of the values w.r.t duration (optional) if omitted the server will use the default value of "5m"
    count = "5" # str | Limits the number of entries in the response (optional) if omitted the server will use the default value of "10"
    resource_count = "6" # str | Limits the number of resources entries per node (optional) if omitted the server will use the default value of "5"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr" # str | Name of the Site, Limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    node_name = "ifav-leaf1" # str | Name of the fabric node, limit the anamaloy score to given nodeName (optional) if omitted the server will use the default value of "None"
    filter = "nodeName:ifav-leaf1" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get utilization top nodes
        api_response = api_instance.nexus_insights_api_v1_utilization_top_nodes_get(start_date=start_date, end_date=end_date, score_type=score_type, stat_name=stat_name, granularity=granularity, count=count, resource_count=resource_count, site_group_name=site_group_name, site_name=site_name, node_name=node_name, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling UtilizationApi->nexus_insights_api_v1_utilization_top_nodes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **score_type** | **str**| Score type, either of [totalScore, anomalyScore, trendScore, rawAnomalyScore, ALL] | [optional] if omitted the server will use the default value of "ALL"
 **stat_name** | **str**| Type of the stats, either of [config, operational, hardware, environmental, ALL] | [optional] if omitted the server will use the default value of "ALL"
 **granularity** | **str**| Granularity of the values w.r.t duration | [optional] if omitted the server will use the default value of "5m"
 **count** | **str**| Limits the number of entries in the response | [optional] if omitted the server will use the default value of "10"
 **resource_count** | **str**| Limits the number of resources entries per node | [optional] if omitted the server will use the default value of "5"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site, Limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **node_name** | **str**| Name of the fabric node, limit the anamaloy score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1UtilizationTopNodesGet200Response**](NexusInsightsApiV1UtilizationTopNodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

