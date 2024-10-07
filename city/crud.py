from typing import Sequence, Optional, Dict

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas
from .models import City


async def get_cities(db: AsyncSession) -> Sequence[City]:
    query = select(models.City)
    result = await db.execute(query)
    return result.scalars().all()


async def get_city(db: AsyncSession, city_id: int) -> Optional[models.City]:
    return await db.get(models.City, city_id)


async def create_city(db: AsyncSession, city: schemas.CityCreate) -> Dict[str, int]:
    query = insert(models.City).values(
        name=city.name,
        additional_info=city.additional_info
    )
    result = await db.execute(query)
    await db.commit()
    resp = {**city.model_dump(), "id": result.lastrowid}
    return resp


async def delete_city(db: AsyncSession, city_id: int) -> Dict[str, str]:
    city = await db.get(models.City, city_id)
    if city:
        await db.delete(city)
        await db.commit()
        return {"message": "City deleted"}
