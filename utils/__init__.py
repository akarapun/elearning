from .isAllowAccess import isAllowAccess

def validObjectAttr(obj, attrName):
    if hasattr(obj, attrName):
        return obj['attrName']
    else:
        return ''

def log(arg):
    print ('\n')
    print ("log --> ##################")
    print (arg)
    print ("##################")
    print ('\n')
