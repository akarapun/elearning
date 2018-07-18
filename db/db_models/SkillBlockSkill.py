from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class SkillBlockSkill(Base):
    __tablename__ = 'skillBlockSkill'
    __table_args__ = (
        PrimaryKeyConstraint('rowId'),
    )

    rowId = Column(Integer, nullable=False)
    skillBlockCode = Column(NVARCHAR(length=20))
    skillCode = Column(NVARCHAR(length=20))
    statusId = Column(NVARCHAR(length=2), default=0)