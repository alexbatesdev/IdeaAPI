# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.http_validation_error import HTTPValidationError  # noqa: F401
from openapi_server.models.idea import Idea  # noqa: F401
from openapi_server.models.idea_in import IdeaIn  # noqa: F401
from openapi_server.models.idea_list import IdeaList  # noqa: F401


def test_add_idea_ideas_post(client: TestClient):
    """Test case for add_idea_ideas_post

    Add Idea
    """
    idea_in = {"title":"title","desc":"desc"}

    headers = {
    }
    response = client.request(
        "POST",
        "/ideas",
        headers=headers,
        json=idea_in,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_idea_ideas_idea_id_delete(client: TestClient):
    """Test case for delete_idea_ideas_idea_id_delete

    Delete Idea
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/ideas/{idea_id}".format(idea_id=None),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_idea_ideas_idea_id_get(client: TestClient):
    """Test case for get_idea_ideas_idea_id_get

    Get Idea
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/ideas/{idea_id}".format(idea_id=None),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_ideas_ideas_get(client: TestClient):
    """Test case for get_ideas_ideas_get

    Get Ideas
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/ideas",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_overwrite_idea_ideas_idea_id_patch(client: TestClient):
    """Test case for overwrite_idea_ideas_idea_id_patch

    Overwrite Idea
    """
    idea_in = {"title":"title","desc":"desc"}

    headers = {
    }
    response = client.request(
        "PATCH",
        "/ideas/{idea_id}".format(idea_id=None),
        headers=headers,
        json=idea_in,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_idea_ideas_idea_id_put(client: TestClient):
    """Test case for update_idea_ideas_idea_id_put

    Update Idea
    """
    idea_in = {"title":"title","desc":"desc"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/ideas/{idea_id}".format(idea_id=None),
        headers=headers,
        json=idea_in,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

