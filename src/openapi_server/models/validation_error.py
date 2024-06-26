# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.location_inner import LocationInner


class ValidationError(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ValidationError - a model defined in OpenAPI

        loc: The loc of this ValidationError.
        msg: The msg of this ValidationError.
        type: The type of this ValidationError.
    """

    loc: List[LocationInner] = Field(alias="loc")
    msg: str = Field(alias="msg")
    type: str = Field(alias="type")

ValidationError.update_forward_refs()
