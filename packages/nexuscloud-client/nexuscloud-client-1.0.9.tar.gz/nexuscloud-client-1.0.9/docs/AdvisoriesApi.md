# nexuscloud_client.AdvisoriesApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_advisories_details_get**](AdvisoriesApi.md#nexus_insights_api_v1_advisories_details_get) | **GET** /nexus/insights/api/v1/advisories/details | Get the advisories
[**nexus_insights_api_v1_advisories_summary_get**](AdvisoriesApi.md#nexus_insights_api_v1_advisories_summary_get) | **GET** /nexus/insights/api/v1/advisories/summary | Get the summary of advisories
[**nexus_insights_api_v1_advisories_top_fabrics_get**](AdvisoriesApi.md#nexus_insights_api_v1_advisories_top_fabrics_get) | **GET** /nexus/insights/api/v1/advisories/topFabrics | Get Top Fabrics based on Advisory Score


# **nexus_insights_api_v1_advisories_details_get**
> NexusInsightsApiV1AdvisoriesDetailsGet200Response nexus_insights_api_v1_advisories_details_get()

Get the advisories

Get the list of advisories for a given InsightsGroup or site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import advisories_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get200_response import NexusInsightsApiV1AdvisoriesDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = advisories_api.AdvisoriesApi(api_client)
    filter = "acknowledged%3Afalse%20AND%20category%3AHWEOL" # str | Lucene format filter - Filter the response based on this filter field (optional)
    site_group_name = "BANGALORE" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "ifav19" # str | Name of the Site - limit the records pertaining to the site (optional)
    node_name = "ifav19-leaf1" # str | Name of the fabric node - limit the records to the nodeName (optional)
    offset = "0" # str | Pagination index into response (optional)
    count = "10" # str | Limits the number of entries in the response (optional)
    end_date = "2021-04-20T12%3A15%3A01-07%3A00" # str | End date, to collect the records generated till specified date (optional)
    sort = "%2Dseverity" # str | Sort records in response by this field (optional)
    start_date = "2021-04-20T12%3A00%3A01-07%3A00" # str | Start date, to skip records generated earlier to this date (optional)
    site_status = "all" # str | Status of the site (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the advisories
        api_response = api_instance.nexus_insights_api_v1_advisories_details_get(filter=filter, site_group_name=site_group_name, site_name=site_name, node_name=node_name, offset=offset, count=count, end_date=end_date, sort=sort, start_date=start_date, site_status=site_status)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AdvisoriesApi->nexus_insights_api_v1_advisories_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **node_name** | **str**| Name of the fabric node - limit the records to the nodeName | [optional]
 **offset** | **str**| Pagination index into response | [optional]
 **count** | **str**| Limits the number of entries in the response | [optional]
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **sort** | **str**| Sort records in response by this field | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **site_status** | **str**| Status of the site | [optional]

### Return type

[**NexusInsightsApiV1AdvisoriesDetailsGet200Response**](NexusInsightsApiV1AdvisoriesDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_advisories_summary_get**
> NexusInsightsApiV1AdvisoriesSummaryGet200Response nexus_insights_api_v1_advisories_summary_get()

Get the summary of advisories

Get the summary of advisories for a given InsightsGroup or site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import advisories_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_advisories_summary_get200_response import NexusInsightsApiV1AdvisoriesSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = advisories_api.AdvisoriesApi(api_client)
    filter = "acknowledged%3Afalse%20AND%20category%3AHWEOL" # str | Lucene format filter - Filter the response based on this filter field (optional)
    site_group_name = "BANGALORE" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    site_name = "ifav19" # str | Name of the Site - limit the records pertaining to the site (optional)
    node_name = "ifav19-leaf1" # str | Name of the fabric node - limit the records to the nodeName (optional)
    end_date = "2021-04-20T12%3A15%3A01-07%3A00" # str | End date, to collect the records generated till specified date (optional)
    start_date = "2021-04-20T12%3A00%3A01-07%3A00" # str | Start date, to skip records generated earlier to this date (optional)
    aggr = "category" # str | Aggregate records by this field (optional)
    site_status = "all" # str | Status of the site (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the summary of advisories
        api_response = api_instance.nexus_insights_api_v1_advisories_summary_get(filter=filter, site_group_name=site_group_name, site_name=site_name, node_name=node_name, end_date=end_date, start_date=start_date, aggr=aggr, site_status=site_status)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AdvisoriesApi->nexus_insights_api_v1_advisories_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **node_name** | **str**| Name of the fabric node - limit the records to the nodeName | [optional]
 **end_date** | **str**| End date, to collect the records generated till specified date | [optional]
 **start_date** | **str**| Start date, to skip records generated earlier to this date | [optional]
 **aggr** | **str**| Aggregate records by this field | [optional]
 **site_status** | **str**| Status of the site | [optional]

### Return type

[**NexusInsightsApiV1AdvisoriesSummaryGet200Response**](NexusInsightsApiV1AdvisoriesSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  * Link - Link to navigate pages of entries in case of pagination <br>  |
**401** | Key not authorized, token contains an invalid number of segments |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_advisories_top_fabrics_get**
> NexusInsightsApiV1AdvisoriesTopFabricsGet200Response nexus_insights_api_v1_advisories_top_fabrics_get()

Get Top Fabrics based on Advisory Score

Get Top Fabrics along with Advisory Score and Advisory Count

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import advisories_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_top_fabrics_get200_response import NexusInsightsApiV1AdvisoriesTopFabricsGet200Response
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
    api_instance = advisories_api.AdvisoriesApi(api_client)
    start_date = "2021-03-26T9:14:54.940+05:30" # str | Start timestamp, to skip records generated earlier to this timestamp (optional) if omitted the server will use the default value of "now-1h"
    end_date = "2021-03-26T10:14:54.940+05:30" # str | End timestamp, to collect the records generated till specified time (optional) if omitted the server will use the default value of "now"
    site_group_name = "telemetry-ig" # str | Name of the Site Group, limit the records to this siteGroup (optional) if omitted the server will use the default value of "None"
    count = 5 # int | Limits the number of entries in the response (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Top Fabrics based on Advisory Score
        api_response = api_instance.nexus_insights_api_v1_advisories_top_fabrics_get(start_date=start_date, end_date=end_date, site_group_name=site_group_name, count=count)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling AdvisoriesApi->nexus_insights_api_v1_advisories_top_fabrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start timestamp, to skip records generated earlier to this timestamp | [optional] if omitted the server will use the default value of "now-1h"
 **end_date** | **str**| End timestamp, to collect the records generated till specified time | [optional] if omitted the server will use the default value of "now"
 **site_group_name** | **str**| Name of the Site Group, limit the records to this siteGroup | [optional] if omitted the server will use the default value of "None"
 **count** | **int**| Limits the number of entries in the response | [optional] if omitted the server will use the default value of 10

### Return type

[**NexusInsightsApiV1AdvisoriesTopFabricsGet200Response**](NexusInsightsApiV1AdvisoriesTopFabricsGet200Response.md)

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

