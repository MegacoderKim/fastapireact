import os
from typing import Generator

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

# from tortoise.contrib.test import finalizer

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app_with_db() -> Generator:
    app = main.create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        yield test_client
    # finalizer()


@pytest.fixture(scope="module")
def test_app() -> Generator:
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:
        yield test_client
    # finalizer()
