from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Position(Base):
    __tablename__ = 'position'
    __table_args__ = (
        PrimaryKeyConstraint('posCode'),
    )

    posCode = Column(NVARCHAR(length=20), nullable=False)
    posDesc = Column(NVARCHAR(length=150))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
