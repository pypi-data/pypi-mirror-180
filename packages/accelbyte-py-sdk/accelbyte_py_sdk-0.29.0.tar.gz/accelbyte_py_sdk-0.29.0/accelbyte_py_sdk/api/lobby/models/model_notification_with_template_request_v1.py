# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: accelbyte_cloud_py_codegen

# AccelByte Cloud Lobby Server (staging)

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


class ModelNotificationWithTemplateRequestV1(Model):
    """Model notification with template request V1 (model.NotificationWithTemplateRequestV1)

    Properties:
        template_context: (templateContext) REQUIRED Dict[str, str]

        template_language: (templateLanguage) REQUIRED str

        template_slug: (templateSlug) REQUIRED str

        topic_name: (topicName) REQUIRED str
    """

    # region fields

    template_context: Dict[str, str]  # REQUIRED
    template_language: str  # REQUIRED
    template_slug: str  # REQUIRED
    topic_name: str  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_template_context(
        self, value: Dict[str, str]
    ) -> ModelNotificationWithTemplateRequestV1:
        self.template_context = value
        return self

    def with_template_language(
        self, value: str
    ) -> ModelNotificationWithTemplateRequestV1:
        self.template_language = value
        return self

    def with_template_slug(self, value: str) -> ModelNotificationWithTemplateRequestV1:
        self.template_slug = value
        return self

    def with_topic_name(self, value: str) -> ModelNotificationWithTemplateRequestV1:
        self.topic_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "template_context"):
            result["templateContext"] = {
                str(k0): str(v0) for k0, v0 in self.template_context.items()
            }
        elif include_empty:
            result["templateContext"] = {}
        if hasattr(self, "template_language"):
            result["templateLanguage"] = str(self.template_language)
        elif include_empty:
            result["templateLanguage"] = ""
        if hasattr(self, "template_slug"):
            result["templateSlug"] = str(self.template_slug)
        elif include_empty:
            result["templateSlug"] = ""
        if hasattr(self, "topic_name"):
            result["topicName"] = str(self.topic_name)
        elif include_empty:
            result["topicName"] = ""
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        template_context: Dict[str, str],
        template_language: str,
        template_slug: str,
        topic_name: str,
    ) -> ModelNotificationWithTemplateRequestV1:
        instance = cls()
        instance.template_context = template_context
        instance.template_language = template_language
        instance.template_slug = template_slug
        instance.topic_name = topic_name
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> ModelNotificationWithTemplateRequestV1:
        instance = cls()
        if not dict_:
            return instance
        if "templateContext" in dict_ and dict_["templateContext"] is not None:
            instance.template_context = {
                str(k0): str(v0) for k0, v0 in dict_["templateContext"].items()
            }
        elif include_empty:
            instance.template_context = {}
        if "templateLanguage" in dict_ and dict_["templateLanguage"] is not None:
            instance.template_language = str(dict_["templateLanguage"])
        elif include_empty:
            instance.template_language = ""
        if "templateSlug" in dict_ and dict_["templateSlug"] is not None:
            instance.template_slug = str(dict_["templateSlug"])
        elif include_empty:
            instance.template_slug = ""
        if "topicName" in dict_ and dict_["topicName"] is not None:
            instance.topic_name = str(dict_["topicName"])
        elif include_empty:
            instance.topic_name = ""
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, ModelNotificationWithTemplateRequestV1]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[ModelNotificationWithTemplateRequestV1]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        ModelNotificationWithTemplateRequestV1,
        List[ModelNotificationWithTemplateRequestV1],
        Dict[Any, ModelNotificationWithTemplateRequestV1],
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
            "templateContext": "template_context",
            "templateLanguage": "template_language",
            "templateSlug": "template_slug",
            "topicName": "topic_name",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "templateContext": True,
            "templateLanguage": True,
            "templateSlug": True,
            "topicName": True,
        }

    # endregion static methods
