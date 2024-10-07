from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base

from city.models import City


class Temperature(Base):
    __tablename__ = "temperatures"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey(City.id))
    date_time = Column(DateTime(timezone=True), nullable=False)
    temperature = Column(Float, nullable=False)

    city = relationship("City", back_populates="temperatures", lazy="select")
