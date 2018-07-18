from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class PeoplePosRole(Base):
    __tablename__ = 'peoplePosRole'
    __table_args__ = (
        PrimaryKeyConstraint('rowId'),
    )

    rowId = Column(Integer, nullable=False)
    peopleCode = Column(NVARCHAR(length=20))
    posCode = Column(NVARCHAR(length=20))
    roleCode = Column(NVARCHAR(length=20))
    statusId = Column(NVARCHAR(length=2), default=0)
