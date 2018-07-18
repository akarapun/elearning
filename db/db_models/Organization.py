from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Organization(Base):
    __tablename__ = 'organization'
    __table_args__ = (
        PrimaryKeyConstraint('orgCode'),
    )

    orgCode = Column(NVARCHAR(length=20), nullable=False)
    strCode = Column(NVARCHAR(length=20))
    parentOrgCode = Column(NVARCHAR(length=20))
    orgTypeCode = Column(NVARCHAR(length=20))
    orgDesc = Column(NVARCHAR(length=150))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
