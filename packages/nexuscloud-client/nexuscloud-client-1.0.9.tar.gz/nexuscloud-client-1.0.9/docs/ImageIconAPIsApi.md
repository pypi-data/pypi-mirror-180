# nexuscloud_client.ImageIconAPIsApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_add_site_icon**](ImageIconAPIsApi.md#platform_add_site_icon) | **POST** /nexus/platform/api/v1/imageIcons | Upload a site&#39;s image Icon
[**platform_delete_image_icon**](ImageIconAPIsApi.md#platform_delete_image_icon) | **DELETE** /nexus/platform/api/v1/imageIcons/{uuid} | Delete a site&#39;s image icon based on UUID
[**platform_get_image_icon**](ImageIconAPIsApi.md#platform_get_image_icon) | **GET** /nexus/platform/api/v1/imageIcons/{uuid} | Get a site&#39;s image icon based on UUID
[**platform_modify_image_icon**](ImageIconAPIsApi.md#platform_modify_image_icon) | **PUT** /nexus/platform/api/v1/imageIcons/{uuid} | Modify an site&#39;s image icon based on UUID


# **platform_add_site_icon**
> PlatformImageIconResp platform_add_site_icon(body)

Upload a site's image Icon

Add an image icon for a site

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import image_icon_apis_api
from nexuscloud_client.model.platform_error_response import PlatformErrorResponse
from nexuscloud_client.model.platform_image_icon_resp import PlatformImageIconResp
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
    api_instance = image_icon_apis_api.ImageIconAPIsApi(api_client)
    body = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Upload a site's image Icon
        api_response = api_instance.platform_add_site_icon(body)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ImageIconAPIsApi->platform_add_site_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file_type**|  |

### Return type

[**PlatformImageIconResp**](PlatformImageIconResp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_delete_image_icon**
> platform_delete_image_icon(uuid)

Delete a site's image icon based on UUID

Delete an image icon given a UUID

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import image_icon_apis_api
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
    api_instance = image_icon_apis_api.ImageIconAPIsApi(api_client)
    uuid = "uuid_example" # str | UUID of site

    # example passing only required values which don't have defaults set
    try:
        # Delete a site's image icon based on UUID
        api_instance.platform_delete_image_icon(uuid)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ImageIconAPIsApi->platform_delete_image_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of site |

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

# **platform_get_image_icon**
> file_type platform_get_image_icon(uuid)

Get a site's image icon based on UUID

Get the image icon for a site

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import image_icon_apis_api
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
    api_instance = image_icon_apis_api.ImageIconAPIsApi(api_client)
    uuid = "uuid_example" # str | UUID of site

    # example passing only required values which don't have defaults set
    try:
        # Get a site's image icon based on UUID
        api_response = api_instance.platform_get_image_icon(uuid)
        pprint(api_response)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ImageIconAPIsApi->platform_get_image_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of site |

### Return type

**file_type**

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_modify_image_icon**
> platform_modify_image_icon(uuid, body)

Modify an site's image icon based on UUID

Modify the image icon of a site

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import nexuscloud_client
from nexuscloud_client.api import image_icon_apis_api
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
    api_instance = image_icon_apis_api.ImageIconAPIsApi(api_client)
    uuid = "uuid_example" # str | UUID of a site
    body = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Modify an site's image icon based on UUID
        api_instance.platform_modify_image_icon(uuid, body)
    except nexuscloud_client.ApiException as e:
        print("Exception when calling ImageIconAPIsApi->platform_modify_image_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of a site |
 **body** | **file_type**|  |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature)

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4xx** | Bad request |  -  |
**5xx** | Internal Server Error |  -  |
**0** | Default error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

