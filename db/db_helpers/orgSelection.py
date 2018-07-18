from db import db_session
from db_models import OrganizationDBModel

def selectOrgByOrgCode(orgCode):
    return db_session.query(OrganizationDBModel).filter_by(orgCode=orgCode).first()

def isOrgByOrgCodeExist(orgCode):
    org = selectOrgByOrgCode(orgCode)
    return True if org is not None else False
