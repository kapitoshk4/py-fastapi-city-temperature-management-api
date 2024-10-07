import os
from datetime import datetime
from typing import Optional

import httpx
from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from city import crud as city_crud
from . import crud as temperature_crud
from dependecies import get_db
from settings import url
from temperature import schemas

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API")


async def fetch_temperature_for_city(city_name: str) -> Optional[float]:
    city_temperature = f"{url}?key={WEATHER_API_KEY}&q={city_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(city_temperature)
        if response.status_code == 200:
            data = response.json()
            return data["current"]["temp_c"]
        return None


async def update_temperatures(db: AsyncSession = Depends(get_db)) -> list:
    cities = await city_crud.get_cities(db)
    temperature_data = []

    for city in cities:
        temp = await fetch_temperature_for_city(city.name)
        if temp is not None:
            temperature_create = schemas.TemperatureCreate(
                city_id=city.id,
                temperature=temp,
                date_time=datetime.utcnow()
            )
            db_temp = await temperature_crud.create_temperature(db, temperature_create)
            temperature_data.append(db_temp)

    return temperature_data
