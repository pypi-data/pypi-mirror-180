# nexuscloud_client.PortChannelApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_portchannel_details_get**](PortChannelApi.md#nexus_insights_api_v1_portchannel_details_get) | **GET** /nexus/insights/api/v1/portchannel/details | Port channel details


# **nexus_insights_api_v1_portchannel_details_get**
> NexusInsightsApiV1PortchannelDetailsGet200Response nexus_insights_api_v1_portchannel_details_get(site_name)

Port channel details

Get port channel protocol details

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import port_channel_api
from nexuscloud_client.model.nexus_insights_api_v1_portchannel_details_get200_response import NexusInsightsApiV1PortchannelDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = port_channel_api.PortChannelApi(api_client)
    site_name = "DC-tel1" # str | Site Name - limit the records pertaining to given siteName
    node_name = "tel1-leaf1" # str | Node name - limit the records pertaining to given node name (optional) if omitted the server will use the default value of "None"
    name = "accBndlGrp_101_pc11" # str | Portchannel interface name (optional) if omitted the server will use the default value of "None"
    pc_type = "pc" # str | Port channel type (optional) if omitted the server will use the default value of "pc"
    sort = "+nodeName" # str | Order the response based on this field. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "None"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    count = 10 # int | Limit the number of entries in response (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination index into response (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Port channel details
        api_response = api_instance.nexus_insights_api_v1_portchannel_details_get(site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling PortChannelApi->nexus_insights_api_v1_portchannel_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Port channel details
        api_response = api_instance.nexus_insights_api_v1_portchannel_details_get(site_name, node_name=node_name, name=name, pc_type=pc_type, sort=sort, end_date=end_date, start_date=start_date, count=count, offset=offset)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling PortChannelApi->nexus_insights_api_v1_portchannel_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Site Name - limit the records pertaining to given siteName |
 **node_name** | **str**| Node name - limit the records pertaining to given node name | [optional] if omitted the server will use the default value of "None"
 **name** | **str**| Portchannel interface name | [optional] if omitted the server will use the default value of "None"
 **pc_type** | **str**| Port channel type | [optional] if omitted the server will use the default value of "pc"
 **sort** | **str**| Order the response based on this field. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **count** | **int**| Limit the number of entries in response | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination index into response | [optional] if omitted the server will use the default value of 0

### Return type

[**NexusInsightsApiV1PortchannelDetailsGet200Response**](NexusInsightsApiV1PortchannelDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Records list |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

