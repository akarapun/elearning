from sqlalchemy import Table, Column, Integer, String, NVARCHAR, DateTime, func
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Structure(Base):
    __tablename__ = 'structure'
    __table_args__ = (
        PrimaryKeyConstraint('strCode'),
    )

    strCode = Column(NVARCHAR(length=20), nullable=False)
    strDesc = Column(NVARCHAR(length=150))
    createdAt = Column(DateTime, default=func.now())
    createdBy = Column(NVARCHAR(length=30))
    updatedAt = Column(DateTime)
    updatedBy = Column(NVARCHAR(length=30))
    statusId = Column(NVARCHAR(length=2), default=0)
