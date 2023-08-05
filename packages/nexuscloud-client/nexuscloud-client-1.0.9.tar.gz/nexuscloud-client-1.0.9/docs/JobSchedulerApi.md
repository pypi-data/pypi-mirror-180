# nexuscloud_client.JobSchedulerApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_config_add_job_post**](JobSchedulerApi.md#nexus_insights_api_v1_config_add_job_post) | **POST** /nexus/insights/api/v1/config/addJob | Add a config job to be scheduled
[**nexus_insights_api_v1_config_delete_job_post**](JobSchedulerApi.md#nexus_insights_api_v1_config_delete_job_post) | **POST** /nexus/insights/api/v1/config/deleteJob | Delete a scheduled job
[**nexus_insights_api_v1_jobs_stop_post**](JobSchedulerApi.md#nexus_insights_api_v1_jobs_stop_post) | **POST** /nexus/insights/api/v1/jobs/stop | Stop a scheduled job


# **nexus_insights_api_v1_config_add_job_post**
> NexusInsightsApiV1ConfigAddJobPost200Response nexus_insights_api_v1_config_add_job_post()

Add a config job to be scheduled

Add a Log Collection or Bug Scan or Best Practices job to be scheduled by Sensei

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import job_scheduler_api
from nexuscloud_client.model.nexus_insights_api_v1_config_add_job_post200_response import NexusInsightsApiV1ConfigAddJobPost200Response
from nexuscloud_client.model.nexus_insights_api_v1_config_add_job_post_request import NexusInsightsApiV1ConfigAddJobPostRequest
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_scheduler_api.JobSchedulerApi(api_client)
    nexus_insights_api_v1_config_add_job_post_request = NexusInsightsApiV1ConfigAddJobPostRequest(
        config_id="COMPLIANCEdbe63844-cfdc-11ea-a27b-b655223bd493",
        config_name="Sanjose_COMPLIANCE",
        config_type="Sanjose",
        fabric_name="Sanjose",
        node_names=["Sanjose-leaf1","Sanjose-leaf2"],
        platform_log_collection=True,
        recurrence_end_date_time=1595615400000,
        recurrence_pattern="Instant",
        recurrence_start_date_time=1595615400000,
    ) # NexusInsightsApiV1ConfigAddJobPostRequest | The parameters used for scheduling the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a config job to be scheduled
        api_response = api_instance.nexus_insights_api_v1_config_add_job_post(nexus_insights_api_v1_config_add_job_post_request=nexus_insights_api_v1_config_add_job_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling JobSchedulerApi->nexus_insights_api_v1_config_add_job_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_config_add_job_post_request** | [**NexusInsightsApiV1ConfigAddJobPostRequest**](NexusInsightsApiV1ConfigAddJobPostRequest.md)| The parameters used for scheduling the job | [optional]

### Return type

[**NexusInsightsApiV1ConfigAddJobPost200Response**](NexusInsightsApiV1ConfigAddJobPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_config_delete_job_post**
> NexusInsightsApiV1ConfigDeleteJobPost200Response nexus_insights_api_v1_config_delete_job_post()

Delete a scheduled job

Delete a Log Collection or Bug Scan or Best Practices job  scheduled by Sensei

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import job_scheduler_api
from nexuscloud_client.model.nexus_insights_api_v1_config_delete_job_post200_response import NexusInsightsApiV1ConfigDeleteJobPost200Response
from nexuscloud_client.model.nexus_insights_api_v1_config_delete_job_post_request import NexusInsightsApiV1ConfigDeleteJobPostRequest
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_scheduler_api.JobSchedulerApi(api_client)
    nexus_insights_api_v1_config_delete_job_post_request = NexusInsightsApiV1ConfigDeleteJobPostRequest(
        config_id="COMPLIANCEdbe63844-cfdc-11ea-a27b-b655223bd493",
        fabric_name="Sanjose",
    ) # NexusInsightsApiV1ConfigDeleteJobPostRequest | The parameters used for deleting the job config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a scheduled job
        api_response = api_instance.nexus_insights_api_v1_config_delete_job_post(nexus_insights_api_v1_config_delete_job_post_request=nexus_insights_api_v1_config_delete_job_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling JobSchedulerApi->nexus_insights_api_v1_config_delete_job_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_config_delete_job_post_request** | [**NexusInsightsApiV1ConfigDeleteJobPostRequest**](NexusInsightsApiV1ConfigDeleteJobPostRequest.md)| The parameters used for deleting the job config | [optional]

### Return type

[**NexusInsightsApiV1ConfigDeleteJobPost200Response**](NexusInsightsApiV1ConfigDeleteJobPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_jobs_stop_post**
> NexusInsightsApiV1JobsStopPost200Response nexus_insights_api_v1_jobs_stop_post()

Stop a scheduled job

Stop an instance of Log Collection or Bug Scan or Best Practices job scheduled by Sensei

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import job_scheduler_api
from nexuscloud_client.model.nexus_insights_api_v1_jobs_stop_post_request import NexusInsightsApiV1JobsStopPostRequest
from nexuscloud_client.model.nexus_insights_api_v1_jobs_stop_post200_response import NexusInsightsApiV1JobsStopPost200Response
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
    api_instance = job_scheduler_api.JobSchedulerApi(api_client)
    nexus_insights_api_v1_jobs_stop_post_request = NexusInsightsApiV1JobsStopPostRequest(
        instance_id="COMPLIANCEdbe63844-cfdc-11ea-a27b-b655223bd493",
        site_name="Sanjose",
    ) # NexusInsightsApiV1JobsStopPostRequest | The parameters used for stopping the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop a scheduled job
        api_response = api_instance.nexus_insights_api_v1_jobs_stop_post(nexus_insights_api_v1_jobs_stop_post_request=nexus_insights_api_v1_jobs_stop_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling JobSchedulerApi->nexus_insights_api_v1_jobs_stop_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_jobs_stop_post_request** | [**NexusInsightsApiV1JobsStopPostRequest**](NexusInsightsApiV1JobsStopPostRequest.md)| The parameters used for stopping the job | [optional]

### Return type

[**NexusInsightsApiV1JobsStopPost200Response**](NexusInsightsApiV1JobsStopPost200Response.md)

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

