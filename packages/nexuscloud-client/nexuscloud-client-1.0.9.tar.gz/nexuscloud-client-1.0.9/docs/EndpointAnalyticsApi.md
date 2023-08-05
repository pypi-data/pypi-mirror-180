# nexuscloud_client.EndpointAnalyticsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_endpoints_anomalies_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_anomalies_get) | **GET** /nexus/insights/api/v1/endpoints/anomalies | Get the anomaly history of an endpoint.
[**nexus_insights_api_v1_endpoints_count_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_count_get) | **GET** /nexus/insights/api/v1/endpoints/count | Get the Endpoints Count of entire site or given a condition
[**nexus_insights_api_v1_endpoints_details_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_details_get) | **GET** /nexus/insights/api/v1/endpoints/details | Get the history of an endpoint
[**nexus_insights_api_v1_endpoints_duplicate_ips_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_duplicate_ips_get) | **GET** /nexus/insights/api/v1/endpoints/duplicateIps | Get the count of duplicate IPs.
[**nexus_insights_api_v1_endpoints_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_get) | **GET** /nexus/insights/api/v1/endpoints | Get the snapshot of entire site or a particular node at a given time
[**nexus_insights_api_v1_endpoints_history_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_history_get) | **GET** /nexus/insights/api/v1/endpoints/history | Get the history of an endpoint
[**nexus_insights_api_v1_endpoints_statistics_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_statistics_get) | **GET** /nexus/insights/api/v1/endpoints/statistics | Get the top nodes by endpoint statistics.
[**nexus_insights_api_v1_endpoints_top_endpoints_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_top_endpoints_get) | **GET** /nexus/insights/api/v1/endpoints/topEndpoints | Get the top nodes by endpoint anomaly score.
[**nexus_insights_api_v1_endpoints_top_nodes_get**](EndpointAnalyticsApi.md#nexus_insights_api_v1_endpoints_top_nodes_get) | **GET** /nexus/insights/api/v1/endpoints/topNodes | Get the top nodes by endpoint stat.


# **nexus_insights_api_v1_endpoints_anomalies_get**
> NexusInsightsApiV1EndpointsAnomaliesGet200Response nexus_insights_api_v1_endpoints_anomalies_get(site_group_name, endpoint)

Get the anomaly history of an endpoint.

Get the entire anomaly history of an endpoint based on the timestamp.

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_anomalies_get200_response import NexusInsightsApiV1EndpointsAnomaliesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "IG-ACI" # str | Name of the Site Group - limit the records pertaining to the sites in this site group
    endpoint = "Topo3/tenant/vxlan-900101/Vlan1001/00:56:01:00:00:01" # str | Endpoint for which the anomaly history is to be retrieved
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    offset = "0" # str | Pagination index into response. (optional) if omitted the server will use the default value of "0"
    count = "5" # str | Num of nodes in response. (optional) if omitted the server will use the default value of "10"
    sort = "-severity" # str | Sort the reponse by which attribute and which order. (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    filter = "cleared:false%20AND%20acknowledged:false" # str | Lucene format filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the anomaly history of an endpoint.
        api_response = api_instance.nexus_insights_api_v1_endpoints_anomalies_get(site_group_name, endpoint)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_anomalies_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the anomaly history of an endpoint.
        api_response = api_instance.nexus_insights_api_v1_endpoints_anomalies_get(site_group_name, endpoint, site_name=site_name, offset=offset, count=count, sort=sort, start_date=start_date, end_date=end_date, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_anomalies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group |
 **endpoint** | **str**| Endpoint for which the anomaly history is to be retrieved |
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **offset** | **str**| Pagination index into response. | [optional] if omitted the server will use the default value of "0"
 **count** | **str**| Num of nodes in response. | [optional] if omitted the server will use the default value of "10"
 **sort** | **str**| Sort the reponse by which attribute and which order. | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **filter** | **str**| Lucene format filter | [optional]

### Return type

[**NexusInsightsApiV1EndpointsAnomaliesGet200Response**](NexusInsightsApiV1EndpointsAnomaliesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_count_get**
> NexusInsightsApiV1EndpointsCountGet200Response nexus_insights_api_v1_endpoints_count_get()

Get the Endpoints Count of entire site or given a condition

Get the Endpoints Count of entire site or given a condition

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_count_get200_response import NexusInsightsApiV1EndpointsCountGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    end_date = "2021-04-20T01:50:11-07:00" # str | End timestamp (optional) if omitted the server will use the default value of "now"
    filter = "interfaceName:po1" # str | Lucene format filter (optional)
    aggr = "interfaceName" # str | Get the epCount, aggregation by this field (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Endpoints Count of entire site or given a condition
        api_response = api_instance.nexus_insights_api_v1_endpoints_count_get(site_group_name=site_group_name, site_name=site_name, end_date=end_date, filter=filter, aggr=aggr)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **end_date** | **str**| End timestamp | [optional] if omitted the server will use the default value of "now"
 **filter** | **str**| Lucene format filter | [optional]
 **aggr** | **str**| Get the epCount, aggregation by this field | [optional]

### Return type

[**NexusInsightsApiV1EndpointsCountGet200Response**](NexusInsightsApiV1EndpointsCountGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_details_get**
> NexusInsightsApiV1EndpointsDetailsGet200Response nexus_insights_api_v1_endpoints_details_get()

Get the history of an endpoint

Get the entire history of an endpoint based on the timestamp

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_details_get200_response import NexusInsightsApiV1EndpointsDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    endpoint = "Topo3/tenant/vxlan-900101/Vlan1001/00:56:01:00:00:01" # str | Endpoint for which the history is to be retrieved (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-04-21T15:35:35-07:00" # str | End date, to collect the records generated till specified date (optional)
    filter = "interfaceName:po1" # str | Lucene format filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the history of an endpoint
        api_response = api_instance.nexus_insights_api_v1_endpoints_details_get(site_group_name=site_group_name, site_name=site_name, endpoint=endpoint, start_date=start_date, end_date=end_date, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **endpoint** | **str**| Endpoint for which the history is to be retrieved | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **filter** | **str**| Lucene format filter | [optional]

### Return type

[**NexusInsightsApiV1EndpointsDetailsGet200Response**](NexusInsightsApiV1EndpointsDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**417** | No sites in given siteGroupName |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_duplicate_ips_get**
> NexusInsightsApiV1EndpointsDuplicateIpsGet200Response nexus_insights_api_v1_endpoints_duplicate_ips_get()

Get the count of duplicate IPs.

Get the count of duplicate IPs associated with an endpoint based on the timestamp

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_duplicate_ips_get200_response import NexusInsightsApiV1EndpointsDuplicateIpsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    endpoint = "Topo3/tenant/vxlan-900101/Vlan1001/00:56:01:00:00:01" # str | Endpoint for which the duplicate ips are to be retrieved (optional)
    details = "true" # str | option to include the details of duplicate ips list (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the count of duplicate IPs.
        api_response = api_instance.nexus_insights_api_v1_endpoints_duplicate_ips_get(site_group_name=site_group_name, site_name=site_name, endpoint=endpoint, details=details, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_duplicate_ips_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **endpoint** | **str**| Endpoint for which the duplicate ips are to be retrieved | [optional]
 **details** | **str**| option to include the details of duplicate ips list | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"

### Return type

[**NexusInsightsApiV1EndpointsDuplicateIpsGet200Response**](NexusInsightsApiV1EndpointsDuplicateIpsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**417** | No sites in given siteGroupName |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_get**
> NexusInsightsApiV1EndpointsGet200Response nexus_insights_api_v1_endpoints_get()

Get the snapshot of entire site or a particular node at a given time

Get the snapshot of entire site or a particular node at a given time

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_get200_response import NexusInsightsApiV1EndpointsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    offset = "0" # str | Pagination index into response. (optional) if omitted the server will use the default value of "0"
    count = "10" # str | Num of nodes in response. (optional) if omitted the server will use the default value of "10"
    sort = "-anomalyScore" # str | Sort the reponse by which attribute and which order. (optional)
    filter = "includeDeletedIPs:true" # str | Lucene format filter (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the snapshot of entire site or a particular node at a given time
        api_response = api_instance.nexus_insights_api_v1_endpoints_get(site_group_name=site_group_name, site_name=site_name, offset=offset, count=count, sort=sort, filter=filter, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **offset** | **str**| Pagination index into response. | [optional] if omitted the server will use the default value of "0"
 **count** | **str**| Num of nodes in response. | [optional] if omitted the server will use the default value of "10"
 **sort** | **str**| Sort the reponse by which attribute and which order. | [optional]
 **filter** | **str**| Lucene format filter | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"

### Return type

[**NexusInsightsApiV1EndpointsGet200Response**](NexusInsightsApiV1EndpointsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_history_get**
> NexusInsightsApiV1EndpointsHistoryGet200Response nexus_insights_api_v1_endpoints_history_get(endpoint)

Get the history of an endpoint

Get the entire history of an endpoint based on the timestamp

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_history_get200_response import NexusInsightsApiV1EndpointsHistoryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    endpoint = "Topo3/tenant/vxlan-900101/Vlan1001/00:56:01:00:00:01" # str | Endpoint for which the history is to be retrieved
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    offset = "0" # str | Pagination index into response. (optional) if omitted the server will use the default value of "0"
    count = "10" # str | Num of nodes in response. (optional) if omitted the server will use the default value of "10"
    sort = "-createTime" # str | Sort the reponse by which attribute and which order. (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    try:
        # Get the history of an endpoint
        api_response = api_instance.nexus_insights_api_v1_endpoints_history_get(endpoint)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the history of an endpoint
        api_response = api_instance.nexus_insights_api_v1_endpoints_history_get(endpoint, site_group_name=site_group_name, site_name=site_name, offset=offset, count=count, sort=sort, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Endpoint for which the history is to be retrieved |
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **offset** | **str**| Pagination index into response. | [optional] if omitted the server will use the default value of "0"
 **count** | **str**| Num of nodes in response. | [optional] if omitted the server will use the default value of "10"
 **sort** | **str**| Sort the reponse by which attribute and which order. | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"

### Return type

[**NexusInsightsApiV1EndpointsHistoryGet200Response**](NexusInsightsApiV1EndpointsHistoryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**417** | No sites in given siteGroupName |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_statistics_get**
> NexusInsightsApiV1EndpointsStatisticsGet200Response nexus_insights_api_v1_endpoints_statistics_get()

Get the top nodes by endpoint statistics.

Get the top nodes by endpoint anomaly score or total endpoints.

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_statistics_get200_response import NexusInsightsApiV1EndpointsStatisticsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    filter = "filter_example" # str | Lucene format filter - Filter the response based on this filter field (optional)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    count = "10" # str | Num of nodes in response. (optional) if omitted the server will use the default value of "10"
    stat_name = "totalEndpoints" # str | The statName to get the top nodes by. (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the top nodes by endpoint statistics.
        api_response = api_instance.nexus_insights_api_v1_endpoints_statistics_get(filter=filter, site_group_name=site_group_name, site_name=site_name, count=count, stat_name=stat_name, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_statistics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **count** | **str**| Num of nodes in response. | [optional] if omitted the server will use the default value of "10"
 **stat_name** | **str**| The statName to get the top nodes by. | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"

### Return type

[**NexusInsightsApiV1EndpointsStatisticsGet200Response**](NexusInsightsApiV1EndpointsStatisticsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_top_endpoints_get**
> NexusInsightsApiV1EndpointsTopEndpointsGet200Response nexus_insights_api_v1_endpoints_top_endpoints_get()

Get the top nodes by endpoint anomaly score.

Get the top nodes by endpoint anomaly score.

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_top_endpoints_get200_response import NexusInsightsApiV1EndpointsTopEndpointsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    count = "10" # str | Num of nodes in response. (optional) if omitted the server will use the default value of "10"
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    filter = "filter_example" # str | Lucene format filter - Filter the response based on this filter field (optional)
    stat_name = "anomalyScore" # str | The statName to get the top nodes by. (optional) if omitted the server will use the default value of "anomalyScore"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the top nodes by endpoint anomaly score.
        api_response = api_instance.nexus_insights_api_v1_endpoints_top_endpoints_get(site_group_name=site_group_name, site_name=site_name, count=count, start_date=start_date, end_date=end_date, filter=filter, stat_name=stat_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_top_endpoints_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **count** | **str**| Num of nodes in response. | [optional] if omitted the server will use the default value of "10"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **stat_name** | **str**| The statName to get the top nodes by. | [optional] if omitted the server will use the default value of "anomalyScore"

### Return type

[**NexusInsightsApiV1EndpointsTopEndpointsGet200Response**](NexusInsightsApiV1EndpointsTopEndpointsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_endpoints_top_nodes_get**
> NexusInsightsApiV1EndpointsStatisticsGet200Response nexus_insights_api_v1_endpoints_top_nodes_get()

Get the top nodes by endpoint stat.

Get the top nodes by endpoint anomaly score or total endpoints.

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_statistics_get200_response import NexusInsightsApiV1EndpointsStatisticsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_api.EndpointAnalyticsApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    count = "10" # str | Num of nodes in response. (optional) if omitted the server will use the default value of "10"
    stat_name = "totalEndpoints" # str | The statName to get the top nodes by. (optional)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the top nodes by endpoint stat.
        api_response = api_instance.nexus_insights_api_v1_endpoints_top_nodes_get(site_group_name=site_group_name, site_name=site_name, count=count, stat_name=stat_name, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsApi->nexus_insights_api_v1_endpoints_top_nodes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **count** | **str**| Num of nodes in response. | [optional] if omitted the server will use the default value of "10"
 **stat_name** | **str**| The statName to get the top nodes by. | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"

### Return type

[**NexusInsightsApiV1EndpointsStatisticsGet200Response**](NexusInsightsApiV1EndpointsStatisticsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**417** | No sites in given siteGroupName |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

