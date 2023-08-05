# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: accelbyte_cloud_py_codegen

# AccelByte Cloud Session Browser Service ()

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


class ModelsMatchAttributes(Model):
    """Models match attributes (models.MatchAttributes)

    Properties:
        first_ticket_created_at: (first_ticket_created_at) REQUIRED int
    """

    # region fields

    first_ticket_created_at: int  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_first_ticket_created_at(self, value: int) -> ModelsMatchAttributes:
        self.first_ticket_created_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "first_ticket_created_at"):
            result["first_ticket_created_at"] = int(self.first_ticket_created_at)
        elif include_empty:
            result["first_ticket_created_at"] = 0
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        first_ticket_created_at: int,
    ) -> ModelsMatchAttributes:
        instance = cls()
        instance.first_ticket_created_at = first_ticket_created_at
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> ModelsMatchAttributes:
        instance = cls()
        if not dict_:
            return instance
        if (
            "first_ticket_created_at" in dict_
            and dict_["first_ticket_created_at"] is not None
        ):
            instance.first_ticket_created_at = int(dict_["first_ticket_created_at"])
        elif include_empty:
            instance.first_ticket_created_at = 0
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, ModelsMatchAttributes]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[ModelsMatchAttributes]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        ModelsMatchAttributes,
        List[ModelsMatchAttributes],
        Dict[Any, ModelsMatchAttributes],
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
            "first_ticket_created_at": "first_ticket_created_at",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "first_ticket_created_at": True,
        }

    # endregion static methods
