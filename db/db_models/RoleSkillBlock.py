from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class RoleSkillBlock(Base):
    __tablename__ = 'roleSkillBlock'
    __table_args__ = (
        PrimaryKeyConstraint('rowId'),
    )

    rowId = Column(Integer, nullable=False)
    roleCode = Column(NVARCHAR(length=20))
    skillBlockCode = Column(NVARCHAR(length=20))
    statusId = Column(NVARCHAR(length=2), default=0)