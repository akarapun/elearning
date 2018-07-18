from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class PeopleCredential(Base):
    __tablename__ = 'peopleCredential'
    __table_args__ = (
        PrimaryKeyConstraint('peopleCode'),
    )

    peopleCode = Column(NVARCHAR(length=20), nullable=False)
    username = Column(NVARCHAR(length=20))
    password = Column(NVARCHAR(length=300))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)