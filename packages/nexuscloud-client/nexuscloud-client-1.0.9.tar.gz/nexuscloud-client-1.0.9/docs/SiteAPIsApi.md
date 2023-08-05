# nexuscloud_client.SiteAPIsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_claim_device**](SiteAPIsApi.md#platform_claim_device) | **POST** /nexus/platform/api/v1/claim/devices | Claim a device
[**platform_delete_site**](SiteAPIsApi.md#platform_delete_site) | **DELETE** /nexus/platform/api/v1/sites/{id} | Delete a site based on site name or UUID
[**platform_enroll_site**](SiteAPIsApi.md#platform_enroll_site) | **POST** /nexus/platform/api/v1/sites | Enroll a site
[**platform_get_all_sites**](SiteAPIsApi.md#platform_get_all_sites) | **GET** /nexus/platform/api/v1/sites | Get all sites
[**platform_get_devices_info**](SiteAPIsApi.md#platform_get_devices_info) | **GET** /nexus/platform/api/v1/devices | Device info
[**platform_get_site**](SiteAPIsApi.md#platform_get_site) | **GET** /nexus/platform/api/v1/sites/{id} | Get a site based on sitename or UUID
[**platform_get_sites_inventory**](SiteAPIsApi.md#platform_get_sites_inventory) | **GET** /nexus/platform/api/v1/sites/inventory | Get all sites inventory
[**platform_handle_auto_claim**](SiteAPIsApi.md#platform_handle_auto_claim) | **POST** /nexus/platform/api/v1/autoclaim/devices | Auto claim discovered switches based of seed switch
[**platform_handle_auto_claim_status**](SiteAPIsApi.md#platform_handle_auto_claim_status) | **GET** /nexus/platform/api/v1/autoclaim/{reqId}/status | Query the status of an auto-claim request
[**platform_handle_discover**](SiteAPIsApi.md#platform_handle_discover) | **GET** /nexus/platform/api/v1/discover/devices/{seedDeviceId} | Discover neighboring switches based on seed switch
[**platform_modify_site**](SiteAPIsApi.md#platform_modify_site) | **PUT** /nexus/platform/api/v1/sites/{id} | Modify a site based on sitename or UUID
[**platform_unclaim_device**](SiteAPIsApi.md#platform_unclaim_device) | **DELETE** /nexus/platform/api/v1/claim/devices/{id} | Unclaim a device based on its claimID
[**platform_update_sa_switch**](SiteAPIsApi.md#platform_update_sa_switch) | **PUT** /nexus/platform/api/v1/sites/{siteId}/devices/{deviceId} | Modify standalone site&#39;s switch update


# **platform_claim_device**
> PlatformSiteInfo platform_claim_device(platform_claim_info)

Claim a device

Claim a device

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_claim_info import PlatformClaimInfo
from nexuscloud_client.model.platform_site_info import PlatformSiteInfo
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    platform_claim_info = PlatformClaimInfo(
        security_token="security_token_example",
        serial="serial_example",
        serial_number="serial_number_example",
    ) # PlatformClaimInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Claim a device
        api_response = api_instance.platform_claim_device(platform_claim_info)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_claim_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_claim_info** | [**PlatformClaimInfo**](PlatformClaimInfo.md)|  |

### Return type

[**PlatformSiteInfo**](PlatformSiteInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_delete_site**
> platform_delete_site(id)

Delete a site based on site name or UUID

Delete a site given an ID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    id = "id_example" # str | ID of site

    # example passing only required values which don't have defaults set
    try:
        # Delete a site based on site name or UUID
        api_instance.platform_delete_site(id)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_delete_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of site |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_enroll_site**
> PlatformSiteInfo platform_enroll_site(platform_enroll_info)

Enroll a site

Enroll a site

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_site_info import PlatformSiteInfo
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_enroll_info import PlatformEnrollInfo
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    platform_enroll_info = PlatformEnrollInfo(
        additional_devices=[
            PlatformDeviceInfo(
                device_id="device_id_example",
                name="name_example",
                role=PlatformSwitchRoles("Leaf"),
                seed=True,
            ),
        ],
        device_id="device_id_example",
        latitude="latitude_example",
        longitude="longitude_example",
        name="name_example",
        role=PlatformSwitchRoles("Leaf"),
        site_type=PlatformSiteType("Aci"),
        tier="tier_example",
    ) # PlatformEnrollInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Enroll a site
        api_response = api_instance.platform_enroll_site(platform_enroll_info)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_enroll_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_enroll_info** | [**PlatformEnrollInfo**](PlatformEnrollInfo.md)|  |

### Return type

[**PlatformSiteInfo**](PlatformSiteInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_get_all_sites**
> PlatformSiteList platform_get_all_sites()

Get all sites

Get all sites filtered by query parameters

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_site_list import PlatformSiteList
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    site_type = "siteType_example" # str | Site type to filter results by (optional)
    site_reachabilty_state = "siteReachabilty.state_example" # str | Deprecating, see - siteReachabilityState (optional)
    site_reachability_state = "siteReachabilityState_example" # str | Site reachability state to filter results by (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all sites
        api_response = api_instance.platform_get_all_sites(site_type=site_type, site_reachabilty_state=site_reachabilty_state, site_reachability_state=site_reachability_state)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_get_all_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_type** | **str**| Site type to filter results by | [optional]
 **site_reachabilty_state** | **str**| Deprecating, see - siteReachabilityState | [optional]
 **site_reachability_state** | **str**| Site reachability state to filter results by | [optional]

### Return type

[**PlatformSiteList**](PlatformSiteList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_get_devices_info**
> PlatformSiteInfo platform_get_devices_info()

Device info

Get all devices filtered by query parameters

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_site_info import PlatformSiteInfo
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    device_id = "deviceID_example" # str | Device ID to filter results by (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Device info
        api_response = api_instance.platform_get_devices_info(device_id=device_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_get_devices_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID to filter results by | [optional]

### Return type

[**PlatformSiteInfo**](PlatformSiteInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_get_site**
> PlatformSiteInfo platform_get_site(id)

Get a site based on sitename or UUID

Get a side given an ID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_site_info import PlatformSiteInfo
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    id = "id_example" # str | ID of site

    # example passing only required values which don't have defaults set
    try:
        # Get a site based on sitename or UUID
        api_response = api_instance.platform_get_site(id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_get_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of site |

### Return type

[**PlatformSiteInfo**](PlatformSiteInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_get_sites_inventory**
> PlatformGetAllResponse platform_get_sites_inventory()

Get all sites inventory

Get all sites in inventory

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_get_all_response import PlatformGetAllResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    type = "type_example" # str | Type of site to filter results by (optional)
    site_name = "siteName_example" # str | Site name to filter results by (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all sites inventory
        api_response = api_instance.platform_get_sites_inventory(type=type, site_name=site_name)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_get_sites_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of site to filter results by | [optional]
 **site_name** | **str**| Site name to filter results by | [optional]

### Return type

[**PlatformGetAllResponse**](PlatformGetAllResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_handle_auto_claim**
> PlatformSaSwitchAsyncClaimResp platform_handle_auto_claim(platform_sa_auto_claim_switch_list)

Auto claim discovered switches based of seed switch

Autoclaim devices

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_sa_auto_claim_switch_list import PlatformSaAutoClaimSwitchList
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_sa_switch_async_claim_resp import PlatformSaSwitchAsyncClaimResp
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    platform_sa_auto_claim_switch_list = PlatformSaAutoClaimSwitchList(
        device_passwd="device_passwd_example",
        device_user_name="device_user_name_example",
        devices=[
            PlatformSaAutoClaimSwitchInfo(
                device_id="device_id_example",
                ip_address="ip_address_example",
                name="name_example",
                serial="serial_example",
                switch_type="switch_type_example",
            ),
        ],
        seed_device_id="seed_device_id_example",
    ) # PlatformSaAutoClaimSwitchList | 

    # example passing only required values which don't have defaults set
    try:
        # Auto claim discovered switches based of seed switch
        api_response = api_instance.platform_handle_auto_claim(platform_sa_auto_claim_switch_list)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_handle_auto_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_sa_auto_claim_switch_list** | [**PlatformSaAutoClaimSwitchList**](PlatformSaAutoClaimSwitchList.md)|  |

### Return type

[**PlatformSaSwitchAsyncClaimResp**](PlatformSaSwitchAsyncClaimResp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_handle_auto_claim_status**
> PlatformSaSwitchAsyncClaimResp platform_handle_auto_claim_status(req_id)

Query the status of an auto-claim request

Check the auto claim status given a request ID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_sa_switch_async_claim_resp import PlatformSaSwitchAsyncClaimResp
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    req_id = "reqId_example" # str | Request ID

    # example passing only required values which don't have defaults set
    try:
        # Query the status of an auto-claim request
        api_response = api_instance.platform_handle_auto_claim_status(req_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_handle_auto_claim_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req_id** | **str**| Request ID |

### Return type

[**PlatformSaSwitchAsyncClaimResp**](PlatformSaSwitchAsyncClaimResp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_handle_discover**
> PlatformSaDiscoverSwitchResp platform_handle_discover(seed_device_id)

Discover neighboring switches based on seed switch

Discover switches given a seed device ID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_sa_discover_switch_resp import PlatformSaDiscoverSwitchResp
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    seed_device_id = "seedDeviceId_example" # str | Seed device ID - Deprecating, change to seedDeviceID here and in path

    # example passing only required values which don't have defaults set
    try:
        # Discover neighboring switches based on seed switch
        api_response = api_instance.platform_handle_discover(seed_device_id)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_handle_discover: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seed_device_id** | **str**| Seed device ID - Deprecating, change to seedDeviceID here and in path |

### Return type

[**PlatformSaDiscoverSwitchResp**](PlatformSaDiscoverSwitchResp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_modify_site**
> platform_modify_site(id, platform_modify_info)

Modify a site based on sitename or UUID

Modify a site given an ID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_modify_info import PlatformModifyInfo
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    id = "id_example" # str | ID of site
    platform_modify_info = PlatformModifyInfo(
        device_id="device_id_example",
        devices=[
            PlatformDeviceInfo(
                device_id="device_id_example",
                name="name_example",
                role=PlatformSwitchRoles("Leaf"),
                seed=True,
            ),
        ],
        image_ref="image_ref_example",
        latitude="latitude_example",
        longitude="longitude_example",
        name="name_example",
        tier="tier_example",
    ) # PlatformModifyInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Modify a site based on sitename or UUID
        api_instance.platform_modify_site(id, platform_modify_info)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_modify_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of site |
 **platform_modify_info** | [**PlatformModifyInfo**](PlatformModifyInfo.md)|  |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_unclaim_device**
> platform_unclaim_device(id)

Unclaim a device based on its claimID

Unclaim a device

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    id = "id_example" # str | Device ID to delete

    # example passing only required values which don't have defaults set
    try:
        # Unclaim a device based on its claimID
        api_instance.platform_unclaim_device(id)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_unclaim_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device ID to delete |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_update_sa_switch**
> platform_update_sa_switch(site_id, device_id, platform_switch_update_info)

Modify standalone site's switch update

Update a standalone switch given a device ID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import site_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_switch_update_info import PlatformSwitchUpdateInfo
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See nexuscloud_client.signing for a list of all supported parameters.
configuration = nexuscloud_client.Configuration(
    host = "https://intersight.com",
    signing_info = nexuscloud_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = nexuscloud_client.signing.SCHEME_HS2019,
        signing_algorithm = nexuscloud_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = nexuscloud_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            nexuscloud_client.signing.HEADER_REQUEST_TARGET,
                            nexuscloud_client.signing.HEADER_CREATED,
                            nexuscloud_client.signing.HEADER_EXPIRES,
                            nexuscloud_client.signing.HEADER_HOST,
                            nexuscloud_client.signing.HEADER_DATE,
                            nexuscloud_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Enter a context with an instance of the API client
with nexuscloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = site_apis_api.SiteAPIsApi(api_client)
    site_id = "siteId_example" # str | Site ID - deprecating, change to siteID here and in path
    device_id = "deviceId_example" # str | Device ID - deprecating, change to deviceID here and in path
    platform_switch_update_info = PlatformSwitchUpdateInfo(
        role=PlatformSwitchRoles("Leaf"),
    ) # PlatformSwitchUpdateInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Modify standalone site's switch update
        api_instance.platform_update_sa_switch(site_id, device_id, platform_switch_update_info)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling SiteAPIsApi->platform_update_sa_switch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site ID - deprecating, change to siteID here and in path |
 **device_id** | **str**| Device ID - deprecating, change to deviceID here and in path |
 **platform_switch_update_info** | [**PlatformSwitchUpdateInfo**](PlatformSwitchUpdateInfo.md)|  |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

