from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class SkillGroupSkillBlock(Base):
    __tablename__ = 'skillGroupSkillBlock'
    __table_args__ = (
        PrimaryKeyConstraint('peopleCode', 'skillGroupCode'),
    )

    peopleCode = Column(NVARCHAR(length=20))
    skillGroupCode = Column(NVARCHAR(length=20))
    skillGroupScore = Column(NVARCHAR(length=10))
    statusId = Column(NVARCHAR(length=2), default=0)