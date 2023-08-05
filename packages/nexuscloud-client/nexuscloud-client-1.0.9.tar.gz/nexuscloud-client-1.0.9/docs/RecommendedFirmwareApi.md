# nexuscloud_client.RecommendedFirmwareApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_firmware_analysis_recommended_firmware_get**](RecommendedFirmwareApi.md#nexus_insights_api_v1_firmware_analysis_recommended_firmware_get) | **GET** /nexus/insights/api/v1/firmwareAnalysis/recommendedFirmware | Get the Recommended firmware path for the given recommendation Ids


# **nexus_insights_api_v1_firmware_analysis_recommended_firmware_get**
> NexusInsightsApiV1FirmwareAnalysisRecommendedFirmwareGet200Response nexus_insights_api_v1_firmware_analysis_recommended_firmware_get(recommendation_id, )

Get the Recommended firmware path for the given recommendation Ids

Get the Recommended firmware path for the given recommendation Ids

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import recommended_firmware_api
from nexuscloud_client.model.nexus_insights_api_v1_firmware_analysis_recommended_firmware_get200_response import NexusInsightsApiV1FirmwareAnalysisRecommendedFirmwareGet200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recommended_firmware_api.RecommendedFirmwareApi(api_client)
    recommendation_id = ["rec1","rec2"] # [str] | Applicable Recommendation ID
    site_group_name = "ifav-insight" # str | Name of Insights Group, limit the records pertaining to the sites in this siteGroupName (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get the Recommended firmware path for the given recommendation Ids
        api_response = api_instance.nexus_insights_api_v1_firmware_analysis_recommended_firmware_get(recommendation_id, )
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling RecommendedFirmwareApi->nexus_insights_api_v1_firmware_analysis_recommended_firmware_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Recommended firmware path for the given recommendation Ids
        api_response = api_instance.nexus_insights_api_v1_firmware_analysis_recommended_firmware_get(recommendation_id, site_group_name=site_group_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling RecommendedFirmwareApi->nexus_insights_api_v1_firmware_analysis_recommended_firmware_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_id** | **[str]**| Applicable Recommendation ID |
 **site_name** | **str**| Name of the Fabric, Limit the records pertaining to this siteName | defaults to "None"
 **site_group_name** | **str**| Name of Insights Group, limit the records pertaining to the sites in this siteGroupName | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1FirmwareAnalysisRecommendedFirmwareGet200Response**](NexusInsightsApiV1FirmwareAnalysisRecommendedFirmwareGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

