# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="FastAPI",
    description="No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)",
    version="0.1.0",
)

app.include_router(DefaultApiRouter)
