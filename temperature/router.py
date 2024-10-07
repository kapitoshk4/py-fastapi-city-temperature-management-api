from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from dependecies import get_db
from . import crud, schemas
from . import services

router = APIRouter()


@router.get("/temperatures/", response_model=list[schemas.Temperature])
async def read_temperatures(db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 100):
    return await crud.get_temperatures(db=db, skip=skip, limit=limit)


@router.get("/temperatures/{city_id}/", response_model=schemas.Temperature)
async def read_temperature_of_city(city_id: int, db: AsyncSession = Depends(get_db)):
    city = await crud.get_temperature_by_city_id(db, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    return city


@router.post("/temperatures/update/")
async def update_temperatures(db: AsyncSession = Depends(get_db)):
    return await services.update_temperatures(db)
