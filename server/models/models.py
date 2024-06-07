from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, conint

Base = declarative_base()

class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    rating = Column(Integer)


class CreateRatingRequest(BaseModel):
    rating: conint(gt=0, lt=6)
