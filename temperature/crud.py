from typing import Optional, Dict

from sqlalchemy import select, insert, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas
from .models import Temperature


async def get_temperatures(db: AsyncSession,
                           skip: int = 0,
                           limit: int = 100) -> ScalarResult[Temperature]:
    query = select(models.Temperature)
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)

    return result.scalars()


async def get_temperature_by_city_id(db: AsyncSession, city_id: int) -> Optional[Temperature] | None:
    return await db.get(models.Temperature, city_id)


async def create_temperature(db: AsyncSession, temperature: schemas.TemperatureCreate) -> Dict[str, int]:
    query = insert(models.Temperature).values(
        **temperature.dict()
    )
    result = await db.execute(query)
    await db.commit()
    resp = {**temperature.model_dump(), "id": result.lastrowid}
    return resp
