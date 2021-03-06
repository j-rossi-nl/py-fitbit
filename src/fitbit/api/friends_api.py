"""
    Fitbit Web API

    Fitbit provides a Web API for accessing data from Fitbit activity trackers, Aria scale, and manually entered logs. Anyone can develop an application to access and modify a Fitbit user's data on their behalf, so long as it complies with Fitbit Platform Terms of Service. These Swagger UI docs do not currently support making Fitbit API requests directly. In order to make a request, construct a request for the appropriate endpoint using this documentation, and then add an Authorization header to each request with an access token obtained using the steps outlined here: https://dev.fitbit.com/build/reference/web-api/oauth2/#obtaining-consent.  # noqa: E501

    OpenAPI spec version: 1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fitbit.api_client import ApiClient


class FriendsApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_friends_invitations(self, **kwargs):  # noqa: E501
        """Invite Friends  # noqa: E501

        Creates an invitation to become friends with the authorized user.  Either invitedUserEmail or invitedUserId needs to be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_friends_invitations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invited_user_email: Email of the user to invite.
        :param str invited_user_id: Encoded ID of the user to invite.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_friends_invitations_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_friends_invitations_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def create_friends_invitations_with_http_info(self, **kwargs):  # noqa: E501
        """Invite Friends  # noqa: E501

        Creates an invitation to become friends with the authorized user.  Either invitedUserEmail or invitedUserId needs to be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_friends_invitations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invited_user_email: Email of the user to invite.
        :param str invited_user_id: Encoded ID of the user to invite.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["invited_user_email", "invited_user_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_friends_invitations" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "invited_user_email" in params:
            query_params.append(
                ("invitedUserEmail", params["invited_user_email"])
            )  # noqa: E501
        if "invited_user_id" in params:
            query_params.append(
                ("invitedUserId", params["invited_user_id"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.1/user/-/friends/invitations",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_friends(self, **kwargs):  # noqa: E501
        """Get Friends  # noqa: E501

        Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_friends(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_friends_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_friends_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_friends_with_http_info(self, **kwargs):  # noqa: E501
        """Get Friends  # noqa: E501

        Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_friends_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_friends" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.1/user/-/friends.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_friends_invitations(self, **kwargs):  # noqa: E501
        """Get Friend Invitations  # noqa: E501

        Returns a list of invitations to become friends with a user in the format requested.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_friends_invitations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_friends_invitations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_friends_invitations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_friends_invitations_with_http_info(self, **kwargs):  # noqa: E501
        """Get Friend Invitations  # noqa: E501

        Returns a list of invitations to become friends with a user in the format requested.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_friends_invitations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_friends_invitations" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.1/user/-/friends/invitations.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_friends_leaderboard(self, **kwargs):  # noqa: E501
        """Get Friends Leaderboard  # noqa: E501

        Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_friends_leaderboard(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_friends_leaderboard_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_friends_leaderboard_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_friends_leaderboard_with_http_info(self, **kwargs):  # noqa: E501
        """Get Friends Leaderboard  # noqa: E501

        Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_friends_leaderboard_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_friends_leaderboard" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.1/user/-/leaderboard/friends.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def respond_friends_invitation(self, from_user_id, accept, **kwargs):  # noqa: E501
        """Respond to Friend Invitation  # noqa: E501

        Accepts or rejects an invitation to become friends wit inviting user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.respond_friends_invitation(from_user_id, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str from_user_id: The encoded ID of a user from which to accept or reject invitation. (required)
        :param str accept: Accept or reject invitation; true or false. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.respond_friends_invitation_with_http_info(
                from_user_id, accept, **kwargs
            )  # noqa: E501
        else:
            (data) = self.respond_friends_invitation_with_http_info(
                from_user_id, accept, **kwargs
            )  # noqa: E501
            return data

    def respond_friends_invitation_with_http_info(
        self, from_user_id, accept, **kwargs
    ):  # noqa: E501
        """Respond to Friend Invitation  # noqa: E501

        Accepts or rejects an invitation to become friends wit inviting user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.respond_friends_invitation_with_http_info(from_user_id, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str from_user_id: The encoded ID of a user from which to accept or reject invitation. (required)
        :param str accept: Accept or reject invitation; true or false. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["from_user_id", "accept"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method respond_friends_invitation" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'from_user_id' is set
        if "from_user_id" not in params or params["from_user_id"] is None:
            raise ValueError(
                "Missing the required parameter `from_user_id` when calling `respond_friends_invitation`"
            )  # noqa: E501
        # verify the required parameter 'accept' is set
        if "accept" not in params or params["accept"] is None:
            raise ValueError(
                "Missing the required parameter `accept` when calling `respond_friends_invitation`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_user_id" in params:
            path_params["from-user-id"] = params["from_user_id"]  # noqa: E501

        query_params = []
        if "accept" in params:
            query_params.append(("accept", params["accept"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.1/user/-/friends/invitations/{from-user-id}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
