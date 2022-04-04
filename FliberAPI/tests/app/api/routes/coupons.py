from unittest import mock

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.repositories.gender import GenderRepository
from app.models.schema.gender import InGenderSchema

pytestmark = pytest.mark.asyncio


async def test_coupon_create(
    async_client: AsyncClient, db_session: AsyncSession
) -> None:
    gender_repository = GenderRepository(db_session)
    payload = {
        "code": "PIOTR",
        "init_count": 100,
    }

    response = await async_client.post("/v1/gender/", json=payload)
    coupon = await gender_repository.get_by_id(response.json()["id"])

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "code": payload["code"],
        "init_count": payload["init_count"],
        "remaining_count": payload["init_count"],
        "id": str(coupon.id),
    }


async def test_coupon_get_by_id(
    async_client: AsyncClient, db_session: AsyncSession
) -> None:
    payload = {
        "code": "PIOTR",
        "init_count": 100,
    }
    gender_repository = GenderRepository(db_session)
    coupon = await gender_repository.create(InGenderSchema(**payload))

    response = await async_client.get(f"/v1/gender/{coupon.id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "code": payload["code"],
        "init_count": payload["init_count"],
        "remaining_count": payload["init_count"],
        "id": mock.ANY,
    }
