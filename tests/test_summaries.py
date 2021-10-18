import json

import pytest


LARGE_INDEX = 1_000_000


def test_create_summmary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"})
    )
    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app):
    response = test_app.post("/summaries/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_summary_list(test_app_with_db):
    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200


def test_ready_summary(test_app_with_db):
    create_summary = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://bit.ly"})
    )
    summary_id = create_summary.json()["id"]

    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://bit.ly"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app_with_db):
    response = test_app_with_db.get(f"/summaries/{LARGE_INDEX}/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"
