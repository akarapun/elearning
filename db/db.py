from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select

# conn = engine.connect()
# trans = conn.begin() start transaction

# execute here

# trans.commit() commit transaction
# conn.close()

# 49.229.208.199
engine = create_engine(
    'mysql+cymysql://root:1q2w3e4r5t@localhost/my_db',
    echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

from db_models import (
    BadgeDBModel,
    BadgeConditionDBModel,
    BadgeTypeDBModel,
    OrganizationDBModel,
    OrganizationTypeDBModel,
    OrgPosDBModel,
    PeopleDBModel,
    PeopleCredentialDBModel,
    PeoplePosRoleDBModel,
    PhoneDBModel,
    PhoneTypeDBModel,
    PositionDBModel,
    PreSkillDBModel,
    RoleDBModel,
    RoleSkillBlockDBModel,
    SexDBModel,
    SkillDBModel,
    SkillBlockDBModel,
    SkillBlockScoreDBModel,
    SkillBlockSkillDBModel,
    SkillGroupDBModel,
    SkillGroupSkillBlockDBModel,
    SkillScoreDBModel,
    SkillScoreHistoryDBModel,
    StatusDBModel,
    StructureDBModel
)

def createAdmin():
    # add admin user

    admin = PeopleDBModel(
        peopleCode='admin'
    )

    import hashlib
    adminCredential = PeopleCredentialDBModel(
        peopleCode='admin',
        username='admin',
        password=hashlib.sha256('admin'.encode('utf-8')).hexdigest()
    )

    db_session.add(admin)
    db_session.add(adminCredential)
    db_session.commit()


def init_db():
    
    pass
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    #
    # createAdmin()
