import setup
setup.pathSetup()

import db
from db import engine, db_session, Base, PeopleDBModel

#Base.metadata.create_all(bind=engine)

batman = PeopleDBModel(peopleCode = 'jtl001', firstname='Batman', createdBy='RD')
db_session.add(batman)

robin = PeopleDBModel(peopleCode = 'jtl002', firstname='Robin', createdBy='RD')
db_session.add(robin)

db_session.commit()