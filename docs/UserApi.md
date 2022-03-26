# swagger_client.UserApi

All URIs are relative to *https://api.fitbit.com*

| Method                                          | HTTP request                    | Description    |
| ----------------------------------------------- | ------------------------------- | -------------- |
| [**get_badges**](UserApi.md#get_badges)         | **GET** /1/user/-/badges.json   | Get Badges     |
| [**get_profile**](UserApi.md#get_profile)       | **GET** /1/user/-/profile.json  | Get Profile    |
| [**update_profile**](UserApi.md#update_profile) | **POST** /1/user/-/profile.json | Update Profile |

# **get_badges**

> get_badges()

Get Badges

Retrieves the user's badges in the format requested. Response includes all badges for the user as seen on the Fitbit website badge locker (both activity and weight related.) The endpoint returns weight and distance badges based on the user's unit profile preference as on the website.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get Badges
    api_instance.get_badges()
except ApiException as e:
    print("Exception when calling UserApi->get_badges: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**

> get_profile()

Get Profile

Returns a user's profile. The authenticated owner receives all values. However, the authenticated user's access to other users' data is subject to those users' privacy settings. Numerical values are returned in the unit system specified in the Accept-Language header.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Get Profile
    api_instance.get_profile()
except ApiException as e:
    print("Exception when calling UserApi->get_profile: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**

> update_profile(gender=gender, birthday=birthday, height=height, about_me=about_me, fullname=fullname, country=country, state=state, city=city, stride_length_walking=stride_length_walking, stride_length_running=stride_length_running, weight_unit=weight_unit, height_unit=height_unit, water_unit=water_unit, glucose_unit=glucose_unit, timezone=timezone, foods_locale=foods_locale, locale=locale, locale_lang=locale_lang, locale_country=locale_country, start_day_of_week=start_day_of_week)

Update Profile

Updates a user's profile using a form.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
gender = 'gender_example' # str | The sex of the user; (MALE/FEMALE/NA). (optional)
birthday = '2013-10-20' # date | The date of birth in the format of yyyy-MM-dd. (optional)
height = 'height_example' # str | The height in the format X.XX in the unit system that corresponds to the Accept-Language header provided. (optional)
about_me = 'about_me_example' # str | This is a short description of user. (optional)
fullname = 'fullname_example' # str | The fullname of the user. (optional)
country = 'country_example' # str | The country of the user's residence. This is a two-character code. (optional)
state = 'state_example' # str | The US state of the user's residence. This is a two-character code if the country was or is set to US. (optional)
city = 'city_example' # str | The US city of the user's residence. (optional)
stride_length_walking = 'stride_length_walking_example' # str | Walking stride length in the format X.XX, where it is in the unit system that corresponds to the Accept-Language header provided. (optional)
stride_length_running = 'stride_length_running_example' # str | Running stride length in the format X.XX, where it is in the unit system that corresponds to the Accept-Language header provided. (optional)
weight_unit = 'weight_unit_example' # str | Default weight unit on website (which doesn't affect API); one of (en_US, en_GB, 'any' for METRIC). (optional)
height_unit = 'height_unit_example' # str | Default height/distance unit on website (which doesn't affect API); one of (en_US, en_GB, 'any' for METRIC). (optional)
water_unit = 'water_unit_example' # str | Default water unit on website (which doesn't affect API); one of (en_US, en_GB, 'any' for METRIC). (optional)
glucose_unit = 'glucose_unit_example' # str | Default glucose unit on website (which doesn't affect API); one of (en_US, en_GB, 'any' for METRIC). (optional)
timezone = 'timezone_example' # str | The timezone in the format 'America/Los_Angeles'. (optional)
foods_locale = 'foods_locale_example' # str | The food database locale in the format of xx.XX. (optional)
locale = 'locale_example' # str | The locale of the website (country/language); one of the locales, currently – (en_US, fr_FR, de_DE, es_ES, en_GB, en_AU, en_NZ, ja_JP). (optional)
locale_lang = 'locale_lang_example' # str | The Language in the format 'xx'. You should specify either locale or both - localeLang and localeCountry (locale is higher priority). (optional)
locale_country = 'locale_country_example' # str | The Country in the format 'xx'. You should specify either locale or both - localeLang and localeCountry (locale is higher priority). (optional)
start_day_of_week = 'start_day_of_week_example' # str | The Start day of the week, meaning what day the week should start on. Either Sunday or Monday. (optional)

try:
    # Update Profile
    api_instance.update_profile(gender=gender, birthday=birthday, height=height, about_me=about_me, fullname=fullname, country=country, state=state, city=city, stride_length_walking=stride_length_walking, stride_length_running=stride_length_running, weight_unit=weight_unit, height_unit=height_unit, water_unit=water_unit, glucose_unit=glucose_unit, timezone=timezone, foods_locale=foods_locale, locale=locale, locale_lang=locale_lang, locale_country=locale_country, start_day_of_week=start_day_of_week)
except ApiException as e:
    print("Exception when calling UserApi->update_profile: %s\n" % e)
```

### Parameters

| Name                      | Type     | Description                                                                                                                                   | Notes      |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **gender**                | **str**  | The sex of the user; (MALE/FEMALE/NA).                                                                                                        | [optional] |
| **birthday**              | **date** | The date of birth in the format of yyyy-MM-dd.                                                                                                | [optional] |
| **height**                | **str**  | The height in the format X.XX in the unit system that corresponds to the Accept-Language header provided.                                     | [optional] |
| **about_me**              | **str**  | This is a short description of user.                                                                                                          | [optional] |
| **fullname**              | **str**  | The fullname of the user.                                                                                                                     | [optional] |
| **country**               | **str**  | The country of the user&#39;s residence. This is a two-character code.                                                                        | [optional] |
| **state**                 | **str**  | The US state of the user&#39;s residence. This is a two-character code if the country was or is set to US.                                    | [optional] |
| **city**                  | **str**  | The US city of the user&#39;s residence.                                                                                                      | [optional] |
| **stride_length_walking** | **str**  | Walking stride length in the format X.XX, where it is in the unit system that corresponds to the Accept-Language header provided.             | [optional] |
| **stride_length_running** | **str**  | Running stride length in the format X.XX, where it is in the unit system that corresponds to the Accept-Language header provided.             | [optional] |
| **weight_unit**           | **str**  | Default weight unit on website (which doesn&#39;t affect API); one of (en_US, en_GB, &#39;any&#39; for METRIC).                               | [optional] |
| **height_unit**           | **str**  | Default height/distance unit on website (which doesn&#39;t affect API); one of (en_US, en_GB, &#39;any&#39; for METRIC).                      | [optional] |
| **water_unit**            | **str**  | Default water unit on website (which doesn&#39;t affect API); one of (en_US, en_GB, &#39;any&#39; for METRIC).                                | [optional] |
| **glucose_unit**          | **str**  | Default glucose unit on website (which doesn&#39;t affect API); one of (en_US, en_GB, &#39;any&#39; for METRIC).                              | [optional] |
| **timezone**              | **str**  | The timezone in the format &#39;America/Los_Angeles&#39;.                                                                                     | [optional] |
| **foods_locale**          | **str**  | The food database locale in the format of xx.XX.                                                                                              | [optional] |
| **locale**                | **str**  | The locale of the website (country/language); one of the locales, currently – (en_US, fr_FR, de_DE, es_ES, en_GB, en_AU, en_NZ, ja_JP).       | [optional] |
| **locale_lang**           | **str**  | The Language in the format &#39;xx&#39;. You should specify either locale or both - localeLang and localeCountry (locale is higher priority). | [optional] |
| **locale_country**        | **str**  | The Country in the format &#39;xx&#39;. You should specify either locale or both - localeLang and localeCountry (locale is higher priority).  | [optional] |
| **start_day_of_week**     | **str**  | The Start day of the week, meaning what day the week should start on. Either Sunday or Monday.                                                | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
