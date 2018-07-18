from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Sex(Base):
    __tablename__ = 'sex'
    __table_args__ = (
        PrimaryKeyConstraint('sexId'),
    )

    sexId = Column(NVARCHAR(length=1))
    sex = Column(NVARCHAR(length=10))
    statusId = Column(NVARCHAR(length=2), default=0)