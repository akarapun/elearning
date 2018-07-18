from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class SkillBlockScore(Base):
    __tablename__ = 'skillBlockScore'
    __table_args__ = (
        PrimaryKeyConstraint('peopleCode', 'skillBlockCode'),
    )

    peopleCode = Column(NVARCHAR(length=20))
    skillBlockCode = Column(NVARCHAR(length=20))
    skillBlockScore = Column(NVARCHAR(length=10))
    statusId = Column(NVARCHAR(length=2), default=0)