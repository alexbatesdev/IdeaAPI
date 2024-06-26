# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Idea(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Idea - a model defined in OpenAPI

        id: The id of this Idea [Optional].
        title: The title of this Idea.
        desc: The desc of this Idea.
        date_created: The date_created of this Idea [Optional].
        updated: The updated of this Idea [Optional].
    """

    id: Optional[int] = Field(alias="id", default=None)
    title: str = Field(alias="title")
    desc: str = Field(alias="desc")
    date_created: Optional[date] = Field(alias="date_created", default=None)
    updated: Optional[datetime] = Field(alias="updated", default=None)

Idea.update_forward_refs()
