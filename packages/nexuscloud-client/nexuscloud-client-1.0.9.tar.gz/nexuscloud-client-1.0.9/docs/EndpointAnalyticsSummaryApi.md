# nexuscloud_client.EndpointAnalyticsSummaryApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_endpoints_summary_get**](EndpointAnalyticsSummaryApi.md#nexus_insights_api_v1_endpoints_summary_get) | **GET** /nexus/insights/api/v1/endpoints/summary | Get the Endpoint Summary of entire fabric or given a condition


# **nexus_insights_api_v1_endpoints_summary_get**
> NexusInsightsApiV1EndpointsSummaryGet200Response nexus_insights_api_v1_endpoints_summary_get()

Get the Endpoint Summary of entire fabric or given a condition

Get the Endpoint Summary of entire fabric or given a condition

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import endpoint_analytics_summary_api
from nexuscloud_client.model.nexus_insights_api_v1_endpoints_summary_get200_response import NexusInsightsApiV1EndpointsSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoint_analytics_summary_api.EndpointAnalyticsSummaryApi(api_client)
    site_group_name = "DEFAULT" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "DEFAULT" # str | Name of the Site - limit the records pertaining to the site (optional)
    end_date = "2021-04-20T01:50:11-07:00" # str | End timestamp (optional) if omitted the server will use the default value of "now"
    filter = "interfaceName:po1" # str | Lucene format filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Endpoint Summary of entire fabric or given a condition
        api_response = api_instance.nexus_insights_api_v1_endpoints_summary_get(site_group_name=site_group_name, site_name=site_name, end_date=end_date, filter=filter)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling EndpointAnalyticsSummaryApi->nexus_insights_api_v1_endpoints_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **end_date** | **str**| End timestamp | [optional] if omitted the server will use the default value of "now"
 **filter** | **str**| Lucene format filter | [optional]

### Return type

[**NexusInsightsApiV1EndpointsSummaryGet200Response**](NexusInsightsApiV1EndpointsSummaryGet200Response.md)

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

