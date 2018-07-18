from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class BadgeType(Base):
    __tablename__ = 'badgeType'
    __table_args__ = (
        PrimaryKeyConstraint('badgeTypeCode'),
    )
    
    badgeTypeCode = Column(NVARCHAR(length=20), nullable=False)
    badgeType = Column(NVARCHAR(length=100))
    badgeTypeDesc = Column(NVARCHAR(length=500))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
