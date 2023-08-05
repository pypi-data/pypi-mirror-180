# nexuscloud_client.FabricFeatureApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_features_get**](FabricFeatureApi.md#nexus_insights_api_v1_features_get) | **GET** /nexus/insights/api/v1/features | Get the site features


# **nexus_insights_api_v1_features_get**
> {str: (NexusInsightsApiV1FeaturesGet200ResponseValue,)} nexus_insights_api_v1_features_get(site_name)

Get the site features

Get the list of features available for a given site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import fabric_feature_api
from nexuscloud_client.model.nexus_insights_api_v1_features_get200_response_value import NexusInsightsApiV1FeaturesGet200ResponseValue
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fabric_feature_api.FabricFeatureApi(api_client)
    site_name = "ifav-blr" # str | Name of the Site, Limit the records pertaining to this siteName

    # example passing only required values which don't have defaults set
    try:
        # Get the site features
        api_response = api_instance.nexus_insights_api_v1_features_get(site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling FabricFeatureApi->nexus_insights_api_v1_features_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Name of the Site, Limit the records pertaining to this siteName |

### Return type

[**{str: (NexusInsightsApiV1FeaturesGet200ResponseValue,)}**](NexusInsightsApiV1FeaturesGet200ResponseValue.md)

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

