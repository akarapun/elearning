from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class People(Base):
    __tablename__ = 'people'
    __table_args__ = (
        PrimaryKeyConstraint('peopleCode'),
    )

    peopleCode = Column(NVARCHAR(length=15), nullable=False)
    firstname = Column(NVARCHAR(length=30))
    lastname = Column(NVARCHAR(length=30))
    sexId = Column(NVARCHAR(length=1))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)