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

# AccelByte Cloud Lobby Server (staging)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HeaderStr
from .....core import HttpResponse

from ...models import ResponseError


class AdminExportConfigV1(Operation):
    """Export lobby config to a json file. (adminExportConfigV1)


        Required permission ADMIN:NAMESPACE:{namespace}:LOBBY:CONFIG [READ]

        Required Scope: social

        Export lobby configuration to a json file. The file can then be imported from the /import endpoint.

        JSON Schema of the exported file:
        {"required":["namespace","entitlementItemID","chatRateLimitDuration","generalRateLimitDuration","autoKickOnDisconnectDelay","chatRateLimitBurst","generalRateLimitBurst","maxPartyMember","autoKickOnDisconnect","profanityFilter","enableChat","entitlementCheck","cancelTicketOnDisconnect","concurrentUsersLimit","readyConsentTimeout","disableInvitationOnJoinParty","allowJoinPartyDuringMatchmaking","allowInviteNonConnectedUser","keepPresenceActivityOnDisconnect","maxDSWaitTime"],"properties":{"allowInviteNonConnectedUser":{"type":"boolean"},"allowJoinPartyDuringMatchmaking":{"type":"boolean"},"autoKickOnDisconnect":{"type":"boolean"},"autoKickOnDisconnectDelay":{"type":"integer","format":"integer"},"cancelTicketOnDisconnect":{"type":"boolean"},"chatRateLimitBurst":{"type":"integer","format":"int32"},"chatRateLimitDuration":{"type":"integer","format":"integer"},"concurrentUsersLimit":{"type":"integer","format":"int32"},"disableInvitationOnJoinParty":{"type":"boolean"},"enableChat":{"type":"boolean"},"entitlementCheck":{"type":"boolean"},"entitlementItemID":{"type":"string"},"generalRateLimitBurst":{"type":"integer","format":"int32"},"generalRateLimitDuration":{"type":"integer","format":"integer"},"keepPresenceActivityOnDisconnect":{"type":"boolean"},"maxDSWaitTime":{"type":"integer","format":"integer"},"maxPartyMember":{"type":"integer","format":"int32"},"namespace":{"type":"string"},"profanityFilter":{"type":"boolean"},"readyConsentTimeout":{"type":"integer","format":"integer"}}}

        Required Permission(s):
            - ADMIN:NAMESPACE:{namespace}:LOBBY:CONFIG [READ]

        Required Scope(s):
            - social

        Properties:
            url: /lobby/v1/admin/config/namespaces/{namespace}/export

            method: GET

            tags: ["config"]

            consumes: []

            produces: ["application/json"]

            securities: [BEARER_AUTH]

            namespace: (namespace) REQUIRED str in path

        Responses:
            200: OK - Any (OK
    JSON Schema of the exported file:
    {"required":["namespace","entitlementItemID","chatRateLimitDuration","generalRateLimitDuration","autoKickOnDisconnectDelay","chatRateLimitBurst","generalRateLimitBurst","maxPartyMember","autoKickOnDisconnect","profanityFilter","enableChat","entitlementCheck","cancelTicketOnDisconnect","concurrentUsersLimit","readyConsentTimeout","disableInvitationOnJoinParty","allowJoinPartyDuringMatchmaking","allowInviteNonConnectedUser","keepPresenceActivityOnDisconnect","maxDSWaitTime"],"properties":{"allowInviteNonConnectedUser":{"type":"boolean"},"allowJoinPartyDuringMatchmaking":{"type":"boolean"},"autoKickOnDisconnect":{"type":"boolean"},"autoKickOnDisconnectDelay":{"type":"integer","format":"integer"},"cancelTicketOnDisconnect":{"type":"boolean"},"chatRateLimitBurst":{"type":"integer","format":"int32"},"chatRateLimitDuration":{"type":"integer","format":"integer"},"concurrentUsersLimit":{"type":"integer","format":"int32"},"disableInvitationOnJoinParty":{"type":"boolean"},"enableChat":{"type":"boolean"},"entitlementCheck":{"type":"boolean"},"entitlementItemID":{"type":"string"},"generalRateLimitBurst":{"type":"integer","format":"int32"},"generalRateLimitDuration":{"type":"integer","format":"integer"},"keepPresenceActivityOnDisconnect":{"type":"boolean"},"maxDSWaitTime":{"type":"integer","format":"integer"},"maxPartyMember":{"type":"integer","format":"int32"},"namespace":{"type":"string"},"profanityFilter":{"type":"boolean"},"readyConsentTimeout":{"type":"integer","format":"integer"}}})

            401: Unauthorized - ResponseError (Unauthorized)

            403: Forbidden - ResponseError (Forbidden)

            500: Internal Server Error - ResponseError (Internal Server Error)
    """

    # region fields

    _url: str = "/lobby/v1/admin/config/namespaces/{namespace}/export"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"]]
    _location_query: str = None

    namespace: str  # REQUIRED in [path]

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
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> AdminExportConfigV1:
        self.namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[Union[None, Any], Union[None, HttpResponse, ResponseError]]:
        """Parse the given response.

                200: OK - Any (OK
        JSON Schema of the exported file:
        {"required":["namespace","entitlementItemID","chatRateLimitDuration","generalRateLimitDuration","autoKickOnDisconnectDelay","chatRateLimitBurst","generalRateLimitBurst","maxPartyMember","autoKickOnDisconnect","profanityFilter","enableChat","entitlementCheck","cancelTicketOnDisconnect","concurrentUsersLimit","readyConsentTimeout","disableInvitationOnJoinParty","allowJoinPartyDuringMatchmaking","allowInviteNonConnectedUser","keepPresenceActivityOnDisconnect","maxDSWaitTime"],"properties":{"allowInviteNonConnectedUser":{"type":"boolean"},"allowJoinPartyDuringMatchmaking":{"type":"boolean"},"autoKickOnDisconnect":{"type":"boolean"},"autoKickOnDisconnectDelay":{"type":"integer","format":"integer"},"cancelTicketOnDisconnect":{"type":"boolean"},"chatRateLimitBurst":{"type":"integer","format":"int32"},"chatRateLimitDuration":{"type":"integer","format":"integer"},"concurrentUsersLimit":{"type":"integer","format":"int32"},"disableInvitationOnJoinParty":{"type":"boolean"},"enableChat":{"type":"boolean"},"entitlementCheck":{"type":"boolean"},"entitlementItemID":{"type":"string"},"generalRateLimitBurst":{"type":"integer","format":"int32"},"generalRateLimitDuration":{"type":"integer","format":"integer"},"keepPresenceActivityOnDisconnect":{"type":"boolean"},"maxDSWaitTime":{"type":"integer","format":"integer"},"maxPartyMember":{"type":"integer","format":"int32"},"namespace":{"type":"string"},"profanityFilter":{"type":"boolean"},"readyConsentTimeout":{"type":"integer","format":"integer"}}})

                401: Unauthorized - ResponseError (Unauthorized)

                403: Forbidden - ResponseError (Forbidden)

                500: Internal Server Error - ResponseError (Internal Server Error)

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
            return content, None
        if code == 401:
            return None, ResponseError.create_from_dict(content)
        if code == 403:
            return None, ResponseError.create_from_dict(content)
        if code == 500:
            return None, ResponseError.create_from_dict(content)

        return self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
    ) -> AdminExportConfigV1:
        instance = cls()
        instance.namespace = namespace
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AdminExportConfigV1:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "namespace": True,
        }

    # endregion static methods
