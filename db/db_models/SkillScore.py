from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class SkillScore(Base):
    __tablename__ = 'skillScore'
    __table_args__ = (
        PrimaryKeyConstraint('peopleCode', 'skillCode'),
    )

    peopleCode = Column(NVARCHAR(length=20))
    skillCode = Column(NVARCHAR(length=20))
    skillBlockScore = Column(NVARCHAR(length=10))
    statusId = Column(NVARCHAR(length=2), default=0)