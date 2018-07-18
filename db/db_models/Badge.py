from sqlalchemy import Table, Column, Integer, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Badge(Base):
    __tablename__ = 'badge'
    __table_args__ = (
        PrimaryKeyConstraint('badgeCode'),
    )
    
    badgeCode = Column(NVARCHAR(length=20), nullable=False)
    badgeTypeCode = Column(NVARCHAR(length=20), nullable=False)
    badge = Column(NVARCHAR(length=100))
    badgeDesc = Column(NVARCHAR(length=500))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
