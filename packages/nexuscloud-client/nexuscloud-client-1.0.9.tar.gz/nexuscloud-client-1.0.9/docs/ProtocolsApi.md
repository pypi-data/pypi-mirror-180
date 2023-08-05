# nexuscloud_client.ProtocolsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_bgp_details_get**](ProtocolsApi.md#nexus_insights_api_v1_bgp_details_get) | **GET** /nexus/insights/api/v1/bgp/details | BGP protocol details
[**nexus_insights_api_v1_igmp_details_get**](ProtocolsApi.md#nexus_insights_api_v1_igmp_details_get) | **GET** /nexus/insights/api/v1/igmp/details | IGMP protocol details
[**nexus_insights_api_v1_igmpsnoop_details_get**](ProtocolsApi.md#nexus_insights_api_v1_igmpsnoop_details_get) | **GET** /nexus/insights/api/v1/igmpsnoop/details | IGMP snoop protocol details
[**nexus_insights_api_v1_protocols_details_get**](ProtocolsApi.md#nexus_insights_api_v1_protocols_details_get) | **GET** /nexus/insights/api/v1/protocols/details | Get protocol details
[**nexus_insights_api_v1_protocols_top_entities_get**](ProtocolsApi.md#nexus_insights_api_v1_protocols_top_entities_get) | **GET** /nexus/insights/api/v1/protocols/topEntities | Protocol top entities
[**nexus_insights_api_v1_svi_details_get**](ProtocolsApi.md#nexus_insights_api_v1_svi_details_get) | **GET** /nexus/insights/api/v1/svi/details | IGMP protocol details
[**nexus_insights_api_v1_vpc_domains_get**](ProtocolsApi.md#nexus_insights_api_v1_vpc_domains_get) | **GET** /nexus/insights/api/v1/vpcDomains | Get VPC domain details


# **nexus_insights_api_v1_bgp_details_get**
> NexusInsightsApiV1BgpDetailsGet200Response nexus_insights_api_v1_bgp_details_get()

BGP protocol details

Get BGP protocol details based on given parameters such as fabric name, node name

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_bgp_details_get200_response import NexusInsightsApiV1BgpDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    node_name = "tel1-leaf1" # str | Node name - Gives bgp protocol details for this node (optional) if omitted the server will use the default value of "None"
    site_name = "DC-tel1" # str | Site name - Limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    vrf_name = "overlay-1" # str | Virtual routing and forwarding name - Limit the records pertaining to given vrf name (optional) if omitted the server will use the default value of "None"
    record_name = "nodeInfo" # str | Record type - Limit the records pertaining to this record type (optional) if omitted the server will use the default value of "None"
    sort = "+" # str | Order the records based on this field. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "None"
    filter_string = "protocolName:bgp AND nodeName:tel1-leaf1" # str | Lucene format filter - Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"
    end_date = "2021-03-29T08:18:55+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    start_date = "2021-03-29T08:03:55+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    count = 5 # int | Number of nodes in response (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Offset from which records are to be returned (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # BGP protocol details
        api_response = api_instance.nexus_insights_api_v1_bgp_details_get(node_name=node_name, site_name=site_name, vrf_name=vrf_name, record_name=record_name, sort=sort, filter_string=filter_string, end_date=end_date, start_date=start_date, count=count, offset=offset)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_bgp_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name - Gives bgp protocol details for this node | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Site name - Limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **vrf_name** | **str**| Virtual routing and forwarding name - Limit the records pertaining to given vrf name | [optional] if omitted the server will use the default value of "None"
 **record_name** | **str**| Record type - Limit the records pertaining to this record type | [optional] if omitted the server will use the default value of "None"
 **sort** | **str**| Order the records based on this field. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "None"
 **filter_string** | **str**| Lucene format filter - Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **count** | **int**| Number of nodes in response | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Offset from which records are to be returned | [optional] if omitted the server will use the default value of 0

### Return type

[**NexusInsightsApiV1BgpDetailsGet200Response**](NexusInsightsApiV1BgpDetailsGet200Response.md)

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

# **nexus_insights_api_v1_igmp_details_get**
> NexusInsightsApiV1IgmpDetailsGet200Response nexus_insights_api_v1_igmp_details_get(node_name, site_name, record_name)

IGMP protocol details

Get igmp protocol details based on given fabricname, nodename, recordname, end timestamp and start timestamp

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_igmp_details_get200_response import NexusInsightsApiV1IgmpDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    node_name = "tel1-leaf1" # str | Node name - limit the records pertaining to given node name
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name
    record_name = "igmpOIF" # str | Record name - limit the records pertaining to given record type
    site_group_name = "BANGALORE" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    sort = "+nodeName" # str | Sort results by event type/severity. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "None"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End timestamp, to collect the records generated till specified time (optional) if omitted the server will use the default value of "now"
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start timestamp, to skip records generated earlier to this timestamp (optional) if omitted the server will use the default value of "now-1h"
    count = 5 # int | Limit the number of entries in response (optional) if omitted the server will use the default value of 10
    offset = 0 # int | Pagination index into response (optional) if omitted the server will use the default value of 0
    filter = "None" # str | Lucene format filter - Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # IGMP protocol details
        api_response = api_instance.nexus_insights_api_v1_igmp_details_get(node_name, site_name, record_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_igmp_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # IGMP protocol details
        api_response = api_instance.nexus_insights_api_v1_igmp_details_get(node_name, site_name, record_name, site_group_name=site_group_name, sort=sort, end_date=end_date, start_date=start_date, count=count, offset=offset, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_igmp_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name - limit the records pertaining to given node name |
 **site_name** | **str**| Site name - limit the records pertaining to given site name |
 **record_name** | **str**| Record name - limit the records pertaining to given record type |
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **sort** | **str**| Sort results by event type/severity. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End timestamp, to collect the records generated till specified time | [optional] if omitted the server will use the default value of "now"
 **start_date** | **str**| Start timestamp, to skip records generated earlier to this timestamp | [optional] if omitted the server will use the default value of "now-1h"
 **count** | **int**| Limit the number of entries in response | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| Pagination index into response | [optional] if omitted the server will use the default value of 0
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1IgmpDetailsGet200Response**](NexusInsightsApiV1IgmpDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IGMP Details |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_igmpsnoop_details_get**
> NexusInsightsApiV1IgmpsnoopDetailsGet200Response nexus_insights_api_v1_igmpsnoop_details_get(node_name, site_name, record_name)

IGMP snoop protocol details

Get igmp snoop protocol details based on given fabricname, nodename, recordname, end timestamp and start timestamp

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_igmpsnoop_details_get200_response import NexusInsightsApiV1IgmpsnoopDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    node_name = "tel1-leaf1" # str | Node name - limit the records pertaining to given node name
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given siteName
    record_name = "igmpsnoopInst" # str | Record name - limit the records pertaining to given record type
    sort = "+nodeName" # str | Order the response based on this field. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "None"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    count = 5 # int | Limit the number of entries in response (optional) if omitted the server will use the default value of 10
    offset = 0 # int | Pagination index into response (optional) if omitted the server will use the default value of 0
    filter_string = "statName:igmp AND nodeName:tel1-leaf1" # str | Lucene format filter - Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # IGMP snoop protocol details
        api_response = api_instance.nexus_insights_api_v1_igmpsnoop_details_get(node_name, site_name, record_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_igmpsnoop_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # IGMP snoop protocol details
        api_response = api_instance.nexus_insights_api_v1_igmpsnoop_details_get(node_name, site_name, record_name, sort=sort, end_date=end_date, start_date=start_date, count=count, offset=offset, filter_string=filter_string)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_igmpsnoop_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name - limit the records pertaining to given node name |
 **site_name** | **str**| Site name - limit the records pertaining to given siteName |
 **record_name** | **str**| Record name - limit the records pertaining to given record type |
 **sort** | **str**| Order the response based on this field. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **count** | **int**| Limit the number of entries in response | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| Pagination index into response | [optional] if omitted the server will use the default value of 0
 **filter_string** | **str**| Lucene format filter - Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1IgmpsnoopDetailsGet200Response**](NexusInsightsApiV1IgmpsnoopDetailsGet200Response.md)

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

# **nexus_insights_api_v1_protocols_details_get**
> NexusInsightsApiV1ProtocolsDetailsGet200Response nexus_insights_api_v1_protocols_details_get()

Get protocol details

Get telemetry protocol stats details for interfaces present in a given fabric

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_protocols_details_get200_response import NexusInsightsApiV1ProtocolsDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    start_date = "2021-03-29T08:03:55+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-29T08:18:55+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given siteName (optional) if omitted the server will use the default value of "None"
    node_name = "tel1-leaf1" # str | Node name - limit the records pertaining to given node name (optional) if omitted the server will use the default value of "None"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    stat_name = "interface" # str | Limit the records based on given statName (optional) if omitted the server will use the default value of "None"
    history = 1 # int | Defines whether records need to be added with timeseries or not in response (optional) if omitted the server will use the default value of 0
    filter = "nodeName:tel1-leaf1" # str | Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"
    filter_l2_neighbors = "peerDeviceName:tel2-n3k-1" # str | Filter the l2neighbors list in response based on this field (optional) if omitted the server will use the default value of "None"
    count = 5 # int | Limit the number of entries in response (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Offset from which records are to be returned (optional) if omitted the server will use the default value of 0
    granularity = "1m" # str | Granularity of the values w.r.t duration : mandatory when history is 1 (optional) if omitted the server will use the default value of "None"
    sort = "-anomalyScore" # str | Order the records based on this field. Use +/- as prefix for ascending/descending order (optional) if omitted the server will use the default value of "nodeName"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get protocol details
        api_response = api_instance.nexus_insights_api_v1_protocols_details_get(start_date=start_date, end_date=end_date, site_name=site_name, node_name=node_name, site_group_name=site_group_name, stat_name=stat_name, history=history, filter=filter, filter_l2_neighbors=filter_l2_neighbors, count=count, offset=offset, granularity=granularity, sort=sort)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_protocols_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_name** | **str**| Site name - limit the records pertaining to given siteName | [optional] if omitted the server will use the default value of "None"
 **node_name** | **str**| Node name - limit the records pertaining to given node name | [optional] if omitted the server will use the default value of "None"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **stat_name** | **str**| Limit the records based on given statName | [optional] if omitted the server will use the default value of "None"
 **history** | **int**| Defines whether records need to be added with timeseries or not in response | [optional] if omitted the server will use the default value of 0
 **filter** | **str**| Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"
 **filter_l2_neighbors** | **str**| Filter the l2neighbors list in response based on this field | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limit the number of entries in response | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Offset from which records are to be returned | [optional] if omitted the server will use the default value of 0
 **granularity** | **str**| Granularity of the values w.r.t duration : mandatory when history is 1 | [optional] if omitted the server will use the default value of "None"
 **sort** | **str**| Order the records based on this field. Use +/- as prefix for ascending/descending order | [optional] if omitted the server will use the default value of "nodeName"

### Return type

[**NexusInsightsApiV1ProtocolsDetailsGet200Response**](NexusInsightsApiV1ProtocolsDetailsGet200Response.md)

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

# **nexus_insights_api_v1_protocols_top_entities_get**
> NexusInsightsApiV1ProtocolsTopEntitiesGet200Response nexus_insights_api_v1_protocols_top_entities_get()

Protocol top entities

Get interface top entries based on various counters such as error, transmit utilization, receive utilization

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_protocols_top_entities_get200_response import NexusInsightsApiV1ProtocolsTopEntitiesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name (optional) if omitted the server will use the default value of "None"
    node_name = "tel1-leaf1" # str | Node name - limit the records pertaining to given node name (optional) if omitted the server will use the default value of "None"
    site_group_name = "ifav-insight" # str | Name of Site Group, limit the records pertaining to the sites in this siteGroupName (optional) if omitted the server will use the default value of "None"
    filter = "nodeName:tel1-leaf1" # str | Lucene format filter - Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"
    start_date = "2021-03-29T08:03:55+05:30" # str | Start timestamp, to skip records generated earlier to this timestamp (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-29T08:18:55+05:30" # str | End timestamp, to collect the records generated till specified time (optional) if omitted the server will use the default value of "now"
    count = 5 # int | Limit the number of entries in response (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Offset from which records are to be returned (optional) if omitted the server will use the default value of 0
    granularity = "1m" # str | Granularity of the values w.r.t duration, mandatory when history is 1 (optional) if omitted the server will use the default value of "5m"
    history = 1 # int | Defines whether records need to be added with timeseries or not in response (optional) if omitted the server will use the default value of 0
    stat_name = "interface:utilization:egress" # str | Limit the records based on given statName (optional) if omitted the server will use the default value of "interface:total:intferrors"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Protocol top entities
        api_response = api_instance.nexus_insights_api_v1_protocols_top_entities_get(site_name=site_name, node_name=node_name, site_group_name=site_group_name, filter=filter, start_date=start_date, end_date=end_date, count=count, offset=offset, granularity=granularity, history=history, stat_name=stat_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_protocols_top_entities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Site name - limit the records pertaining to given site name | [optional] if omitted the server will use the default value of "None"
 **node_name** | **str**| Node name - limit the records pertaining to given node name | [optional] if omitted the server will use the default value of "None"
 **site_group_name** | **str**| Name of Site Group, limit the records pertaining to the sites in this siteGroupName | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"
 **start_date** | **str**| Start timestamp, to skip records generated earlier to this timestamp | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End timestamp, to collect the records generated till specified time | [optional] if omitted the server will use the default value of "now"
 **count** | **int**| Limit the number of entries in response | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Offset from which records are to be returned | [optional] if omitted the server will use the default value of 0
 **granularity** | **str**| Granularity of the values w.r.t duration, mandatory when history is 1 | [optional] if omitted the server will use the default value of "5m"
 **history** | **int**| Defines whether records need to be added with timeseries or not in response | [optional] if omitted the server will use the default value of 0
 **stat_name** | **str**| Limit the records based on given statName | [optional] if omitted the server will use the default value of "interface:total:intferrors"

### Return type

[**NexusInsightsApiV1ProtocolsTopEntitiesGet200Response**](NexusInsightsApiV1ProtocolsTopEntitiesGet200Response.md)

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

# **nexus_insights_api_v1_svi_details_get**
> NexusInsightsApiV1SviDetailsGet200Response nexus_insights_api_v1_svi_details_get(node_name, site_name, )

IGMP protocol details

Get igmp protocol details based on given fabricname, nodename, recordname, end timestamp and start timestamp

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_svi_details_get200_response import NexusInsightsApiV1SviDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    node_name = "tel1-leaf1" # str | Node name - limit the records pertaining to given node name
    site_name = "DC-tel1" # str | Site name - limit the records pertaining to given site name
    site_group_name = "BANGALORE" # str | Name of Site Group, limit the records pertaining to the sites in this siteGroupName (optional)
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End timestamp, to collect the records generated till specified time (optional) if omitted the server will use the default value of "now"
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start timestamp, to skip records generated earlier to this timestamp (optional) if omitted the server will use the default value of "now-1h"
    interface_type = "svi" # str | Interface type - limit the records pertaining to the given interfaceType (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # IGMP protocol details
        api_response = api_instance.nexus_insights_api_v1_svi_details_get(node_name, site_name, )
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_svi_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # IGMP protocol details
        api_response = api_instance.nexus_insights_api_v1_svi_details_get(node_name, site_name, site_group_name=site_group_name, end_date=end_date, start_date=start_date, interface_type=interface_type)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_svi_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name - limit the records pertaining to given node name |
 **site_name** | **str**| Site name - limit the records pertaining to given site name |
 **interface_name** | **str**| Name of the node interface - limit the records pertaining to given interfaceName | defaults to "None"
 **site_group_name** | **str**| Name of Site Group, limit the records pertaining to the sites in this siteGroupName | [optional]
 **end_date** | **str**| End timestamp, to collect the records generated till specified time | [optional] if omitted the server will use the default value of "now"
 **start_date** | **str**| Start timestamp, to skip records generated earlier to this timestamp | [optional] if omitted the server will use the default value of "now-1h"
 **interface_type** | **str**| Interface type - limit the records pertaining to the given interfaceType | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SviDetailsGet200Response**](NexusInsightsApiV1SviDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Svi Details |  * date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_vpc_domains_get**
> NexusInsightsApiV1VpcDomainsGet200Response nexus_insights_api_v1_vpc_domains_get()

Get VPC domain details

Get VPC domain details in a given fabric

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import protocols_api
from nexuscloud_client.model.nexus_insights_api_v1_vpc_domains_get200_response import NexusInsightsApiV1VpcDomainsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = protocols_api.ProtocolsApi(api_client)
    end_date = "2021-03-29T08:18:55+05:30" # str | End timestamp, to collect the records generated till specified time (optional) if omitted the server will use the default value of "now"
    site_name = "DC-tel1" # str | site name - limit the records pertaining to given site name (optional) if omitted the server will use the default value of "None"
    site_group_name = "Ig1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    sort = "-domainId" # str | Order the response based on this field (optional) if omitted the server will use the default value of "None"
    filter = "domainId:100" # str | Filter the response based on this filter field (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get VPC domain details
        api_response = api_instance.nexus_insights_api_v1_vpc_domains_get(end_date=end_date, site_name=site_name, site_group_name=site_group_name, sort=sort, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ProtocolsApi->nexus_insights_api_v1_vpc_domains_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End timestamp, to collect the records generated till specified time | [optional] if omitted the server will use the default value of "now"
 **site_name** | **str**| site name - limit the records pertaining to given site name | [optional] if omitted the server will use the default value of "None"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **sort** | **str**| Order the response based on this field | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Filter the response based on this filter field | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1VpcDomainsGet200Response**](NexusInsightsApiV1VpcDomainsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Records list |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

