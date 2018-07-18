from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class OrgPos(Base):
    __tablename__ = 'orgPos'
    __table_args__ = (
        PrimaryKeyConstraint('rowId'),
    )

    rowId = Column(Integer, nullable=False)
    orgCode = Column(NVARCHAR(length=20))
    posCode = Column(NVARCHAR(length=20))
    statusId = Column(NVARCHAR(length=2), default=0)