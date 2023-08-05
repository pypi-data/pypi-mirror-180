# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: accelbyte_cloud_py_codegen

# AccelByte Cloud Platform Service (4.18.1)

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

from ..models.platform_reward import PlatformReward


class DLCItem(Model):
    """DLC item (DLCItem)

    Properties:
        id_: (id) OPTIONAL str

        rewards: (rewards) OPTIONAL List[PlatformReward]
    """

    # region fields

    id_: str  # OPTIONAL
    rewards: List[PlatformReward]  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_id(self, value: str) -> DLCItem:
        self.id_ = value
        return self

    def with_rewards(self, value: List[PlatformReward]) -> DLCItem:
        self.rewards = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "id_"):
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = ""
        if hasattr(self, "rewards"):
            result["rewards"] = [
                i0.to_dict(include_empty=include_empty) for i0 in self.rewards
            ]
        elif include_empty:
            result["rewards"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        id_: Optional[str] = None,
        rewards: Optional[List[PlatformReward]] = None,
    ) -> DLCItem:
        instance = cls()
        if id_ is not None:
            instance.id_ = id_
        if rewards is not None:
            instance.rewards = rewards
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> DLCItem:
        instance = cls()
        if not dict_:
            return instance
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = ""
        if "rewards" in dict_ and dict_["rewards"] is not None:
            instance.rewards = [
                PlatformReward.create_from_dict(i0, include_empty=include_empty)
                for i0 in dict_["rewards"]
            ]
        elif include_empty:
            instance.rewards = []
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, DLCItem]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[DLCItem]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[DLCItem, List[DLCItem], Dict[Any, DLCItem]]:
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
            "id": "id_",
            "rewards": "rewards",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "id": False,
            "rewards": False,
        }

    # endregion static methods
