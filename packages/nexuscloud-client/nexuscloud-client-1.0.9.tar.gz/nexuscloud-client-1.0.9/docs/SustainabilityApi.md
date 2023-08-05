# nexuscloud_client.SustainabilityApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nexus_insights_api_v1_sustainability_available_timelines_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_available_timelines_get) | **GET** /nexus/insights/api/v1/sustainability/availableTimelines | Get available timelines for the sites
[**nexus_insights_api_v1_sustainability_calc_status_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_calc_status_get) | **GET** /nexus/insights/api/v1/sustainability/calcStatus | Get Sustainability Calc Status
[**nexus_insights_api_v1_sustainability_cost_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_cost_get) | **GET** /nexus/insights/api/v1/sustainability/cost | Get Sustainability Cost data
[**nexus_insights_api_v1_sustainability_data_status_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_data_status_get) | **GET** /nexus/insights/api/v1/sustainability/dataStatus | Is Sustainability Data ready to be consumed
[**nexus_insights_api_v1_sustainability_emissions_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_emissions_get) | **GET** /nexus/insights/api/v1/sustainability/emissions | Get Sustainability Emissions data
[**nexus_insights_api_v1_sustainability_energy_settings_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_energy_settings_get) | **GET** /nexus/insights/api/v1/sustainability/energySettings | Get Cost ($/kWh) per Site
[**nexus_insights_api_v1_sustainability_energy_settings_post**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_energy_settings_post) | **POST** /nexus/insights/api/v1/sustainability/energySettings | Set Power Cost ($/kWh) per Site
[**nexus_insights_api_v1_sustainability_power_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_power_get) | **GET** /nexus/insights/api/v1/sustainability/power | Get Sustainability Power data
[**nexus_insights_api_v1_sustainability_site_status_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_site_status_get) | **GET** /nexus/insights/api/v1/sustainability/siteStatus | Get Sustainability Site Status
[**nexus_insights_api_v1_sustainability_sources_get**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_sources_get) | **GET** /nexus/insights/api/v1/sustainability/sources | Get Sustainability Sources data
[**nexus_insights_api_v1_sustainability_trigger_calcs_post**](SustainabilityApi.md#nexus_insights_api_v1_sustainability_trigger_calcs_post) | **POST** /nexus/insights/api/v1/sustainability/triggerCalcs | Trigger Sustainability Data calculations


# **nexus_insights_api_v1_sustainability_available_timelines_get**
> NexusInsightsApiV1SustainabilityAvailableTimelinesGet200Response nexus_insights_api_v1_sustainability_available_timelines_get()

Get available timelines for the sites

Get available timelines for the sites

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_available_timelines_get200_response import NexusInsightsApiV1SustainabilityAvailableTimelinesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_name_list = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get available timelines for the sites
        api_response = api_instance.nexus_insights_api_v1_sustainability_available_timelines_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_available_timelines_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get available timelines for the sites
        api_response = api_instance.nexus_insights_api_v1_sustainability_available_timelines_get(site_name=site_name, site_name_list=site_name_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_available_timelines_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_name_list** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilityAvailableTimelinesGet200Response**](NexusInsightsApiV1SustainabilityAvailableTimelinesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_calc_status_get**
> NexusInsightsApiV1SustainabilityCalcStatusGet200Response nexus_insights_api_v1_sustainability_calc_status_get()

Get Sustainability Calc Status

Get Sustainability Calc Status

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_calc_status_get200_response import NexusInsightsApiV1SustainabilityCalcStatusGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    calc_id = "XYZ" # str | calc ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Sustainability Calc Status
        api_response = api_instance.nexus_insights_api_v1_sustainability_calc_status_get(calc_id=calc_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_calc_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calc_id** | **str**| calc ID | [optional]

### Return type

[**NexusInsightsApiV1SustainabilityCalcStatusGet200Response**](NexusInsightsApiV1SustainabilityCalcStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_cost_get**
> NexusInsightsApiV1SustainabilityCostGet200Response nexus_insights_api_v1_sustainability_cost_get()

Get Sustainability Cost data

Get Sustainability Cost data

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_cost_get200_response import NexusInsightsApiV1SustainabilityCostGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    start_date = "2021-04-01T0:00:00.000+05:30" # str | Start timestamp (optional) if omitted the server will use the default value of "None"
    end_date = "2021-04-30T23:59:59.000+05:30" # str | End timestamp (optional) if omitted the server will use the default value of "None"
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_name_list = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get Sustainability Cost data
        api_response = api_instance.nexus_insights_api_v1_sustainability_cost_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_cost_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Sustainability Cost data
        api_response = api_instance.nexus_insights_api_v1_sustainability_cost_get(start_date=start_date, end_date=end_date, site_name=site_name, site_name_list=site_name_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_cost_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **start_date** | **str**| Start timestamp | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End timestamp | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_name_list** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilityCostGet200Response**](NexusInsightsApiV1SustainabilityCostGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_data_status_get**
> NexusInsightsApiV1SustainabilityDataStatusGet200Response nexus_insights_api_v1_sustainability_data_status_get()

Is Sustainability Data ready to be consumed

Gives the status if the Sustainability data is ready to be consumed or not

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_data_status_get200_response import NexusInsightsApiV1SustainabilityDataStatusGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_name_list = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Is Sustainability Data ready to be consumed
        api_response = api_instance.nexus_insights_api_v1_sustainability_data_status_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_data_status_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Is Sustainability Data ready to be consumed
        api_response = api_instance.nexus_insights_api_v1_sustainability_data_status_get(site_name=site_name, site_name_list=site_name_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_data_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start timestamp | defaults to "None"
 **end_date** | **str**| End timestamp | defaults to "None"
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_name_list** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilityDataStatusGet200Response**](NexusInsightsApiV1SustainabilityDataStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_emissions_get**
> NexusInsightsApiV1SustainabilityEmissionsGet200Response nexus_insights_api_v1_sustainability_emissions_get()

Get Sustainability Emissions data

Get Sustainability Emissions data

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_emissions_get200_response import NexusInsightsApiV1SustainabilityEmissionsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    start_date = "2021-04-01T0:00:00.000+05:30" # str | Start timestamp (optional) if omitted the server will use the default value of "None"
    end_date = "2021-04-30T23:59:59.000+05:30" # str | End timestamp (optional) if omitted the server will use the default value of "None"
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_name_list = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get Sustainability Emissions data
        api_response = api_instance.nexus_insights_api_v1_sustainability_emissions_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_emissions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Sustainability Emissions data
        api_response = api_instance.nexus_insights_api_v1_sustainability_emissions_get(start_date=start_date, end_date=end_date, site_name=site_name, site_name_list=site_name_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_emissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **start_date** | **str**| Start timestamp | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End timestamp | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_name_list** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilityEmissionsGet200Response**](NexusInsightsApiV1SustainabilityEmissionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_energy_settings_get**
> NexusInsightsApiV1SustainabilityEnergySettingsGet200Response nexus_insights_api_v1_sustainability_energy_settings_get()

Get Cost ($/kWh) per Site

Get Cost ($/kWh) per Site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_energy_settings_get200_response import NexusInsightsApiV1SustainabilityEnergySettingsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Get Cost ($/kWh) per Site
        api_response = api_instance.nexus_insights_api_v1_sustainability_energy_settings_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_energy_settings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"

### Return type

[**NexusInsightsApiV1SustainabilityEnergySettingsGet200Response**](NexusInsightsApiV1SustainabilityEnergySettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_energy_settings_post**
> NexusInsightsApiV1SustainabilityEnergySettingsGet200Response1 nexus_insights_api_v1_sustainability_energy_settings_post()

Set Power Cost ($/kWh) per Site

Set Power Cost ($/kWh) per Site

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_energy_settings_get_request import NexusInsightsApiV1SustainabilityEnergySettingsGetRequest
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_energy_settings_get200_response1 import NexusInsightsApiV1SustainabilityEnergySettingsGet200Response1
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    nexus_insights_api_v1_sustainability_energy_settings_get_request = NexusInsightsApiV1SustainabilityEnergySettingsGetRequest(
        cost_data=[
            NexusInsightsApiV1SustainabilityEnergySettingsGetRequestCostDataInner(
                power_cost=0.1,
                site_name="SanJose",
            ),
        ],
    ) # NexusInsightsApiV1SustainabilityEnergySettingsGetRequest | The parameters used for setting the data (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Power Cost ($/kWh) per Site
        api_response = api_instance.nexus_insights_api_v1_sustainability_energy_settings_post(nexus_insights_api_v1_sustainability_energy_settings_get_request=nexus_insights_api_v1_sustainability_energy_settings_get_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_energy_settings_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_sustainability_energy_settings_get_request** | [**NexusInsightsApiV1SustainabilityEnergySettingsGetRequest**](NexusInsightsApiV1SustainabilityEnergySettingsGetRequest.md)| The parameters used for setting the data | [optional]

### Return type

[**NexusInsightsApiV1SustainabilityEnergySettingsGet200Response1**](NexusInsightsApiV1SustainabilityEnergySettingsGet200Response1.md)

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

# **nexus_insights_api_v1_sustainability_power_get**
> NexusInsightsApiV1SustainabilityPowerGet200Response nexus_insights_api_v1_sustainability_power_get()

Get Sustainability Power data

Get Sustainability Power data

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_power_get200_response import NexusInsightsApiV1SustainabilityPowerGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    start_date = "2021-04-01T0:00:00.000+05:30" # str | Start timestamp (optional) if omitted the server will use the default value of "None"
    end_date = "2021-04-30T23:59:59.000+05:30" # str | End timestamp (optional) if omitted the server will use the default value of "None"
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_name_list = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get Sustainability Power data
        api_response = api_instance.nexus_insights_api_v1_sustainability_power_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_power_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Sustainability Power data
        api_response = api_instance.nexus_insights_api_v1_sustainability_power_get(start_date=start_date, end_date=end_date, site_name=site_name, site_name_list=site_name_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_power_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **start_date** | **str**| Start timestamp | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End timestamp | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_name_list** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilityPowerGet200Response**](NexusInsightsApiV1SustainabilityPowerGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_site_status_get**
> NexusInsightsApiV1SustainabilitySiteStatusGet200Response nexus_insights_api_v1_sustainability_site_status_get()

Get Sustainability Site Status

Get Sustainability Site Status

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_site_status_get200_response import NexusInsightsApiV1SustainabilitySiteStatusGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_name_list = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get Sustainability Site Status
        api_response = api_instance.nexus_insights_api_v1_sustainability_site_status_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_site_status_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Sustainability Site Status
        api_response = api_instance.nexus_insights_api_v1_sustainability_site_status_get(site_name=site_name, site_name_list=site_name_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_site_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_group_name** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_name_list** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilitySiteStatusGet200Response**](NexusInsightsApiV1SustainabilitySiteStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_sources_get**
> NexusInsightsApiV1SustainabilitySourcesGet200Response nexus_insights_api_v1_sustainability_sources_get()

Get Sustainability Sources data

Get Sustainability Sources data

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_sources_get200_response import NexusInsightsApiV1SustainabilitySourcesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    start_date = "2021-04-01T0:00:00.000+05:30" # str | Start timestamp (optional) if omitted the server will use the default value of "None"
    end_date = "2021-04-30T23:59:59.000+05:30" # str | End timestamp (optional) if omitted the server will use the default value of "None"
    site_name = "coke-site1" # str | Name of the site - limit the records pertaining to this siteName (optional) if omitted the server will use the default value of "None"
    site_list_name = "coke-site1,coke-site2" # str | Name of the sites - limit the records pertaining to given siteListNames (optional) if omitted the server will use the default value of "None"

    # example passing only required values which don't have defaults set
    try:
        # Get Sustainability Sources data
        api_response = api_instance.nexus_insights_api_v1_sustainability_sources_get()
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_sources_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Sustainability Sources data
        api_response = api_instance.nexus_insights_api_v1_sustainability_sources_get(start_date=start_date, end_date=end_date, site_name=site_name, site_list_name=site_list_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_sources_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_name_list** | **str**| Name of the Insights Group - limit the records pertaining to the sites in this siteGroupName | defaults to "None"
 **start_date** | **str**| Start timestamp | [optional] if omitted the server will use the default value of "None"
 **end_date** | **str**| End timestamp | [optional] if omitted the server will use the default value of "None"
 **site_name** | **str**| Name of the site - limit the records pertaining to this siteName | [optional] if omitted the server will use the default value of "None"
 **site_list_name** | **str**| Name of the sites - limit the records pertaining to given siteListNames | [optional] if omitted the server will use the default value of "None"

### Return type

[**NexusInsightsApiV1SustainabilitySourcesGet200Response**](NexusInsightsApiV1SustainabilitySourcesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nexus_insights_api_v1_sustainability_trigger_calcs_post**
> NexusInsightsApiV1SustainabilityTriggerCalcsPost200Response nexus_insights_api_v1_sustainability_trigger_calcs_post()

Trigger Sustainability Data calculations

Trigger Sustainability Data calculations

### Example


```python
import time
import nexuscloud_client
from nexuscloud_client.api import sustainability_api
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_trigger_calcs_post200_response import NexusInsightsApiV1SustainabilityTriggerCalcsPost200Response
from nexuscloud_client.model.nexus_insights_api_v1_sustainability_trigger_calcs_post_request import NexusInsightsApiV1SustainabilityTriggerCalcsPostRequest
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)


# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sustainability_api.SustainabilityApi(api_client)
    nexus_insights_api_v1_sustainability_trigger_calcs_post_request = NexusInsightsApiV1SustainabilityTriggerCalcsPostRequest(
        end_date="2021-04-01T0:00:00.000+05:30",
        site_group_name="coke-IG",
        site_name="coke-site1",
        site_name_list="coke-site1,coke-site2",
        start_date="2021-04-01T0:00:00.000+05:30",
    ) # NexusInsightsApiV1SustainabilityTriggerCalcsPostRequest | The parameters used for scheduling the job (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Trigger Sustainability Data calculations
        api_response = api_instance.nexus_insights_api_v1_sustainability_trigger_calcs_post(nexus_insights_api_v1_sustainability_trigger_calcs_post_request=nexus_insights_api_v1_sustainability_trigger_calcs_post_request)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SustainabilityApi->nexus_insights_api_v1_sustainability_trigger_calcs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nexus_insights_api_v1_sustainability_trigger_calcs_post_request** | [**NexusInsightsApiV1SustainabilityTriggerCalcsPostRequest**](NexusInsightsApiV1SustainabilityTriggerCalcsPostRequest.md)| The parameters used for scheduling the job | [optional]

### Return type

[**NexusInsightsApiV1SustainabilityTriggerCalcsPost200Response**](NexusInsightsApiV1SustainabilityTriggerCalcsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Key not authorized:token contains an invalid number of segments |  -  |
**500** | Server error, either the server is overloaded or there is an error in the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

