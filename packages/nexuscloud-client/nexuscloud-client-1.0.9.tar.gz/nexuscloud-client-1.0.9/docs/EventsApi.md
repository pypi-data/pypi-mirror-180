# nexuscloud_client.EventsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_events_buckets_get**](EventsApi.md#nexus_insights_api_v1_events_buckets_get) | **GET** /nexus/insights/api/v1/events/buckets | Events buckets
[**nexus_insights_api_v1_events_details_get**](EventsApi.md#nexus_insights_api_v1_events_details_get) | **GET** /nexus/insights/api/v1/events/details | Events details
[**nexus_insights_api_v1_events_summary_get**](EventsApi.md#nexus_insights_api_v1_events_summary_get) | **GET** /nexus/insights/api/v1/events/summary | Events summary


# **nexus_insights_api_v1_events_buckets_get**
> NexusInsightsApiV1EventsBucketsGet200Response nexus_insights_api_v1_events_buckets_get()

Events buckets

Get the count of Audit Logs, Events and Faults event types in time series pattern within the specified time period

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import events_api
from nexuscloud_client.model.nexus_insights_api_v1_events_buckets_get200_response import NexusInsightsApiV1EventsBucketsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr3" # str | Name of the Site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    granularity = "5m" # str | The samples interval time (optional) if omitted the server will use the default value of "5m"
    filter = "eventType:AuditLog AND severity:major" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Events buckets
        api_response = api_instance.nexus_insights_api_v1_events_buckets_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, granularity=granularity, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EventsApi->nexus_insights_api_v1_events_buckets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **granularity** | **str**| The samples interval time | [optional] if omitted the server will use the default value of "5m"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1EventsBucketsGet200Response**](NexusInsightsApiV1EventsBucketsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Buckets of Audit Logs, Events and Faults event types |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_events_details_get**
> NexusInsightsApiV1EventsDetailsGet200Response nexus_insights_api_v1_events_details_get()

Events details

Get the detailed info for Audit Logs, Events and Faults event types within the specified time period

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import events_api
from nexuscloud_client.model.nexus_insights_api_v1_events_details_get200_response import NexusInsightsApiV1EventsDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr3" # str | Name of the Site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    filter = "eventType:AuditLog AND severity:major" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"
    offset = 10 # int | Offset from which records are to be returned (optional) if omitted the server will use the default value of 0
    sort = "-severity" # str | Sort results by event type/severity. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "None"
    count = 8 # int | Limits the number of records in the response (optional) if omitted the server will use the default value of 10
    event_type = "None" # str | Type of event (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Events details
        api_response = api_instance.nexus_insights_api_v1_events_details_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, filter=filter, offset=offset, sort=sort, count=count, event_type=event_type)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EventsApi->nexus_insights_api_v1_events_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"
 **offset** | **int**| Offset from which records are to be returned | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| Sort results by event type/severity. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limits the number of records in the response | [optional] if omitted the server will use the default value of 10
 **event_type** | **str**| Type of event | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1EventsDetailsGet200Response**](NexusInsightsApiV1EventsDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Audit Logs, Events and Faults event types |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_events_summary_get**
> NexusInsightsApiV1EventsSummaryGet200Response nexus_insights_api_v1_events_summary_get()

Events summary

Get the severity/action count for Audit Logs, Events and Faults event types within the specified time period

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import events_api
from nexuscloud_client.model.nexus_insights_api_v1_events_summary_get200_response import NexusInsightsApiV1EventsSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr3" # str | Name of the Site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    node_name = "ifav-leaf1" # str | Name of the node - limit the records pertaining to this nodeName (optional) if omitted the server will use the default value of "None"
    filter = "eventType:AuditLog AND severity:major" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Events summary
        api_response = api_instance.nexus_insights_api_v1_events_summary_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, node_name=node_name, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EventsApi->nexus_insights_api_v1_events_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the Site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **node_name** | **str**| Name of the node - limit the records pertaining to this nodeName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1EventsSummaryGet200Response**](NexusInsightsApiV1EventsSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of Audit Logs, Events and Faults event types |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

