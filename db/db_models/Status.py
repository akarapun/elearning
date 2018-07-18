from sqlalchemy import NVARCHAR, func, Column
from sqlalchemy import PrimaryKeyConstraint

from db import Base

class Status(Base):
    __tablename__ = 'status'
    __table_args__ = (
        PrimaryKeyConstraint('statusId'),
    )

    statusId = Column(NVARCHAR(length=2), nullable=False)
    status = Column(NVARCHAR(length=50))
