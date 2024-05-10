# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.idea import Idea
from openapi_server.models.idea_in import IdeaIn
from openapi_server.models.idea_list import IdeaList


router = APIRouter()


@router.post(
    "/ideas",
    responses={
        201: {"model": IdeaList, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Add Idea",
    response_model_by_alias=True,
)
async def add_idea_ideas_post(
    idea_in: IdeaIn = Body(None, description=""),
) -> IdeaList:
    ...


@router.delete(
    "/ideas/{idea_id}",
    responses={
        200: {"model": IdeaList, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Delete Idea",
    response_model_by_alias=True,
)
async def delete_idea_ideas_idea_id_delete(
    idea_id:  = Path(None, description=""),
) -> IdeaList:
    ...


@router.get(
    "/ideas/{idea_id}",
    responses={
        200: {"model": Idea, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Get Idea",
    response_model_by_alias=True,
)
async def get_idea_ideas_idea_id_get(
    idea_id:  = Path(None, description=""),
) -> Idea:
    ...


@router.get(
    "/ideas",
    responses={
        200: {"model": IdeaList, "description": "Successful Response"},
    },
    tags=["default"],
    summary="Get Ideas",
    response_model_by_alias=True,
)
async def get_ideas_ideas_get(
) -> IdeaList:
    ...


@router.patch(
    "/ideas/{idea_id}",
    responses={
        200: {"model": Idea, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Overwrite Idea",
    response_model_by_alias=True,
)
async def overwrite_idea_ideas_idea_id_patch(
    idea_id:  = Path(None, description=""),
    idea_in: IdeaIn = Body(None, description=""),
) -> Idea:
    ...


@router.put(
    "/ideas/{idea_id}",
    responses={
        200: {"model": Idea, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Update Idea",
    response_model_by_alias=True,
)
async def update_idea_ideas_idea_id_put(
    idea_id:  = Path(None, description=""),
    idea_in: IdeaIn = Body(None, description=""),
) -> Idea:
    ...
