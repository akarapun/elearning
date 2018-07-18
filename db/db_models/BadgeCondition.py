from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class BadgeCondition(Base):
    __tablename__ = 'badgeCondition'
    __table_args__ = (
        PrimaryKeyConstraint('rowId', 'badgeCode'),
    )
    
    rowId = Column(Integer, nullable=False)
    badgeCode = Column(NVARCHAR(length=20), nullable=False)
    ConditionType = Column(NVARCHAR(length=20))
    ConditionCode = Column(NVARCHAR(length=20))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
