# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: accelbyte_cloud_py_codegen

# AccelByte Cloud Legal Service (1.25.1)

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

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model


class AcceptAgreementRequest(Model):
    """Accept agreement request (AcceptAgreementRequest)

    Properties:
        is_accepted: (isAccepted) REQUIRED bool

        localized_policy_version_id: (localizedPolicyVersionId) REQUIRED str

        policy_id: (policyId) REQUIRED str

        policy_version_id: (policyVersionId) REQUIRED str

        is_need_to_send_event_marketing: (isNeedToSendEventMarketing) OPTIONAL bool
    """

    # region fields

    is_accepted: bool  # REQUIRED
    localized_policy_version_id: str  # REQUIRED
    policy_id: str  # REQUIRED
    policy_version_id: str  # REQUIRED
    is_need_to_send_event_marketing: bool  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_is_accepted(self, value: bool) -> AcceptAgreementRequest:
        self.is_accepted = value
        return self

    def with_localized_policy_version_id(self, value: str) -> AcceptAgreementRequest:
        self.localized_policy_version_id = value
        return self

    def with_policy_id(self, value: str) -> AcceptAgreementRequest:
        self.policy_id = value
        return self

    def with_policy_version_id(self, value: str) -> AcceptAgreementRequest:
        self.policy_version_id = value
        return self

    def with_is_need_to_send_event_marketing(
        self, value: bool
    ) -> AcceptAgreementRequest:
        self.is_need_to_send_event_marketing = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "is_accepted"):
            result["isAccepted"] = bool(self.is_accepted)
        elif include_empty:
            result["isAccepted"] = False
        if hasattr(self, "localized_policy_version_id"):
            result["localizedPolicyVersionId"] = str(self.localized_policy_version_id)
        elif include_empty:
            result["localizedPolicyVersionId"] = ""
        if hasattr(self, "policy_id"):
            result["policyId"] = str(self.policy_id)
        elif include_empty:
            result["policyId"] = ""
        if hasattr(self, "policy_version_id"):
            result["policyVersionId"] = str(self.policy_version_id)
        elif include_empty:
            result["policyVersionId"] = ""
        if hasattr(self, "is_need_to_send_event_marketing"):
            result["isNeedToSendEventMarketing"] = bool(
                self.is_need_to_send_event_marketing
            )
        elif include_empty:
            result["isNeedToSendEventMarketing"] = False
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        is_accepted: bool,
        localized_policy_version_id: str,
        policy_id: str,
        policy_version_id: str,
        is_need_to_send_event_marketing: Optional[bool] = None,
    ) -> AcceptAgreementRequest:
        instance = cls()
        instance.is_accepted = is_accepted
        instance.localized_policy_version_id = localized_policy_version_id
        instance.policy_id = policy_id
        instance.policy_version_id = policy_version_id
        if is_need_to_send_event_marketing is not None:
            instance.is_need_to_send_event_marketing = is_need_to_send_event_marketing
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AcceptAgreementRequest:
        instance = cls()
        if not dict_:
            return instance
        if "isAccepted" in dict_ and dict_["isAccepted"] is not None:
            instance.is_accepted = bool(dict_["isAccepted"])
        elif include_empty:
            instance.is_accepted = False
        if (
            "localizedPolicyVersionId" in dict_
            and dict_["localizedPolicyVersionId"] is not None
        ):
            instance.localized_policy_version_id = str(
                dict_["localizedPolicyVersionId"]
            )
        elif include_empty:
            instance.localized_policy_version_id = ""
        if "policyId" in dict_ and dict_["policyId"] is not None:
            instance.policy_id = str(dict_["policyId"])
        elif include_empty:
            instance.policy_id = ""
        if "policyVersionId" in dict_ and dict_["policyVersionId"] is not None:
            instance.policy_version_id = str(dict_["policyVersionId"])
        elif include_empty:
            instance.policy_version_id = ""
        if (
            "isNeedToSendEventMarketing" in dict_
            and dict_["isNeedToSendEventMarketing"] is not None
        ):
            instance.is_need_to_send_event_marketing = bool(
                dict_["isNeedToSendEventMarketing"]
            )
        elif include_empty:
            instance.is_need_to_send_event_marketing = False
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, AcceptAgreementRequest]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[AcceptAgreementRequest]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        AcceptAgreementRequest,
        List[AcceptAgreementRequest],
        Dict[Any, AcceptAgreementRequest],
    ]:
        if many:
            if isinstance(any_, dict):
                return cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                return cls.create_many_from_list(any_, include_empty=include_empty)
            else:
                raise ValueError()
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "isAccepted": "is_accepted",
            "localizedPolicyVersionId": "localized_policy_version_id",
            "policyId": "policy_id",
            "policyVersionId": "policy_version_id",
            "isNeedToSendEventMarketing": "is_need_to_send_event_marketing",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "isAccepted": True,
            "localizedPolicyVersionId": True,
            "policyId": True,
            "policyVersionId": True,
            "isNeedToSendEventMarketing": False,
        }

    # endregion static methods
