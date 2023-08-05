# nexuscloud_client.MetadataApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_metadata_cloud_sync_post**](MetadataApi.md#nexus_insights_api_v1_metadata_cloud_sync_post) | **POST** /nexus/insights/api/v1/metadata/cloudSync | Update to Latest Metadata
[**nexus_insights_api_v1_metadata_latest_get**](MetadataApi.md#nexus_insights_api_v1_metadata_latest_get) | **GET** /nexus/insights/api/v1/metadata/latest | Get Latest Metadata


# **nexus_insights_api_v1_metadata_cloud_sync_post**
> NexusInsightsApiV1MetadataCloudSyncPost200Response nexus_insights_api_v1_metadata_cloud_sync_post()

Update to Latest Metadata

Update to Latest Metadata

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import metadata_api
from nexuscloud_client.model.nexus_insights_api_v1_metadata_cloud_sync_post200_response import NexusInsightsApiV1MetadataCloudSyncPost200Response
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
    api_instance = metadata_api.MetadataApi(api_client)
    body = {} # bool, date, datetime, dict, float, int, list, str, none_type | The parameters used for starting the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update to Latest Metadata
        api_response = api_instance.nexus_insights_api_v1_metadata_cloud_sync_post(body=body)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MetadataApi->nexus_insights_api_v1_metadata_cloud_sync_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| The parameters used for starting the job | [optional]

### Return type

[**NexusInsightsApiV1MetadataCloudSyncPost200Response**](NexusInsightsApiV1MetadataCloudSyncPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_metadata_latest_get**
> NexusInsightsApiV1MetadataCloudSyncPost200Response nexus_insights_api_v1_metadata_latest_get()

Get Latest Metadata

Get Latest Metadata

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import metadata_api
from nexuscloud_client.model.nexus_insights_api_v1_metadata_cloud_sync_post200_response import NexusInsightsApiV1MetadataCloudSyncPost200Response
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
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Latest Metadata
        api_response = api_instance.nexus_insights_api_v1_metadata_latest_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling MetadataApi->nexus_insights_api_v1_metadata_latest_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NexusInsightsApiV1MetadataCloudSyncPost200Response**](NexusInsightsApiV1MetadataCloudSyncPost200Response.md)

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

