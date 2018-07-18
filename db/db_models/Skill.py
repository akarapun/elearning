from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Skill(Base):
    __tablename__ = 'skill'
    __table_args__ = (
        PrimaryKeyConstraint('skillCode'),
    )

    skillCode = Column(NVARCHAR(length=20), nullable=False)
    skill = Column(NVARCHAR(length=100))
    skillDesc = Column(NVARCHAR(length=300))
    tpl = Column(Integer)
    expiryType = Column(Integer)
    expiryCondition = Column(NVARCHAR(length=500))
    expiredAt = Column(DateTime)
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
