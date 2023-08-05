# nexuscloud_client.AnomaliesApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_alerts_trend_get**](AnomaliesApi.md#nexus_insights_api_v1_alerts_trend_get) | **GET** /nexus/insights/api/v1/alerts/trend | Get the number of anomalies for past one week
[**nexus_insights_api_v1_anomalies_buckets_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_buckets_get) | **GET** /nexus/insights/api/v1/anomalies/buckets | Return the anomalies buckets
[**nexus_insights_api_v1_anomalies_details_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_details_get) | **GET** /nexus/insights/api/v1/anomalies/details | Get Anomalies details list
[**nexus_insights_api_v1_anomalies_related_metrics_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_related_metrics_get) | **GET** /nexus/insights/api/v1/anomalies/relatedMetrics | Get the list of default resources
[**nexus_insights_api_v1_anomalies_related_metrics_post**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_related_metrics_post) | **POST** /nexus/insights/api/v1/anomalies/relatedMetrics | Get the list of default resources
[**nexus_insights_api_v1_anomalies_related_objects_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_related_objects_get) | **GET** /nexus/insights/api/v1/anomalies/relatedObjects | Get the list of related objects
[**nexus_insights_api_v1_anomalies_summary_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_summary_get) | **GET** /nexus/insights/api/v1/anomalies/summary | Get the summary of anomalies
[**nexus_insights_api_v1_anomalies_time_range_trend_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_time_range_trend_get) | **GET** /nexus/insights/api/v1/anomalies/timeRangeTrend | Get the number of anomalies for past one week
[**nexus_insights_api_v1_anomalies_top_fabrics_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_top_fabrics_get) | **GET** /nexus/insights/api/v1/anomalies/topFabrics | Get Top Fabrics based on Anomaly Score
[**nexus_insights_api_v1_anomalies_top_flow_records_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_top_flow_records_get) | **GET** /nexus/insights/api/v1/anomalies/topFlowRecords | Get top flow records by anomalies
[**nexus_insights_api_v1_anomalies_top_flows_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_top_flows_get) | **GET** /nexus/insights/api/v1/anomalies/topFlows | Get the top flows by anomalies
[**nexus_insights_api_v1_anomalies_top_nodes_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_top_nodes_get) | **GET** /nexus/insights/api/v1/anomalies/topNodes | Get top nodes list based on anomaly score
[**nexus_insights_api_v1_anomalies_trend_get**](AnomaliesApi.md#nexus_insights_api_v1_anomalies_trend_get) | **GET** /nexus/insights/api/v1/anomalies/trend | Get the trend of anomalies


# **nexus_insights_api_v1_alerts_trend_get**
> NexusInsightsApiV1AlertsTrendGet200Response nexus_insights_api_v1_alerts_trend_get()

Get the number of anomalies for past one week

Given an insightsGroup or Fabric, return the number of anomalies on every day of the week

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_alerts_trend_get200_response import NexusInsightsApiV1AlertsTrendGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "default" # str | Name of the site group - limit the records pertaining to this site group (optional)
    site_name = "DC-WEST" # str | Name of the site - limit the records pertaining to this site (optional)
    trend_interval = "1d" # str |  (optional)
    start_ts = "2022-08-08T23:59:59.999Z" # str |  (optional)
    end_ts = "2022-08-17T23:59:59.999Z" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the number of anomalies for past one week
        api_response = api_instance.nexus_insights_api_v1_alerts_trend_get(site_group_name=site_group_name, site_name=site_name, trend_interval=trend_interval, start_ts=start_ts, end_ts=end_ts)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_alerts_trend_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the site group - limit the records pertaining to this site group | [optional]
 **site_name** | **str**| Name of the site - limit the records pertaining to this site | [optional]
 **trend_interval** | **str**|  | [optional]
 **start_ts** | **str**|  | [optional]
 **end_ts** | **str**|  | [optional]

### Return type

[**NexusInsightsApiV1AlertsTrendGet200Response**](NexusInsightsApiV1AlertsTrendGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_buckets_get**
> NexusInsightsApiV1AnomaliesBucketsGet200Response nexus_insights_api_v1_anomalies_buckets_get()

Return the anomalies buckets

Returning anomalies buckets

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_buckets_get200_response import NexusInsightsApiV1AnomaliesBucketsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "DC-WEST-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    granularity = "338m" # str | Granularity of the timeseries data w.r.t duration (optional)
    end_date = "2021-04-20T10%3A23%3A22.756-07%3A00" # str | End date, to collect the records generated till specified date (optional)
    start_date = "2021-04-14T13%3A23%3A47.000-07%3A00" # str | Start date, to skip records generated earlier to this date (optional)
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return the anomalies buckets
        api_response = api_instance.nexus_insights_api_v1_anomalies_buckets_get(site_group_name=site_group_name, granularity=granularity, end_date=end_date, start_date=start_date, site_name=site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_buckets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **granularity** | **str**| Granularity of the timeseries data w.r.t duration | [optional]
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesBucketsGet200Response**](NexusInsightsApiV1AnomaliesBucketsGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_details_get**
> NexusInsightsApiV1AnomaliesDetailsGet200Response nexus_insights_api_v1_anomalies_details_get()

Get Anomalies details list

Get the list of anomalies for a given IG or site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_details_get200_response import NexusInsightsApiV1AnomaliesDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    filter = "acknowledged:false" # str | Lucene format filter - Filter the response based on this filter field (optional)
    site_group_name = "DC-WEST-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    node_name = "ifav-leaf1" # str | Name of the fabric node, limit the anomaly score to given nodeName (optional) if omitted the server will use the default value of "None"
    offset = "0" # str | Pagination index into response. (optional)
    count = "10" # str | Num of nodes in response. (optional)
    end_date = "2021-04-19T14:08:05-07:00" # str | End date, to collect the records generated till specified date (optional)
    sort = "-severity" # str | Sort the reponse by which attribute and which order. (optional)
    start_date = "2021-04-19T13:53:05-07:00" # str | Start date, to skip records generated earlier to this date (optional)
    aggr = "mnemonicTitle" # str | Aggregate records by this field (optional)
    site_status = "all" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Anomalies details list
        api_response = api_instance.nexus_insights_api_v1_anomalies_details_get(filter=filter, site_group_name=site_group_name, site_name=site_name, node_name=node_name, offset=offset, count=count, end_date=end_date, sort=sort, start_date=start_date, aggr=aggr, site_status=site_status)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **node_name** | **str**| Name of the fabric node, limit the anomaly score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **offset** | **str**| Pagination index into response. | [optional]
 **count** | **str**| Num of nodes in response. | [optional]
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **sort** | **str**| Sort the reponse by which attribute and which order. | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **aggr** | **str**| Aggregate records by this field | [optional]
 **site_status** | **str**|  | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesDetailsGet200Response**](NexusInsightsApiV1AnomaliesDetailsGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_related_metrics_get**
> NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response nexus_insights_api_v1_anomalies_related_metrics_get()

Get the list of default resources

defaultDescription

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_related_metrics_get200_response import NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "SG_SJC2-candid-scale1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    anomaly_id = "VPC836136418329" # str | Identifier for the anomaly (optional)
    user_name = "apic-user" # str | User name (optional)
    site_name = "candid-scale1" # str | Name of the Site - limit the records pertaining to the site (optional)
    resource_list = "config:BD, config:EPG, environmental:Memory, environmental:CPU" # str | Comma separated list of tuples specifying the resources to be applied for POST request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of default resources
        api_response = api_instance.nexus_insights_api_v1_anomalies_related_metrics_get(site_group_name=site_group_name, anomaly_id=anomaly_id, user_name=user_name, site_name=site_name, resource_list=resource_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_related_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **anomaly_id** | **str**| Identifier for the anomaly | [optional]
 **user_name** | **str**| User name | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **resource_list** | **str**| Comma separated list of tuples specifying the resources to be applied for POST request. | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response**](NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_related_metrics_post**
> NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response nexus_insights_api_v1_anomalies_related_metrics_post()

Get the list of default resources

defaultDescription

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_related_metrics_get200_response import NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "SG_SJC2-candid-scale1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    anomaly_id = "VPC836136418329" # str | Identifier for the anomaly (optional)
    user_name = "apic-user" # str | User name (optional)
    site_name = "candid-scale1" # str | Name of the Site - limit the records pertaining to the site (optional)
    resource_list = "config:BD, config:EPG, environmental:Memory, environmental:CPU" # str | Comma separated list of tuples specifying the resources to be applied for POST request. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of default resources
        api_response = api_instance.nexus_insights_api_v1_anomalies_related_metrics_post(site_group_name=site_group_name, anomaly_id=anomaly_id, user_name=user_name, site_name=site_name, resource_list=resource_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_related_metrics_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **anomaly_id** | **str**| Identifier for the anomaly | [optional]
 **user_name** | **str**| User name | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **resource_list** | **str**| Comma separated list of tuples specifying the resources to be applied for POST request. | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response**](NexusInsightsApiV1AnomaliesRelatedMetricsGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_related_objects_get**
> NexusInsightsApiV1AnomaliesRelatedObjectsGet200Response nexus_insights_api_v1_anomalies_related_objects_get()

Get the list of related objects

Get the list of related objects

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_related_objects_get200_response import NexusInsightsApiV1AnomaliesRelatedObjectsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "SG_SJC2-candid-scale1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    end_date = "2021-04-22T16%3A32%3A31-07%3A00" # str | End date, to collect the records generated till specified date (optional)
    start_date = "2021-04-22T13%3A11%3A48-07%3A00" # str | Start date, to skip records generated earlier to this date (optional)
    site_name = "candid-scale1" # str | Name of the Site - limit the records pertaining to the site (optional)
    anomaly_id = "VPC836136418329" # str | Identifier for the anomaly (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of related objects
        api_response = api_instance.nexus_insights_api_v1_anomalies_related_objects_get(site_group_name=site_group_name, end_date=end_date, start_date=start_date, site_name=site_name, anomaly_id=anomaly_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_related_objects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **anomaly_id** | **str**| Identifier for the anomaly | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesRelatedObjectsGet200Response**](NexusInsightsApiV1AnomaliesRelatedObjectsGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_summary_get**
> NexusInsightsApiV1AnomaliesSummaryGet200Response nexus_insights_api_v1_anomalies_summary_get()

Get the summary of anomalies

Given an insightsGroup or Fabric, return the summary of anomalies

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_summary_get200_response import NexusInsightsApiV1AnomaliesSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "BANGALORE" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DC-WEST" # str | Name of the fabric - limit the records pertaining to this fabricName (optional)
    node_name = "ifav-leaf1" # str | Name of the fabric node, limit the anomaly score to given nodeName (optional) if omitted the server will use the default value of "None"
    filter = "None" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"
    end_date = "2021-04-20T12%3A24%3A09-07%3A00" # str | End date, to collect the records generated till specified date (optional)
    start_date = "2021-04-20T12%3A09%3A09-07%3A00" # str | Start date, to skip records generated earlier to this date (optional)
    aggr = "category" # str | Aggregate records by this field (optional)
    site_status = "all" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the summary of anomalies
        api_response = api_instance.nexus_insights_api_v1_anomalies_summary_get(site_group_name=site_group_name, site_name=site_name, node_name=node_name, filter=filter, end_date=end_date, start_date=start_date, aggr=aggr, site_status=site_status)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the fabric - limit the records pertaining to this fabricName | [optional]
 **node_name** | **str**| Name of the fabric node, limit the anomaly score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **aggr** | **str**| Aggregate records by this field | [optional]
 **site_status** | **str**|  | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesSummaryGet200Response**](NexusInsightsApiV1AnomaliesSummaryGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_time_range_trend_get**
> NexusInsightsApiV1AnomaliesTimeRangeTrendGet200Response nexus_insights_api_v1_anomalies_time_range_trend_get()

Get the number of anomalies for past one week

Given an insightsGroup or Fabric, return the number of anomalies on every day of the week

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_time_range_trend_get200_response import NexusInsightsApiV1AnomaliesTimeRangeTrendGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "default" # str | Name of the site group - limit the records pertaining to this site group (optional)
    site_name = "DC-WEST" # str | Name of the site - limit the records pertaining to this site (optional)
    trend_interval = "1d" # str |  (optional)
    num_past_intervals = 7 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the number of anomalies for past one week
        api_response = api_instance.nexus_insights_api_v1_anomalies_time_range_trend_get(site_group_name=site_group_name, site_name=site_name, trend_interval=trend_interval, num_past_intervals=num_past_intervals)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_time_range_trend_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the site group - limit the records pertaining to this site group | [optional]
 **site_name** | **str**| Name of the site - limit the records pertaining to this site | [optional]
 **trend_interval** | **str**|  | [optional]
 **num_past_intervals** | **int**|  | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesTimeRangeTrendGet200Response**](NexusInsightsApiV1AnomaliesTimeRangeTrendGet200Response.md)

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

# **nexus_insights_api_v1_anomalies_top_fabrics_get**
> NexusInsightsApiV1AnomaliesTopFabricsGet200Response nexus_insights_api_v1_anomalies_top_fabrics_get()

Get Top Fabrics based on Anomaly Score

Get Top Fabrics along with Anomaly Score and Anomaly Count

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_top_fabrics_get200_response import NexusInsightsApiV1AnomaliesTopFabricsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "telemetry-ig" # str | Name of the Site Group, limit the records to this site group (optional) if omitted the server will use the default value of "None"
    count = 5 # int | Limits the number of entries in the response (optional) if omitted the server will use the default value of 10
    offset = 0 # int | Pagination index into response. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Top Fabrics based on Anomaly Score
        api_response = api_instance.nexus_insights_api_v1_anomalies_top_fabrics_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, count=count, offset=offset)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_top_fabrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group, limit the records to this site group | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limits the number of entries in the response | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| Pagination index into response. | [optional] if omitted the server will use the default value of 0

### Return type

[**NexusInsightsApiV1AnomaliesTopFabricsGet200Response**](NexusInsightsApiV1AnomaliesTopFabricsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_anomalies_top_flow_records_get**
> NexusInsightsApiV1AnomaliesTopFlowRecordsGet200Response nexus_insights_api_v1_anomalies_top_flow_records_get()

Get top flow records by anomalies

Get top flow records by anomalies

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_top_flow_records_get200_response import NexusInsightsApiV1AnomaliesTopFlowRecordsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "NI-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    node_name = "ifav-leaf1" # str | Name of the fabric node, limit the anomaly score to given nodeName (optional) if omitted the server will use the default value of "None"
    count = "1" # str | Num of nodes in response. (optional)
    stat_name = "flow:pktdrop,latency" # str | The statName to get the top nodes by. (optional)
    filter = "acknowledged:false" # str | Lucene format filter - Filter the response based on this filter field (optional)
    granularity = "338m" # str | Granularity of the timeseries data w.r.t duration (optional)
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get top flow records by anomalies
        api_response = api_instance.nexus_insights_api_v1_anomalies_top_flow_records_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_top_flow_records_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get top flow records by anomalies
        api_response = api_instance.nexus_insights_api_v1_anomalies_top_flow_records_get(site_group_name=site_group_name, node_name=node_name, count=count, stat_name=stat_name, filter=filter, granularity=granularity, site_name=site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_top_flow_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date, to collect the records generated till specified date | defaults to "now"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | defaults to "now-15m"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **node_name** | **str**| Name of the fabric node, limit the anomaly score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **count** | **str**| Num of nodes in response. | [optional]
 **stat_name** | **str**| The statName to get the top nodes by. | [optional]
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **granularity** | **str**| Granularity of the timeseries data w.r.t duration | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesTopFlowRecordsGet200Response**](NexusInsightsApiV1AnomaliesTopFlowRecordsGet200Response.md)

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
**500** | Internal Server Error, The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application. |  -  |
**502** | Bad Gateway, Site is down |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_anomalies_top_flows_get**
> NexusInsightsApiV1AnomaliesTopFlowsGet200Response nexus_insights_api_v1_anomalies_top_flows_get()

Get the top flows by anomalies

Get the top flows by anomalies

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_top_flows_get200_response import NexusInsightsApiV1AnomaliesTopFlowsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "NI-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "tel2" # str | Name of the Site - limit the records pertaining to the site (optional)
    count = "1" # str | Limit the number of records in the response (optional)
    offset = 0 # int | Pagination index into response. (optional) if omitted the server will use the default value of 0
    stat_name = "flow" # str | Limit statistics in the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the top flows by anomalies
        api_response = api_instance.nexus_insights_api_v1_anomalies_top_flows_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_top_flows_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the top flows by anomalies
        api_response = api_instance.nexus_insights_api_v1_anomalies_top_flows_get(site_group_name=site_group_name, site_name=site_name, count=count, offset=offset, stat_name=stat_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_top_flows_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date, to collect the records generated till specified date | defaults to "now"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | defaults to "now-15m"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **count** | **str**| Limit the number of records in the response | [optional]
 **offset** | **int**| Pagination index into response. | [optional] if omitted the server will use the default value of 0
 **stat_name** | **str**| Limit statistics in the response | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesTopFlowsGet200Response**](NexusInsightsApiV1AnomaliesTopFlowsGet200Response.md)

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
**500** | Internal Server Error, The server encountered an internal error and was unable to complete your request. Either the sever is overloaded or there is an error in the application. |  -  |
**502** | Bad Gateway, Site is down |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_anomalies_top_nodes_get**
> NexusInsightsApiV1AnomaliesTopNodesGet200Response nexus_insights_api_v1_anomalies_top_nodes_get()

Get top nodes list based on anomaly score

Get the list of the fabric wide top nodes based on anomaly scores

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_top_nodes_get200_response import NexusInsightsApiV1AnomaliesTopNodesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group, limit the records to this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr" # str | Name of the Site, limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    node_name = "ifav-leaf1" # str | Name of the Fabric node, limit the anomaly score to given nodeName (optional) if omitted the server will use the default value of "None"
    filter = "resourceType:bgp AND category:environmental" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"
    offset = 10 # int | Offset from which records are returned (optional) if omitted the server will use the default value of 0
    count = 5 # int | Limits the number of nodes in response (optional) if omitted the server will use the default value of 10
    stat_name = "cpu" # str | Type of the stats, either of {cpu, memory, queue} (optional) if omitted the server will use the default value of "None"
    level = "node" # str | Level at which records are to be returned like \"fabric\", \"node\" (optional) if omitted the server will use the default value of "None"
    aggr = "severity" # str | default value: \"severity\" (optional) if omitted the server will use the default value of "severity"
    granularity = "2m" # str | Granularity of the values w.r.t duration (optional) if omitted the server will use the default value of "5m"
    response_by_create_time = False # bool | Sort records in response by create time (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get top nodes list based on anomaly score
        api_response = api_instance.nexus_insights_api_v1_anomalies_top_nodes_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, node_name=node_name, filter=filter, offset=offset, count=count, stat_name=stat_name, level=level, aggr=aggr, granularity=granularity, response_by_create_time=response_by_create_time)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_top_nodes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group, limit the records to this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site, limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **node_name** | **str**| Name of the Fabric node, limit the anomaly score to given nodeName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"
 **offset** | **int**| Offset from which records are returned | [optional] if omitted the server will use the default value of 0
 **count** | **int**| Limits the number of nodes in response | [optional] if omitted the server will use the default value of 10
 **stat_name** | **str**| Type of the stats, either of {cpu, memory, queue} | [optional] if omitted the server will use the default value of "None"
 **level** | **str**| Level at which records are to be returned like \&quot;fabric\&quot;, \&quot;node\&quot; | [optional] if omitted the server will use the default value of "None"
 **aggr** | **str**| default value: \&quot;severity\&quot; | [optional] if omitted the server will use the default value of "severity"
 **granularity** | **str**| Granularity of the values w.r.t duration | [optional] if omitted the server will use the default value of "5m"
 **response_by_create_time** | **bool**| Sort records in response by create time | [optional] if omitted the server will use the default value of False

### Return type

[**NexusInsightsApiV1AnomaliesTopNodesGet200Response**](NexusInsightsApiV1AnomaliesTopNodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_anomalies_trend_get**
> NexusInsightsApiV1AnomaliesTrendGet200Response nexus_insights_api_v1_anomalies_trend_get()

Get the trend of anomalies

Given an insightsGroup or Fabric, return the trend of anomalies

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import anomalies_api
from nexuscloud_client.model.nexus_insights_api_v1_anomalies_trend_get200_response import NexusInsightsApiV1AnomaliesTrendGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = anomalies_api.AnomaliesApi(api_client)
    site_group_name = "default" # str | Name of the site group - limit the records pertaining to this site group (optional)
    site_name = "DC-WEST" # str | Name of the site - limit the records pertaining to this site (optional)
    trend_interval = "1d" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the trend of anomalies
        api_response = api_instance.nexus_insights_api_v1_anomalies_trend_get(site_group_name=site_group_name, site_name=site_name, trend_interval=trend_interval)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AnomaliesApi->nexus_insights_api_v1_anomalies_trend_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the site group - limit the records pertaining to this site group | [optional]
 **site_name** | **str**| Name of the site - limit the records pertaining to this site | [optional]
 **trend_interval** | **str**|  | [optional]

### Return type

[**NexusInsightsApiV1AnomaliesTrendGet200Response**](NexusInsightsApiV1AnomaliesTrendGet200Response.md)

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

