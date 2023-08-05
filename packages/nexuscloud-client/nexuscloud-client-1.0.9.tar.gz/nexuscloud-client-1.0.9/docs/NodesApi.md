# nexuscloud_client.NodesApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_jobs_node_states_get**](NodesApi.md#nexus_insights_api_v1_jobs_node_states_get) | **GET** /nexus/insights/api/v1/jobs/nodeStates | Node state of fabric nodes
[**nexus_insights_api_v1_node_capabilities_get**](NodesApi.md#nexus_insights_api_v1_node_capabilities_get) | **GET** /nexus/insights/api/v1/nodeCapabilities | Get the features available on the node
[**nexus_insights_api_v1_nodes_get**](NodesApi.md#nexus_insights_api_v1_nodes_get) | **GET** /nexus/insights/api/v1/nodes | Get nodes list


# **nexus_insights_api_v1_jobs_node_states_get**
> NexusInsightsApiV1JobsNodeStatesGet200Response nexus_insights_api_v1_jobs_node_states_get(site_group_name, site_name)

Node state of fabric nodes

Gives the node state details of the fabric nodes

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import nodes_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_jobs_node_states_get200_response import NexusInsightsApiV1JobsNodeStatesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)
    site_group_name = "ifav-insight" # str | Limit the records pertaining to this siteGroupName
    site_name = "ifav-blr3" # str | Limit the records pertaining to this siteName
    job_type = "LOG,TACASSIST,COMPLIANCE" # str | Comma separated list of job types w.r.t which node state is to be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # Node state of fabric nodes
        api_response = api_instance.nexus_insights_api_v1_jobs_node_states_get(site_group_name, site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling NodesApi->nexus_insights_api_v1_jobs_node_states_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Node state of fabric nodes
        api_response = api_instance.nexus_insights_api_v1_jobs_node_states_get(site_group_name, site_name, job_type=job_type)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling NodesApi->nexus_insights_api_v1_jobs_node_states_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Limit the records pertaining to this siteGroupName |
 **site_name** | **str**| Limit the records pertaining to this siteName |
 **job_type** | **str**| Comma separated list of job types w.r.t which node state is to be returned | [optional]

### Return type

[**NexusInsightsApiV1JobsNodeStatesGet200Response**](NexusInsightsApiV1JobsNodeStatesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nodes list |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_node_capabilities_get**
> {str: (NexusInsightsApiV1NodeCapabilitiesGet200ResponseValue,)} nexus_insights_api_v1_node_capabilities_get(site_name, node_name)

Get the features available on the node

Get the list of features available for a given node

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import nodes_api
from nexuscloud_client.model.nexus_insights_api_v1_node_capabilities_get200_response_value import NexusInsightsApiV1NodeCapabilitiesGet200ResponseValue
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)
    site_name = "ifav-blr" # str | Name of the Site, Limit the records pertaining to this siteName
    node_name = "ifav-leaf1" # str | Name of the site node, limits the capabilites to given nodeName

    # example passing only required values which don't have defaults set
    try:
        # Get the features available on the node
        api_response = api_instance.nexus_insights_api_v1_node_capabilities_get(site_name, node_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling NodesApi->nexus_insights_api_v1_node_capabilities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Name of the Site, Limit the records pertaining to this siteName |
 **node_name** | **str**| Name of the site node, limits the capabilites to given nodeName |

### Return type

[**{str: (NexusInsightsApiV1NodeCapabilitiesGet200ResponseValue,)}**](NexusInsightsApiV1NodeCapabilitiesGet200ResponseValue.md)

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

# **nexus_insights_api_v1_nodes_get**
> NexusInsightsApiV1NodesGet200Response nexus_insights_api_v1_nodes_get()

Get nodes list

Get detailed info of nodes

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import nodes_api
from nexuscloud_client.model.nexus_insights_api_v1_nodes_get200_response import NexusInsightsApiV1NodesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start date, to skip records generated earlier to this date (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End date, to collect the records generated till specified date (optional) if omitted the server will use the default value of "now"
    site_group_name = "ifav-insight" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional) if omitted the server will use the default value of "None"
    site_name = "ifav-blr3" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    node_names = "ifav-blr2-ifc1,ifav-blr2-ifc2" # str | List of comma separated nodeNames - limit the records pertaining to these nodeNames (optional) if omitted the server will use the default value of "None"
    node_roles = "Controller,Leaf" # str | List of comma separated types of node (optional) if omitted the server will use the default value of "None"
    filter = "None" # str | Lucene format filter (optional) if omitted the server will use the default value of "None"
    include = "anomalyScore" # str | Include Anomaly Scores field in nodes output (optional) if omitted the server will use the default value of "None"
    count = 8 # int | Limits the number of records in the response (optional) if omitted the server will use the default value of 10
    oper_st = "None" # str | Comma separated list of operSt - limit the records pertaining to this operSt (optional) if omitted the server will use the default value of "None"
    include_crv = False # bool | Display Cisco Recommended Version (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get nodes list
        api_response = api_instance.nexus_insights_api_v1_nodes_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, site_name=site_name, node_names=node_names, node_roles=node_roles, filter=filter, include=include, count=count, oper_st=oper_st, include_crv=include_crv)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling NodesApi->nexus_insights_api_v1_nodes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **node_names** | **str**| List of comma separated nodeNames - limit the records pertaining to these nodeNames | [optional] if omitted the server will use the default value of "None"
 **node_roles** | **str**| List of comma separated types of node | [optional] if omitted the server will use the default value of "None"
 **filter** | **str**| Lucene format filter | [optional] if omitted the server will use the default value of "None"
 **include** | **str**| Include Anomaly Scores field in nodes output | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limits the number of records in the response | [optional] if omitted the server will use the default value of 10
 **oper_st** | **str**| Comma separated list of operSt - limit the records pertaining to this operSt | [optional] if omitted the server will use the default value of "None"
 **include_crv** | **bool**| Display Cisco Recommended Version | [optional] if omitted the server will use the default value of False

### Return type

[**NexusInsightsApiV1NodesGet200Response**](NexusInsightsApiV1NodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nodes list |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

