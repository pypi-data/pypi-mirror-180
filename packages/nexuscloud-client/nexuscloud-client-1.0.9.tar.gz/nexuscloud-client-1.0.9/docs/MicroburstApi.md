# nexuscloud_client.MicroburstApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_microburst_queues_get**](MicroburstApi.md#nexus_insights_api_v1_microburst_queues_get) | **GET** /nexus/insights/api/v1/microburst/queues | Get interface queues
[**nexus_insights_api_v1_microburst_status_get**](MicroburstApi.md#nexus_insights_api_v1_microburst_status_get) | **GET** /nexus/insights/api/v1/microburst/status | Get microburst status of all fabrics
[**nexus_insights_api_v1_microburst_summary_get**](MicroburstApi.md#nexus_insights_api_v1_microburst_summary_get) | **GET** /nexus/insights/api/v1/microburst/summary | Get summary of microburst
[**nexus_insights_api_v1_microburst_top_bursts_get**](MicroburstApi.md#nexus_insights_api_v1_microburst_top_bursts_get) | **GET** /nexus/insights/api/v1/microburst/topBursts | Top microbursts based on peak or duration


# **nexus_insights_api_v1_microburst_queues_get**
> NexusInsightsApiV1MicroburstQueuesGet200Response nexus_insights_api_v1_microburst_queues_get()

Get interface queues

Get all queues in an interface for particular node and fabric name

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import microburst_api
from nexuscloud_client.model.nexus_insights_api_v1_microburst_queues_get200_response import NexusInsightsApiV1MicroburstQueuesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = microburst_api.MicroburstApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get interface queues
        api_response = api_instance.nexus_insights_api_v1_microburst_queues_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MicroburstApi->nexus_insights_api_v1_microburst_queues_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | defaults to "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | defaults to "None"
 **node_name** | **str**| Name of the fabric node - limit the records pertaining to given nodeName | defaults to "None"
 **interface_name** | **str**| Name of the node interface - limit the records pertaining to given interfaceName | defaults to "None"

### Return type

[**NexusInsightsApiV1MicroburstQueuesGet200Response**](NexusInsightsApiV1MicroburstQueuesGet200Response.md)

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

# **nexus_insights_api_v1_microburst_status_get**
> NexusInsightsApiV1MicroburstStatusGet200Response nexus_insights_api_v1_microburst_status_get()

Get microburst status of all fabrics

Get microburst status of all fabrics in the site group

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import microburst_api
from nexuscloud_client.model.nexus_insights_api_v1_microburst_status_get200_response import NexusInsightsApiV1MicroburstStatusGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = microburst_api.MicroburstApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get microburst status of all fabrics
        api_response = api_instance.nexus_insights_api_v1_microburst_status_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MicroburstApi->nexus_insights_api_v1_microburst_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | defaults to "None"

### Return type

[**NexusInsightsApiV1MicroburstStatusGet200Response**](NexusInsightsApiV1MicroburstStatusGet200Response.md)

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

# **nexus_insights_api_v1_microburst_summary_get**
> NexusInsightsApiV1MicroburstSummaryGet200Response nexus_insights_api_v1_microburst_summary_get()

Get summary of microburst

Get summary of microburst - count, avg and max peak, avg and max duration values per queue

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import microburst_api
from nexuscloud_client.model.nexus_insights_api_v1_microburst_summary_get200_response import NexusInsightsApiV1MicroburstSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = microburst_api.MicroburstApi(api_client)
    granularity = "2m" # str | Granularity of statistics in the response (optional) if omitted the server will use the default value of "1m"

    # example passing only required values which don't have defaults set
    try:
        # Get summary of microburst
        api_response = api_instance.nexus_insights_api_v1_microburst_summary_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MicroburstApi->nexus_insights_api_v1_microburst_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get summary of microburst
        api_response = api_instance.nexus_insights_api_v1_microburst_summary_get(granularity=granularity)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MicroburstApi->nexus_insights_api_v1_microburst_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | defaults to "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | defaults to "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | defaults to "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | defaults to "None"
 **node_name** | **str**| Name of the fabric node - limit the records pertaining to given nodeName | defaults to "None"
 **interface_name** | **str**| Name of the node interface - limit the records pertaining to given interfaceName | defaults to "None"
 **granularity** | **str**| Granularity of statistics in the response | [optional] if omitted the server will use the default value of "1m"

### Return type

[**NexusInsightsApiV1MicroburstSummaryGet200Response**](NexusInsightsApiV1MicroburstSummaryGet200Response.md)

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

# **nexus_insights_api_v1_microburst_top_bursts_get**
> NexusInsightsApiV1MicroburstTopBurstsGet200Response nexus_insights_api_v1_microburst_top_bursts_get()

Top microbursts based on peak or duration

Gives the top N microbursts at interface level based on peak or duration

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import microburst_api
from nexuscloud_client.model.nexus_insights_api_v1_microburst_top_bursts_get200_response import NexusInsightsApiV1MicroburstTopBurstsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = microburst_api.MicroburstApi(api_client)
    stat_name = "peak" # str | Stats type - either peak or duration (optional) if omitted the server will use the default value of "peak"
    queue_name = "queue-0" # str | Name of the interface queue - either a particular queueName or combination of all [queue-0, queue-1, ..., all] (optional) if omitted the server will use the default value of "all"
    count = 10 # int | Limits the number of entries (optional) if omitted the server will use the default value of 10
    offset = 0 # int | Pagination index into response. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Top microbursts based on peak or duration
        api_response = api_instance.nexus_insights_api_v1_microburst_top_bursts_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MicroburstApi->nexus_insights_api_v1_microburst_top_bursts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Top microbursts based on peak or duration
        api_response = api_instance.nexus_insights_api_v1_microburst_top_bursts_get(stat_name=stat_name, queue_name=queue_name, count=count, offset=offset)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MicroburstApi->nexus_insights_api_v1_microburst_top_bursts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | defaults to "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | defaults to "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | defaults to "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | defaults to "None"
 **node_name** | **str**| Name of the fabric node - limit the records pertaining to given nodeName | defaults to "None"
 **interface_name** | **str**| Name of the node interface - limit the records pertaining to given interfaceName | defaults to "None"
 **stat_name** | **str**| Stats type - either peak or duration | [optional] if omitted the server will use the default value of "peak"
 **queue_name** | **str**| Name of the interface queue - either a particular queueName or combination of all [queue-0, queue-1, ..., all] | [optional] if omitted the server will use the default value of "all"
 **count** | **int**| Limits the number of entries | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| Pagination index into response. | [optional] if omitted the server will use the default value of 0

### Return type

[**NexusInsightsApiV1MicroburstTopBurstsGet200Response**](NexusInsightsApiV1MicroburstTopBurstsGet200Response.md)

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

