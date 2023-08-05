# nexuscloud_client.SummaryApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_jobs_summary_get**](SummaryApi.md#nexus_insights_api_v1_jobs_summary_get) | **GET** /nexus/insights/api/v1/jobs/summary | Get Job Summary


# **nexus_insights_api_v1_jobs_summary_get**
> NexusInsightsApiV1JobsSummaryGet200Response nexus_insights_api_v1_jobs_summary_get(site_name)

Get Job Summary

List of jobs and status  Test if job is success or failure, and test progress of the job

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import summary_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_jobs_summary_get200_response import NexusInsightsApiV1JobsSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = summary_api.SummaryApi(api_client)
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site
    filter = "acknowledged:false" # str | Lucene format filter - Filter the response based on this filter field (optional)
    site_group_name = "DC-WEST-IG" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    end_date = "2021-04-19T14:08:05-07:00" # str | End date, to collect the records generated till specified date (optional)
    start_date = "2021-04-19T13:53:05-07:00" # str | Start date, to skip records generated earlier to this date (optional)
    job_id = "jobId_example" # str | job id (optional)
    job_type = "jobType_example" # str | Comma separated list of job types (optional)
    user_name = "userName_example" # str | username (optional)
    config_id = "configId_example" # str | configId for job (optional)
    oper_st = "operSt_example" # str | Status of the operation (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Job Summary
        api_response = api_instance.nexus_insights_api_v1_jobs_summary_get(site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SummaryApi->nexus_insights_api_v1_jobs_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Job Summary
        api_response = api_instance.nexus_insights_api_v1_jobs_summary_get(site_name, filter=filter, site_group_name=site_group_name, end_date=end_date, start_date=start_date, job_id=job_id, job_type=job_type, user_name=user_name, config_id=config_id, oper_st=oper_st)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SummaryApi->nexus_insights_api_v1_jobs_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site |
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **job_id** | **str**| job id | [optional]
 **job_type** | **str**| Comma separated list of job types | [optional]
 **user_name** | **str**| username | [optional]
 **config_id** | **str**| configId for job | [optional]
 **oper_st** | **str**| Status of the operation | [optional]

### Return type

[**NexusInsightsApiV1JobsSummaryGet200Response**](NexusInsightsApiV1JobsSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory parameter or provided an unsupported parameter. |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**500** | Server error, either the server is overloaded or there is an error in the application |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

