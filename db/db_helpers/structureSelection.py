from db_models import StructureDBModel
from db import db_session

def selectStructureByStrCode(strCode):
    return db_session.query(StructureDBModel).filter_by(strCode=strCode).first()

def isStructureByStrCodeExist(strCode):
    structure = selectStructureByStrCode(strCode)
    return True if structure is not None else False


"""
    delete Structure by strCode
    return type -> Boolean
"""
def deleteStructureByStrCode(strCode):
    isDeleteSuccess = False
    if isStructureByStrCodeExist(strCode):
        toDeleteStr = selectStructureByStrCode(strCode)
        db_session.delete(toDeleteStr)
        db_session.commit()

        isDeleteSuccess = True

    return isDeleteSuccess

def selectAllStructure():
    return db_session.query(StructureDBModel).all()
