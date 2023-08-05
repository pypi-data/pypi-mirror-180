# nexuscloud_client.ReportsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_reports_cloud_details_get**](ReportsApi.md#nexus_insights_api_v1_reports_cloud_details_get) | **GET** /nexus/insights/api/v1/reports/cloudDetails | Get conformance details of a reportType for a siteName over an outlookPeriod
[**nexus_insights_api_v1_reports_cloud_inventory_get**](ReportsApi.md#nexus_insights_api_v1_reports_cloud_inventory_get) | **GET** /nexus/insights/api/v1/reports/cloudInventory | Get Inventory reports for a siteName
[**nexus_insights_api_v1_reports_cloud_summary_get**](ReportsApi.md#nexus_insights_api_v1_reports_cloud_summary_get) | **GET** /nexus/insights/api/v1/reports/cloudSummary | Get conformance summary of a reportType for a siteName over an outlookPeriod
[**nexus_insights_api_v1_reports_details_get**](ReportsApi.md#nexus_insights_api_v1_reports_details_get) | **GET** /nexus/insights/api/v1/reports/details | Get conformance details of a reportType for a siteName over an outlookPeriod
[**nexus_insights_api_v1_reports_inventory_get**](ReportsApi.md#nexus_insights_api_v1_reports_inventory_get) | **GET** /nexus/insights/api/v1/reports/inventory | Get Inventory reports for a siteName
[**nexus_insights_api_v1_reports_summary_get**](ReportsApi.md#nexus_insights_api_v1_reports_summary_get) | **GET** /nexus/insights/api/v1/reports/summary | Get conformance summary of a reportType for a siteName over an outlookPeriod


# **nexus_insights_api_v1_reports_cloud_details_get**
> NexusInsightsApiV1ReportsCloudDetailsGet200Response nexus_insights_api_v1_reports_cloud_details_get(outlook)

Get conformance details of a reportType for a siteName over an outlookPeriod

Get a hardware, software or overall conformance details for a fabric over a projection period (from now to max. 18 months in the future).

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import reports_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_reports_cloud_details_get200_response import NexusInsightsApiV1ReportsCloudDetailsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    outlook = 3 # int | Period over which the conformance details for the fabric are projected
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    site_name_list = "DC-WEST,DC-EAST" # str | List of site names (optional)
    site_group_name = "IG1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    filter = "softwareConformance:healthy%20AND%20hardwareConformance:critical" # str | Lucene format filter - Filter the response based on this filter field (optional)
    include = "nodes" # str | Device types to include in the conformance results (optional)
    offset = "0" # str | Pagination index into response (optional)
    count = "10" # str | Limits the number of entries in the response (optional)
    sort = "siteName%2Cdesc" # str | Sort records in response by this field (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get conformance details of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_cloud_details_get(outlook)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_cloud_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get conformance details of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_cloud_details_get(outlook, site_name=site_name, site_name_list=site_name_list, site_group_name=site_group_name, filter=filter, include=include, offset=offset, count=count, sort=sort)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_cloud_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outlook** | **int**| Period over which the conformance details for the fabric are projected |
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **site_name_list** | **str**| List of site names | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **include** | **str**| Device types to include in the conformance results | [optional]
 **offset** | **str**| Pagination index into response | [optional]
 **count** | **str**| Limits the number of entries in the response | [optional]
 **sort** | **str**| Sort records in response by this field | [optional]

### Return type

[**NexusInsightsApiV1ReportsCloudDetailsGet200Response**](NexusInsightsApiV1ReportsCloudDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Conformance report currently unavailable for the fabric |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_reports_cloud_inventory_get**
> NexusInsightsApiV1ReportsCloudInventoryGet200Response nexus_insights_api_v1_reports_cloud_inventory_get()

Get Inventory reports for a siteName

Get Inventory reports for the given siteName

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import reports_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_reports_cloud_inventory_get200_response import NexusInsightsApiV1ReportsCloudInventoryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    site_name_list = "DC-WEST,DC-EAST" # str | List of site names (optional)
    site_group_name = "IG1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Inventory reports for a siteName
        api_response = api_instance.nexus_insights_api_v1_reports_cloud_inventory_get(site_name=site_name, site_name_list=site_name_list, site_group_name=site_group_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_cloud_inventory_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **site_name_list** | **str**| List of site names | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]

### Return type

[**NexusInsightsApiV1ReportsCloudInventoryGet200Response**](NexusInsightsApiV1ReportsCloudInventoryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Inventory report currently unavailable for the fabric |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_reports_cloud_summary_get**
> NexusInsightsApiV1ReportsCloudSummaryGet200Response nexus_insights_api_v1_reports_cloud_summary_get(outlook_period, report_type)

Get conformance summary of a reportType for a siteName over an outlookPeriod

Get a hardware, software or overall conformance summary for a fabric over a projection period (from now to max. 18 months in the future).

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import reports_api
from nexuscloud_client.model.nexus_insights_api_v1_reports_cloud_summary_get200_response import NexusInsightsApiV1ReportsCloudSummaryGet200Response
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
    api_instance = reports_api.ReportsApi(api_client)
    outlook_period = 3 # int | Period over which the conformance details for the fabric are projected
    report_type = "overall" # str | Type of report
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    site_name_list = "DC-WEST,DC-EAST" # str | List of site names (optional)
    site_group_name = "IG1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get conformance summary of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_cloud_summary_get(outlook_period, report_type)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_cloud_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get conformance summary of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_cloud_summary_get(outlook_period, report_type, site_name=site_name, site_name_list=site_name_list, site_group_name=site_group_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_cloud_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outlook_period** | **int**| Period over which the conformance details for the fabric are projected |
 **report_type** | **str**| Type of report |
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **site_name_list** | **str**| List of site names | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]

### Return type

[**NexusInsightsApiV1ReportsCloudSummaryGet200Response**](NexusInsightsApiV1ReportsCloudSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**415** | Conformance report currently unavailable for the fabric |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_reports_details_get**
> NexusInsightsApiV1ReportsDetailsGet200Response nexus_insights_api_v1_reports_details_get(outlook)

Get conformance details of a reportType for a siteName over an outlookPeriod

Get a hardware, software or overall conformance details for a fabric over a projection period (from now to max. 18 months in the future).

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import reports_api
from nexuscloud_client.model.nexus_insights_api_v1_reports_details_get200_response import NexusInsightsApiV1ReportsDetailsGet200Response
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
    api_instance = reports_api.ReportsApi(api_client)
    outlook = 3 # int | Period over which the conformance details for the fabric are projected
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    site_group_name = "IG1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)
    filter = "softwareConformance:healthy%20AND%20hardwareConformance:critical" # str | Lucene format filter - Filter the response based on this filter field (optional)
    include = "nodes" # str | Device types to include in the conformance results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get conformance details of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_details_get(outlook)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_details_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get conformance details of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_details_get(outlook, site_name=site_name, site_group_name=site_group_name, filter=filter, include=include)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outlook** | **int**| Period over which the conformance details for the fabric are projected |
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]
 **filter** | **str**| Lucene format filter - Filter the response based on this filter field | [optional]
 **include** | **str**| Device types to include in the conformance results | [optional]

### Return type

[**NexusInsightsApiV1ReportsDetailsGet200Response**](NexusInsightsApiV1ReportsDetailsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Conformance report currently unavailable for the fabric |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_reports_inventory_get**
> NexusInsightsApiV1ReportsInventoryGet200Response nexus_insights_api_v1_reports_inventory_get()

Get Inventory reports for a siteName

Get Inventory reports for the given siteName

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import reports_api
from nexuscloud_client.model.nexus_insights_api_v1_reports_inventory_get200_response import NexusInsightsApiV1ReportsInventoryGet200Response
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
    api_instance = reports_api.ReportsApi(api_client)
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    site_group_name = "IG1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Inventory reports for a siteName
        api_response = api_instance.nexus_insights_api_v1_reports_inventory_get(site_name=site_name, site_group_name=site_group_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_inventory_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]

### Return type

[**NexusInsightsApiV1ReportsInventoryGet200Response**](NexusInsightsApiV1ReportsInventoryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Inventory report currently unavailable for the fabric |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_reports_summary_get**
> NexusInsightsApiV1ReportsSummaryGet200Response nexus_insights_api_v1_reports_summary_get(outlook_period, report_type)

Get conformance summary of a reportType for a siteName over an outlookPeriod

Get a hardware, software or overall conformance summary for a fabric over a projection period (from now to max. 18 months in the future).

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import reports_api
from nexuscloud_client.model.nexus_insights_api_v1_advisories_details_get401_response import NexusInsightsApiV1AdvisoriesDetailsGet401Response
from nexuscloud_client.model.nexus_insights_api_v1_reports_summary_get200_response import NexusInsightsApiV1ReportsSummaryGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    outlook_period = 3 # int | Period over which the conformance details for the fabric are projected
    report_type = "overall" # str | Type of report
    site_name = "DC-WEST" # str | Name of the Site - limit the records pertaining to the site (optional)
    site_group_name = "IG1" # str | Name of the Site Group - limit the records pertaining to the sites in this site group (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get conformance summary of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_summary_get(outlook_period, report_type)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get conformance summary of a reportType for a siteName over an outlookPeriod
        api_response = api_instance.nexus_insights_api_v1_reports_summary_get(outlook_period, report_type, site_name=site_name, site_group_name=site_group_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ReportsApi->nexus_insights_api_v1_reports_summary_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outlook_period** | **int**| Period over which the conformance details for the fabric are projected |
 **report_type** | **str**| Type of report |
 **site_name** | **str**| Name of the Site - limit the records pertaining to the site | [optional]
 **site_group_name** | **str**| Name of the Site Group - limit the records pertaining to the sites in this site group | [optional]

### Return type

[**NexusInsightsApiV1ReportsSummaryGet200Response**](NexusInsightsApiV1ReportsSummaryGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**400** | Either missing a mandatory param or provided an unsupported param |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |
**404** | Conformance report currently unavailable for the fabric |  * Date - Timestamp the response was processed, based on the server&#39;s clock, in GMT <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

