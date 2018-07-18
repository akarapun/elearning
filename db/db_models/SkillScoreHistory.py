from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class SkillScoreHistory(Base):
    __tablename__ = 'skillScoreHistory'
    __table_args__ = (
        PrimaryKeyConstraint('rowId'),
    )

    rowId = Column(Integer, nullable=False)
    peopleCode = Column(NVARCHAR(length=20))
    skillCode = Column(NVARCHAR(length=20))
    examDate = Column(DateTime)
    expiryDate = Column(DateTime)
    cpl = Column(Integer)
    tpl = Column(Integer)
    skillScore = Column(NVARCHAR(length=10))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)