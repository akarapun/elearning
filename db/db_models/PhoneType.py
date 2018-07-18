from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class PhoneType(Base):
    __tablename__ = 'phoneType'
    __table_args__ = (
        PrimaryKeyConstraint('phoneTypeId'),
    )

    phoneTypeId = Column(NVARCHAR(length=2), nullable=False)
    type = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)