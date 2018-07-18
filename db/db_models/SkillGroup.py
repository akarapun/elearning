from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class SkillGroup(Base):
    __tablename__ = 'skillGroup'
    __table_args__ = (
        PrimaryKeyConstraint('skillGroupCode'),
    )

    skillGroupCode = Column(NVARCHAR(length=20), nullable=False)
    skillGroup = Column(NVARCHAR(length=100))
    skillGroupDesc = Column(NVARCHAR(length=300))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
