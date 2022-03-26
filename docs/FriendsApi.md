# swagger_client.FriendsApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                     | HTTP request                                            | Description                  |
| -------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------- |
| [**create_friends_invitations**](FriendsApi.md#create_friends_invitations) | **POST** /1.1/user/-/friends/invitations                | Invite Friends               |
| [**get_friends**](FriendsApi.md#get_friends)                               | **GET** /1.1/user/-/friends.json                        | Get Friends                  |
| [**get_friends_invitations**](FriendsApi.md#get_friends_invitations)       | **GET** /1.1/user/-/friends/invitations.json            | Get Friend Invitations       |
| [**get_friends_leaderboard**](FriendsApi.md#get_friends_leaderboard)       | **GET** /1.1/user/-/leaderboard/friends.json            | Get Friends Leaderboard      |
| [**respond_friends_invitation**](FriendsApi.md#respond_friends_invitation) | **POST** /1.1/user/-/friends/invitations/{from-user-id} | Respond to Friend Invitation |

# **create_friends_invitations**

> create_friends_invitations(invited_user_email=invited_user_email, invited_user_id=invited_user_id)

Invite Friends

Creates an invitation to become friends with the authorized user. Either invitedUserEmail or invitedUserId needs to be provided.

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
api_instance = swagger_client.FriendsApi(swagger_client.ApiClient(configuration))
invited_user_email = 'invited_user_email_example' # str | Email of the user to invite. (optional)
invited_user_id = 'invited_user_id_example' # str | Encoded ID of the user to invite. (optional)

try:
    # Invite Friends
    api_instance.create_friends_invitations(invited_user_email=invited_user_email, invited_user_id=invited_user_id)
except ApiException as e:
    print("Exception when calling FriendsApi->create_friends_invitations: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                       | Notes      |
| ---------------------- | ------- | --------------------------------- | ---------- |
| **invited_user_email** | **str** | Email of the user to invite.      | [optional] |
| **invited_user_id**    | **str** | Encoded ID of the user to invite. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends**

> get_friends()

Get Friends

Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.FriendsApi(swagger_client.ApiClient(configuration))

try:
    # Get Friends
    api_instance.get_friends()
except ApiException as e:
    print("Exception when calling FriendsApi->get_friends: %s\n" % e)
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

# **get_friends_invitations**

> get_friends_invitations()

Get Friend Invitations

Returns a list of invitations to become friends with a user in the format requested.

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
api_instance = swagger_client.FriendsApi(swagger_client.ApiClient(configuration))

try:
    # Get Friend Invitations
    api_instance.get_friends_invitations()
except ApiException as e:
    print("Exception when calling FriendsApi->get_friends_invitations: %s\n" % e)
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

# **get_friends_leaderboard**

> get_friends_leaderboard()

Get Friends Leaderboard

Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.FriendsApi(swagger_client.ApiClient(configuration))

try:
    # Get Friends Leaderboard
    api_instance.get_friends_leaderboard()
except ApiException as e:
    print("Exception when calling FriendsApi->get_friends_leaderboard: %s\n" % e)
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

# **respond_friends_invitation**

> respond_friends_invitation(from_user_id, accept)

Respond to Friend Invitation

Accepts or rejects an invitation to become friends wit inviting user.

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
api_instance = swagger_client.FriendsApi(swagger_client.ApiClient(configuration))
from_user_id = 'from_user_id_example' # str | The encoded ID of a user from which to accept or reject invitation.
accept = 'accept_example' # str | Accept or reject invitation; true or false.

try:
    # Respond to Friend Invitation
    api_instance.respond_friends_invitation(from_user_id, accept)
except ApiException as e:
    print("Exception when calling FriendsApi->respond_friends_invitation: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                                                         | Notes |
| ---------------- | ------- | ------------------------------------------------------------------- | ----- |
| **from_user_id** | **str** | The encoded ID of a user from which to accept or reject invitation. |
| **accept**       | **str** | Accept or reject invitation; true or false.                         |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
