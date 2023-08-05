# nexuscloud_client.LogCollectionApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_config_fast_start_get**](LogCollectionApi.md#nexus_insights_api_v1_config_fast_start_get) | **GET** /nexus/insights/api/v1/config/fastStart | Get status of fastStart job
[**nexus_insights_api_v1_config_fast_start_post**](LogCollectionApi.md#nexus_insights_api_v1_config_fast_start_post) | **POST** /nexus/insights/api/v1/config/fastStart | Start a fastStart job
[**nexus_insights_api_v1_job_tech_support_upload_all_post**](LogCollectionApi.md#nexus_insights_api_v1_job_tech_support_upload_all_post) | **POST** /nexus/insights/api/v1/job/techSupportUploadAll | Trigger techsupport upload
[**nexus_insights_api_v1_job_tech_support_upload_post**](LogCollectionApi.md#nexus_insights_api_v1_job_tech_support_upload_post) | **POST** /nexus/insights/api/v1/job/techSupportUpload | Trigger techsupport upload


# **nexus_insights_api_v1_config_fast_start_get**
> NexusInsightsApiV1ConfigFastStartGet201Response nexus_insights_api_v1_config_fast_start_get()

Get status of fastStart job

Get status of fastStart job.

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import log_collection_api
from nexuscloud_client.model.nexus_insights_api_v1_config_fast_start_get201_response import NexusInsightsApiV1ConfigFastStartGet201Response
from nexuscloud_client.model.nexus_insights_api_v1_config_fast_start_get_request import NexusInsightsApiV1ConfigFastStartGetRequest
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
    api_instance = log_collection_api.LogCollectionApi(api_client)
    nexus_insights_api_v1_config_fast_start_get_request = NexusInsightsApiV1ConfigFastStartGetRequest(
        instance_id="SAASTACASSIST-5544f688-0d4a-11ed-97a6-2a01f04f2523",
    ) # NexusInsightsApiV1ConfigFastStartGetRequest | Config id of the job for which status needs to be checked (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get status of fastStart job
        api_response = api_instance.nexus_insights_api_v1_config_fast_start_get(nexus_insights_api_v1_config_fast_start_get_request=nexus_insights_api_v1_config_fast_start_get_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling LogCollectionApi->nexus_insights_api_v1_config_fast_start_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_config_fast_start_get_request** | [**NexusInsightsApiV1ConfigFastStartGetRequest**](NexusInsightsApiV1ConfigFastStartGetRequest.md)| Config id of the job for which status needs to be checked | [optional]

### Return type

[**NexusInsightsApiV1ConfigFastStartGet201Response**](NexusInsightsApiV1ConfigFastStartGet201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**401** | Key not authorized:token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_config_fast_start_post**
> NexusInsightsApiV1ConfigFastStartGet201Response1 nexus_insights_api_v1_config_fast_start_post()

Start a fastStart job

Add a fastStart job to be scheduled by jobScheduler.

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import log_collection_api
from nexuscloud_client.model.nexus_insights_api_v1_config_fast_start_get201_response1 import NexusInsightsApiV1ConfigFastStartGet201Response1
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_config_fast_start_get_request1 import NexusInsightsApiV1ConfigFastStartGetRequest1
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = log_collection_api.LogCollectionApi(api_client)
    nexus_insights_api_v1_config_fast_start_get_request1 = NexusInsightsApiV1ConfigFastStartGetRequest1(
        instance_id="FDO22242J62",
    ) # NexusInsightsApiV1ConfigFastStartGetRequest1 | The parameters used for starting the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a fastStart job
        api_response = api_instance.nexus_insights_api_v1_config_fast_start_post(nexus_insights_api_v1_config_fast_start_get_request1=nexus_insights_api_v1_config_fast_start_get_request1)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling LogCollectionApi->nexus_insights_api_v1_config_fast_start_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_config_fast_start_get_request1** | [**NexusInsightsApiV1ConfigFastStartGetRequest1**](NexusInsightsApiV1ConfigFastStartGetRequest1.md)| The parameters used for starting the job | [optional]

### Return type

[**NexusInsightsApiV1ConfigFastStartGet201Response1**](NexusInsightsApiV1ConfigFastStartGet201Response1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ok |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Location - URL where the created object is accessible should be returned <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_job_tech_support_upload_all_post**
> NexusInsightsApiV1JobTechSupportUploadPost200Response nexus_insights_api_v1_job_tech_support_upload_all_post()

Trigger techsupport upload

Post api to trigger techsupport upload

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import log_collection_api
from nexuscloud_client.model.nexus_insights_api_v1_job_tech_support_upload_post200_response import NexusInsightsApiV1JobTechSupportUploadPost200Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_job_tech_support_upload_all_post_request import NexusInsightsApiV1JobTechSupportUploadAllPostRequest
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = log_collection_api.LogCollectionApi(api_client)
    nexus_insights_api_v1_job_tech_support_upload_all_post_request = NexusInsightsApiV1JobTechSupportUploadAllPostRequest(
        jobid="TACASSIST_Instant1",
        origin="UI",
        site_name="dcnm_test1",
        user_name="admin",
    ) # NexusInsightsApiV1JobTechSupportUploadAllPostRequest | The parameters used for starting the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Trigger techsupport upload
        api_response = api_instance.nexus_insights_api_v1_job_tech_support_upload_all_post(nexus_insights_api_v1_job_tech_support_upload_all_post_request=nexus_insights_api_v1_job_tech_support_upload_all_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling LogCollectionApi->nexus_insights_api_v1_job_tech_support_upload_all_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_job_tech_support_upload_all_post_request** | [**NexusInsightsApiV1JobTechSupportUploadAllPostRequest**](NexusInsightsApiV1JobTechSupportUploadAllPostRequest.md)| The parameters used for starting the job | [optional]

### Return type

[**NexusInsightsApiV1JobTechSupportUploadPost200Response**](NexusInsightsApiV1JobTechSupportUploadPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | In progress |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**403** | Records list |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Job ID not found |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**503** | Not connected |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_job_tech_support_upload_post**
> NexusInsightsApiV1JobTechSupportUploadPost200Response nexus_insights_api_v1_job_tech_support_upload_post()

Trigger techsupport upload

Post api to trigger techsupport upload

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import log_collection_api
from nexuscloud_client.model.nexus_insights_api_v1_job_tech_support_upload_post_request import NexusInsightsApiV1JobTechSupportUploadPostRequest
from nexuscloud_client.model.nexus_insights_api_v1_job_tech_support_upload_post200_response import NexusInsightsApiV1JobTechSupportUploadPost200Response
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
    api_instance = log_collection_api.LogCollectionApi(api_client)
    nexus_insights_api_v1_job_tech_support_upload_post_request = NexusInsightsApiV1JobTechSupportUploadPostRequest(
        filename="File name to be ued",
        jobid="TACASSIST_Instant1",
        origin="UI",
        serialnumber="FDO22242J62",
    ) # NexusInsightsApiV1JobTechSupportUploadPostRequest | The parameters used for starting the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Trigger techsupport upload
        api_response = api_instance.nexus_insights_api_v1_job_tech_support_upload_post(nexus_insights_api_v1_job_tech_support_upload_post_request=nexus_insights_api_v1_job_tech_support_upload_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling LogCollectionApi->nexus_insights_api_v1_job_tech_support_upload_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_job_tech_support_upload_post_request** | [**NexusInsightsApiV1JobTechSupportUploadPostRequest**](NexusInsightsApiV1JobTechSupportUploadPostRequest.md)| The parameters used for starting the job | [optional]

### Return type

[**NexusInsightsApiV1JobTechSupportUploadPost200Response**](NexusInsightsApiV1JobTechSupportUploadPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | In progress |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Job ID not found |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

