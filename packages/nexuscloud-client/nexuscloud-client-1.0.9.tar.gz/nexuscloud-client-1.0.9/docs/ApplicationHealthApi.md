# nexuscloud_client.ApplicationHealthApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_health_collection_stats_get**](ApplicationHealthApi.md#nexus_insights_api_v1_health_collection_stats_get) | **GET** /nexus/insights/api/v1/health/collectionStats | Get collection status for last hour, status of bug scan and best practices(NX/DCNM) run for the devices


# **nexus_insights_api_v1_health_collection_stats_get**
> NexusInsightsApiV1HealthCollectionStatsGet200Response nexus_insights_api_v1_health_collection_stats_get()

Get collection status for last hour, status of bug scan and best practices(NX/DCNM) run for the devices

Get the collection pipeline for each of the following - Resource Utilization, Environmental, Statistics, Flows, Endpoint, Events for each node for last hour. Get the status of bug scan and best practices(NX/DCNM) run for the devices

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import application_health_api
from nexuscloud_client.model.nexus_insights_api_v1_health_collection_stats_get200_response import NexusInsightsApiV1HealthCollectionStatsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_health_api.ApplicationHealthApi(api_client)
    site_group_name = "swmp3-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "ifav-blr3" # str | Name of the Site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection status for last hour, status of bug scan and best practices(NX/DCNM) run for the devices
        api_response = api_instance.nexus_insights_api_v1_health_collection_stats_get(site_group_name=site_group_name, site_name=site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ApplicationHealthApi->nexus_insights_api_v1_health_collection_stats_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1HealthCollectionStatsGet200Response**](NexusInsightsApiV1HealthCollectionStatsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection Status for last hour |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

