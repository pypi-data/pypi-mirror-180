# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: accelbyte_cloud_py_codegen

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

# AccelByte Cloud Iam Service (5.22.0)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HeaderStr
from .....core import HttpResponse

from ...models import OauthmodelErrorResponse
from ...models import OauthmodelTokenResponse


class PlatformTokenGrantV3(Operation):
    """OAuth2 access token generation specific to platform (PlatformTokenGrantV3)

    Platform token grant specifically used for performing token grant using platform, e.g. Steam, Justice, etc. The endpoint automatically create an account if the account associated with the platform is not exists yet.
    This endpoint requires all requests to have Authorization header set with Basic access authentication
    constructed from client id and client secret. For publisher-game namespace schema : Specify only either platform_token or device_id. Device token grant
    should be requested along with device_id parameter against game namespace. Another 3rd party platform token grant should be requested
    along with platform_token parameter against publisher namespace.





    ## 2FA remember device




    To remember device for 2FA, should provide cookie: device_token or header: Device-Token




    ## Supported platforms:






      * steam : The platform_tokenâs value is the authentication code returned by Steam.


      * steamopenid : Steam's user authentication method using OpenID 2.0. The platform_token's value is URL generated by Steam on web authentication


      * facebook : The platform_tokenâs value is the authorization code returned by Facebook OAuth


      * google : The platform_tokenâs value is the authorization code returned by Google OAuth


      * oculus : The platform_tokenâs value is a string composed of Oculus's user ID and the nonce separated by a colon (:).


      * twitch : The platform_tokenâs value is the authorization code returned by Twitch OAuth.


      * discord : The platform_tokenâs value is the authorization code returned by Discord OAuth


      * android : The device_id is the Androidâs device ID


      * ios : The device_id is the iOSâs device ID.


      * apple : The platform_tokenâs value is the authorization code returned by Apple OAuth.(We will use this code to generate APP token)


      * device : Every device that doesânt run Android and iOS is categorized as a device. The device_id is the deviceâs ID.


      * justice : The platform_tokenâs value is the designated userâs access token.


      * epicgames : The platform_tokenâs value is an access-token obtained from Epicgames EOS Account Service.


      * stadia : The platform_token's value is a JWT Token, which can be obtained after calling the Stadia SDK's function.


      * ps4 : The platform_tokenâs value is the authorization code returned by Sony OAuth.


      * ps5 : The platform_tokenâs value is the authorization code returned by Sony OAuth.


      * nintendo : The platform_tokenâs value is the authorization code(id_token) returned by Nintendo OAuth.


      * awscognito : The platform_tokenâs value is the aws cognito access token or id token (JWT).


      * live : The platform_tokenâs value is xbox XSTS token


      * xblweb : The platform_tokenâs value is code returned by xbox after login


      * netflix : The platform_tokenâs value is GAT (Gamer Access Token) returned by Netflix backend


      * snapchat : The platform_tokenâs value is the authorization code returned by Snapchat OAuth.





    ## Account Group




    Several platforms are grouped under account groups. The accounts on these platforms have the same platform user id.
    Login using one of these platform will returns the same IAM user.




    Following is the current registered account grouping:






      * (psn) ps4web


      * (psn) ps4


      * (psn) ps5





    ## Access Token Content




    Following is the access tokenâs content:






      *


    namespace. It is the namespace the token was generated from.





      *


    display_name. The display name of the sub. It is empty if the token is generated from the client credential





      *


    roles. The subâs roles. It is empty if the token is generated from the client credential





      *


    namespace_roles. The subâs roles scoped to namespace. Improvement from roles, which make the role scoped to specific namespace instead of global to publisher namespace





      *


    permissions. The sub or audâ permissions





      *


    bans. The subâs list of bans. It is used by the IAM client for validating the token.





      *


    jflgs. It stands for Justice Flags. It is a special flag used for storing additional status information regarding the sub. It is implemented as a bit mask. Following explains what each bit represents:




        * 1: Email Address Verified



        * 2: Phone Number Verified



        * 4: Anonymous



        * 8: Suspicious Login






      *


    aud. The aud is the client ID.





      *


    iat. The time the token issues at. It is in Epoch time format





      *


    exp. The time the token expires. It is in Epoch time format





      *


    sub. The UserID. The sub is omitted if the token is generated from client credential






    ## Bans




    The JWT contains user's active bans with its expiry date. List of ban types can be obtained from /bans.



    action code : 10704

    Properties:
        url: /iam/v3/oauth/platforms/{platformId}/token

        method: POST

        tags: ["OAuth2.0"]

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        securities: [BASIC_AUTH]

        client_id: (client_id) OPTIONAL str in form_data

        create_headless: (createHeadless) OPTIONAL bool in form_data

        device_id: (device_id) OPTIONAL str in form_data

        mac_address: (macAddress) OPTIONAL str in form_data

        platform_token: (platform_token) OPTIONAL str in form_data

        platform_id: (platformId) REQUIRED str in path

    Responses:
        200: OK - OauthmodelTokenResponse (Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)

        403: Forbidden - OauthmodelErrorResponse (Forbidden)
    """

    # region fields

    _url: str = "/iam/v3/oauth/platforms/{platformId}/token"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BASIC_AUTH"]]
    _location_query: str = None

    client_id: str  # OPTIONAL in [form_data]
    create_headless: bool  # OPTIONAL in [form_data]
    device_id: str  # OPTIONAL in [form_data]
    mac_address: str  # OPTIONAL in [form_data]
    platform_token: str  # OPTIONAL in [form_data]
    platform_id: str  # REQUIRED in [path]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def securities(self) -> List[List[str]]:
        return self._securities

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "form_data": self.get_form_data_params(),
            "path": self.get_path_params(),
        }

    def get_form_data_params(self) -> dict:
        result = {}
        if hasattr(self, "client_id"):
            result["client_id"] = self.client_id
        if hasattr(self, "create_headless"):
            result["createHeadless"] = self.create_headless
        if hasattr(self, "device_id"):
            result["device_id"] = self.device_id
        if hasattr(self, "mac_address"):
            result["macAddress"] = self.mac_address
        if hasattr(self, "platform_token"):
            result["platform_token"] = self.platform_token
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_client_id(self, value: str) -> PlatformTokenGrantV3:
        self.client_id = value
        return self

    def with_create_headless(self, value: bool) -> PlatformTokenGrantV3:
        self.create_headless = value
        return self

    def with_device_id(self, value: str) -> PlatformTokenGrantV3:
        self.device_id = value
        return self

    def with_mac_address(self, value: str) -> PlatformTokenGrantV3:
        self.mac_address = value
        return self

    def with_platform_token(self, value: str) -> PlatformTokenGrantV3:
        self.platform_token = value
        return self

    def with_platform_id(self, value: str) -> PlatformTokenGrantV3:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "client_id") and self.client_id:
            result["client_id"] = str(self.client_id)
        elif include_empty:
            result["client_id"] = ""
        if hasattr(self, "create_headless") and self.create_headless:
            result["createHeadless"] = bool(self.create_headless)
        elif include_empty:
            result["createHeadless"] = False
        if hasattr(self, "device_id") and self.device_id:
            result["device_id"] = str(self.device_id)
        elif include_empty:
            result["device_id"] = ""
        if hasattr(self, "mac_address") and self.mac_address:
            result["macAddress"] = str(self.mac_address)
        elif include_empty:
            result["macAddress"] = ""
        if hasattr(self, "platform_token") and self.platform_token:
            result["platform_token"] = str(self.platform_token)
        elif include_empty:
            result["platform_token"] = ""
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[
        Union[None, OauthmodelTokenResponse],
        Union[None, HttpResponse, OauthmodelErrorResponse],
    ]:
        """Parse the given response.

        200: OK - OauthmodelTokenResponse (Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)

        403: Forbidden - OauthmodelErrorResponse (Forbidden)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(
            code=code, content_type=content_type, content=content
        )
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return OauthmodelTokenResponse.create_from_dict(content), None
        if code == 400:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        if code == 401:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        if code == 403:
            return None, OauthmodelErrorResponse.create_from_dict(content)

        return self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        platform_id: str,
        client_id: Optional[str] = None,
        create_headless: Optional[bool] = None,
        device_id: Optional[str] = None,
        mac_address: Optional[str] = None,
        platform_token: Optional[str] = None,
    ) -> PlatformTokenGrantV3:
        instance = cls()
        instance.platform_id = platform_id
        if client_id is not None:
            instance.client_id = client_id
        if create_headless is not None:
            instance.create_headless = create_headless
        if device_id is not None:
            instance.device_id = device_id
        if mac_address is not None:
            instance.mac_address = mac_address
        if platform_token is not None:
            instance.platform_token = platform_token
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> PlatformTokenGrantV3:
        instance = cls()
        if "client_id" in dict_ and dict_["client_id"] is not None:
            instance.client_id = str(dict_["client_id"])
        elif include_empty:
            instance.client_id = ""
        if "createHeadless" in dict_ and dict_["createHeadless"] is not None:
            instance.create_headless = bool(dict_["createHeadless"])
        elif include_empty:
            instance.create_headless = False
        if "device_id" in dict_ and dict_["device_id"] is not None:
            instance.device_id = str(dict_["device_id"])
        elif include_empty:
            instance.device_id = ""
        if "macAddress" in dict_ and dict_["macAddress"] is not None:
            instance.mac_address = str(dict_["macAddress"])
        elif include_empty:
            instance.mac_address = ""
        if "platform_token" in dict_ and dict_["platform_token"] is not None:
            instance.platform_token = str(dict_["platform_token"])
        elif include_empty:
            instance.platform_token = ""
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "client_id": "client_id",
            "createHeadless": "create_headless",
            "device_id": "device_id",
            "macAddress": "mac_address",
            "platform_token": "platform_token",
            "platformId": "platform_id",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "client_id": False,
            "createHeadless": False,
            "device_id": False,
            "macAddress": False,
            "platform_token": False,
            "platformId": True,
        }

    # endregion static methods
