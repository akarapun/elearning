from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Phone(Base):
    __tablename__ = 'phone'
    __table_args__ = (
        PrimaryKeyConstraint('rowId', 'peopleCode'),
    )

    rowId = Column(Integer, nullable=False)
    peopleCode = Column(NVARCHAR(length=20), nullable=False)
    phone = Column(NVARCHAR(length=15))
    ext = Column(NVARCHAR(length=5))
    phoneTypeId = Column(NVARCHAR(length=2))
    statusId = Column(NVARCHAR(length=2), default=0)