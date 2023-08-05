# nexuscloud_client.FabricsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_sites_get**](FabricsApi.md#nexus_insights_api_v1_sites_get) | **GET** /nexus/insights/api/v1/sites | Get fabrics list
[**nexus_insights_api_v1_sites_summary_get**](FabricsApi.md#nexus_insights_api_v1_sites_summary_get) | **GET** /nexus/insights/api/v1/sitesSummary | Get fabric anomaly summary
[**nexus_insights_api_v1_sites_top_nodes_get**](FabricsApi.md#nexus_insights_api_v1_sites_top_nodes_get) | **GET** /nexus/insights/api/v1/sites/topNodes | Get Fabric wide Top Nodes


# **nexus_insights_api_v1_sites_get**
> NexusInsightsApiV1SitesGet200Response nexus_insights_api_v1_sites_get()

Get fabrics list

Get detailed info of fabrics

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import fabrics_api
from nexuscloud_client.model.nexus_insights_api_v1_sites_get200_response import NexusInsightsApiV1SitesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fabrics_api.FabricsApi(api_client)
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr3" # str | Name of the Site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    filter = "configStatus:ENABLED" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"
    config_status = "None" # str | Config status (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get fabrics list
        api_response = api_instance.nexus_insights_api_v1_sites_get(site_group_name=site_group_name, site_name=site_name, filter=filter, config_status=config_status)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling FabricsApi->nexus_insights_api_v1_sites_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"
 **config_status** | **str**| Config status | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SitesGet200Response**](NexusInsightsApiV1SitesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fabrics list |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sites_summary_get**
> NexusInsightsApiV1SitesSummaryGet200Response nexus_insights_api_v1_sites_summary_get()

Get fabric anomaly summary

Get the fabric anomaly summary having number of anomalies generated and respective anomaly scores

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import fabrics_api
from nexuscloud_client.model.nexus_insights_api_v1_sites_summary_get200_response import NexusInsightsApiV1SitesSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fabrics_api.FabricsApi(api_client)
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr" # str | Name of the Site, Limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    history = "1" # str | Defines whether records need to be added with timeseries or not in response (optional) if omitted the server will use the default value of "0"
    granularity = "2m" # str | Granularity of the timeseries data w.r.t duration, applicable if history is set to yes (optional) if omitted the server will use the default value of "5m"
    include = "anomalyScore" # str | Includes the latest maximum anomalyscore of the site if set to \"anomalyScore\" (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get fabric anomaly summary
        api_response = api_instance.nexus_insights_api_v1_sites_summary_get(site_group_name=site_group_name, site_name=site_name, start_date=start_date, end_date=end_date, history=history, granularity=granularity, include=include)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling FabricsApi->nexus_insights_api_v1_sites_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site, Limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **history** | **str**| Defines whether records need to be added with timeseries or not in response | [optional] if omitted the server will use the default value of "0"
 **granularity** | **str**| Granularity of the timeseries data w.r.t duration, applicable if history is set to yes | [optional] if omitted the server will use the default value of "5m"
 **include** | **str**| Includes the latest maximum anomalyscore of the site if set to \&quot;anomalyScore\&quot; | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SitesSummaryGet200Response**](NexusInsightsApiV1SitesSummaryGet200Response.md)

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

# **nexus_insights_api_v1_sites_top_nodes_get**
> NexusInsightsApiV1SitesTopNodesGet200Response nexus_insights_api_v1_sites_top_nodes_get()

Get Fabric wide Top Nodes

Get Fabric wide top nodes by Resource Utilization, Environmental, Statistics, Flow Analytics and Endpoint Analytics

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import fabrics_api
from nexuscloud_client.model.nexus_insights_api_v1_sites_top_nodes_get200_response import NexusInsightsApiV1SitesTopNodesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fabrics_api.FabricsApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start timestamp, to skip records generated earlier to this timestamp (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End timestamp, to collect the records generated till specified time (optional) if omitted the server will use the default value of "now"
    node_name = "ifav-leaf1" # str | Name of the fabric node, limit the anamaloy score to given nodeName (optional) if omitted the server will use the default value of "None"
    site_group_name = "ifav-insight" # str | Name of Site Group, limit the records pertaining to the sites in this siteGroupName (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr" # str | Name of the Site, Limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    granularity = "1m" # str | Granularity of the values w.r.t duration, mandatory when history is 1 (optional) if omitted the server will use the default value of "5m"
    history = 1 # int | Defines whether records need to be added with timeseries or not in response (optional) if omitted the server will use the default value of 0
    count = 5 # int | Limits the number of entries in the response (optional) if omitted the server will use the default value of 10
    resource_count = 5 # int | Limits the number of resources entries per node (optional) if omitted the server will use the default value of 10
    score_type = "trendScore" # str | Score type, either of [totalScore, anomalyScore, trendScore, rawAnomalyScore] (optional) if omitted the server will use the default value of "rawAnomalyScore"
    resource_type = "environmental" # str | Resource type, either of [statistics, environmental, flow, resources, endpoint, all] (optional) if omitted the server will use the default value of "all"
    node_roles = "controller" # str | Specifies type of node or comma seprated mutiple types like leaf,contoller,spine (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fabric wide Top Nodes
        api_response = api_instance.nexus_insights_api_v1_sites_top_nodes_get(start_date=start_date, end_date=end_date, node_name=node_name, site_group_name=site_group_name, site_name=site_name, granularity=granularity, history=history, count=count, resource_count=resource_count, score_type=score_type, resource_type=resource_type, node_roles=node_roles)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling FabricsApi->nexus_insights_api_v1_sites_top_nodes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start timestamp, to skip records generated earlier to this timestamp | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End timestamp, to collect the records generated till specified time | [optional] if omitted the server will use the default value of "now"
 **node_name** | **str**| Name of the fabric node, limit the anamaloy score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **site_group_name** | **str**| Name of Site Group, limit the records pertaining to the sites in this siteGroupName | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site, Limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **granularity** | **str**| Granularity of the values w.r.t duration, mandatory when history is 1 | [optional] if omitted the server will use the default value of "5m"
 **history** | **int**| Defines whether records need to be added with timeseries or not in response | [optional] if omitted the server will use the default value of 0
 **count** | **int**| Limits the number of entries in the response | [optional] if omitted the server will use the default value of 10
 **resource_count** | **int**| Limits the number of resources entries per node | [optional] if omitted the server will use the default value of 10
 **score_type** | **str**| Score type, either of [totalScore, anomalyScore, trendScore, rawAnomalyScore] | [optional] if omitted the server will use the default value of "rawAnomalyScore"
 **resource_type** | **str**| Resource type, either of [statistics, environmental, flow, resources, endpoint, all] | [optional] if omitted the server will use the default value of "all"
 **node_roles** | **str**| Specifies type of node or comma seprated mutiple types like leaf,contoller,spine | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SitesTopNodesGet200Response**](NexusInsightsApiV1SitesTopNodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

