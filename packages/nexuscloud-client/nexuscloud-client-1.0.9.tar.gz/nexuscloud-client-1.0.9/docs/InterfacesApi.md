# nexuscloud_client.InterfacesApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_interfaces_summary_get**](InterfacesApi.md#nexus_insights_api_v1_interfaces_summary_get) | **GET** /nexus/insights/api/v1/interfaces/summary | Get Interface Summary
[**nexus_insights_api_v1_l3neighbors_get**](InterfacesApi.md#nexus_insights_api_v1_l3neighbors_get) | **GET** /nexus/insights/api/v1/l3neighbors | Get l3neighborsSummary Summary
[**nexus_insights_api_v1_northsouth_traffic_summary_get**](InterfacesApi.md#nexus_insights_api_v1_northsouth_traffic_summary_get) | **GET** /nexus/insights/api/v1/northsouthTraffic/summary | Get NorthSouthTraffic Summary


# **nexus_insights_api_v1_interfaces_summary_get**
> NexusInsightsApiV1InterfacesSummaryGet200Response nexus_insights_api_v1_interfaces_summary_get()

Get Interface Summary

Get the interfaces stats and their status

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import interfaces_api
from nexuscloud_client.model.nexus_insights_api_v1_interfaces_summary_get200_response import NexusInsightsApiV1InterfacesSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interfaces_api.InterfacesApi(api_client)
    start_date = "2021-03-26T09:14:54.940+05:30" # str | Start Date, to collect the records from the specified date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End Date, to collect the records at the specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name (optional) if omitted the server will use the default value of "None"
    interface_type = "physical,pc" # str | Interface type - limit the records pertaining to the given interfaceType (optional) if omitted the server will use the default value of "None"
    filter = "nodeName:tel1-leaf1" # str | Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Interface Summary
        api_response = api_instance.nexus_insights_api_v1_interfaces_summary_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, interface_type=interface_type, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling InterfacesApi->nexus_insights_api_v1_interfaces_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start Date, to collect the records from the specified date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End Date, to collect the records at the specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Site name - limit the records pertaining to given site name | [optional] if omitted the server will use the default value of "None"
 **interface_type** | **str**| Interface type - limit the records pertaining to the given interfaceType | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1InterfacesSummaryGet200Response**](NexusInsightsApiV1InterfacesSummaryGet200Response.md)

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

# **nexus_insights_api_v1_l3neighbors_get**
> NexusInsightsApiV1L3neighborsGet200Response nexus_insights_api_v1_l3neighbors_get()

Get l3neighborsSummary Summary

Get l3neighborsSummary Summary

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import interfaces_api
from nexuscloud_client.model.nexus_insights_api_v1_l3neighbors_get200_response import NexusInsightsApiV1L3neighborsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interfaces_api.InterfacesApi(api_client)
    start_date = "2021-03-26T10:14:54.940+05:30" # str | Start Date, to collect the records from the specified date (optional) if omitted the server will use the default value of "now -1h"
    neighbor_operst = "active" # str | neighbor operst filter - limit the records pertaining to given operst (optional)
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End Date, to collect the records at the specified date (optional) if omitted the server will use the default value of "now"
    sort = "-nodeName" # str | Order the response based on this field (optional) if omitted the server will use the default value of "None"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name (optional) if omitted the server will use the default value of "None"
    filter = "nodeName:tel1-leaf1" # str | Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"
    count = 10 # int | Limit the number of entries in response (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination index into response (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get l3neighborsSummary Summary
        api_response = api_instance.nexus_insights_api_v1_l3neighbors_get(start_date=start_date, neighbor_operst=neighbor_operst, end_date=end_date, sort=sort, site_group_name=site_group_name, site_name=site_name, filter=filter, count=count, offset=offset)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling InterfacesApi->nexus_insights_api_v1_l3neighbors_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start Date, to collect the records from the specified date | [optional] if omitted the server will use the default value of "now -1h"
 **neighbor_operst** | **str**| neighbor operst filter - limit the records pertaining to given operst | [optional]
 **end_date** | **str**| End Date, to collect the records at the specified date | [optional] if omitted the server will use the default value of "now"
 **sort** | **str**| Order the response based on this field | [optional] if omitted the server will use the default value of "None"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Site name - limit the records pertaining to given site name | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limit the number of entries in response | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination index into response | [optional] if omitted the server will use the default value of 0

### Return type

[**NexusInsightsApiV1L3neighborsGet200Response**](NexusInsightsApiV1L3neighborsGet200Response.md)

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

# **nexus_insights_api_v1_northsouth_traffic_summary_get**
> NexusInsightsApiV1NorthsouthTrafficSummaryGet200Response nexus_insights_api_v1_northsouth_traffic_summary_get()

Get NorthSouthTraffic Summary

Get NorthSouthTraffic Summary

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import interfaces_api
from nexuscloud_client.model.nexus_insights_api_v1_northsouth_traffic_summary_get200_response import NexusInsightsApiV1NorthsouthTrafficSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interfaces_api.InterfacesApi(api_client)
    start_date = "2021-03-26T10:14:54.940+05:30" # str | Start Date, to collect the records from the specified date (optional) if omitted the server will use the default value of "now -1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End Date, to collect the records at the specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name (optional) if omitted the server will use the default value of "None"
    granularity = "3h" # str | Granularity of the values w.r.t duration (optional) if omitted the server will use the default value of "5m"
    history = "1" # str | Require the timeseries data or not (optional) if omitted the server will use the default value of "0"
    filter = "nodeName:tel1-leaf1" # str | Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get NorthSouthTraffic Summary
        api_response = api_instance.nexus_insights_api_v1_northsouth_traffic_summary_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, granularity=granularity, history=history, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling InterfacesApi->nexus_insights_api_v1_northsouth_traffic_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start Date, to collect the records from the specified date | [optional] if omitted the server will use the default value of "now -1h"
 **end_date** | **str**| End Date, to collect the records at the specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Site name - limit the records pertaining to given site name | [optional] if omitted the server will use the default value of "None"
 **granularity** | **str**| Granularity of the values w.r.t duration | [optional] if omitted the server will use the default value of "5m"
 **history** | **str**| Require the timeseries data or not | [optional] if omitted the server will use the default value of "0"
 **filter** | **str**| Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1NorthsouthTrafficSummaryGet200Response**](NexusInsightsApiV1NorthsouthTrafficSummaryGet200Response.md)

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

