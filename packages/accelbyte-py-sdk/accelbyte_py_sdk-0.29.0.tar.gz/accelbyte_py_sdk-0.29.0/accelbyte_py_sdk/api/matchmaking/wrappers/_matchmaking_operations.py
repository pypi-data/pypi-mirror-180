# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: accelbyte_cloud_py_codegen

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
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

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import HeaderStr
from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import run_request_async
from ....core import same_doc_as

from ..models import LogAppMessageDeclaration
from ..models import ResponseError

from ..operations.matchmaking_operations import GetHealthcheckInfo
from ..operations.matchmaking_operations import HandlerV3Healthz
from ..operations.matchmaking_operations import PublicGetMessages
from ..operations.matchmaking_operations import VersionCheckHandler


@same_doc_as(GetHealthcheckInfo)
def get_healthcheck_info(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = GetHealthcheckInfo.create()
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@same_doc_as(GetHealthcheckInfo)
async def get_healthcheck_info_async(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = GetHealthcheckInfo.create()
    return await run_request_async(
        request, additional_headers=x_additional_headers, **kwargs
    )


@same_doc_as(HandlerV3Healthz)
def handler_v3_healthz(x_additional_headers: Optional[Dict[str, str]] = None, **kwargs):
    request = HandlerV3Healthz.create()
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@same_doc_as(HandlerV3Healthz)
async def handler_v3_healthz_async(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = HandlerV3Healthz.create()
    return await run_request_async(
        request, additional_headers=x_additional_headers, **kwargs
    )


@same_doc_as(PublicGetMessages)
def public_get_messages(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = PublicGetMessages.create()
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@same_doc_as(PublicGetMessages)
async def public_get_messages_async(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = PublicGetMessages.create()
    return await run_request_async(
        request, additional_headers=x_additional_headers, **kwargs
    )


@same_doc_as(VersionCheckHandler)
def version_check_handler(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = VersionCheckHandler.create()
    return run_request(request, additional_headers=x_additional_headers, **kwargs)


@same_doc_as(VersionCheckHandler)
async def version_check_handler_async(
    x_additional_headers: Optional[Dict[str, str]] = None, **kwargs
):
    request = VersionCheckHandler.create()
    return await run_request_async(
        request, additional_headers=x_additional_headers, **kwargs
    )
