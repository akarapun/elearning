from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class PreSkill(Base):
    __tablename__ = 'perSkill'
    __table_args__ = (
        PrimaryKeyConstraint('skillCode','preSkillCode'),
    )
    
    skillCode = Column(NVARCHAR(length=20), nullable=False)
    preSkillCode = Column(NVARCHAR(length=20), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
