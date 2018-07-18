from flask import request
import jwt

from settings.app import ENCODE_SECRET

def isAllowAccess():
    
    status = False

    try:
        token = request.headers.get('Authorization')
        encodedToken = token.encode('utf-8')
        decoded = jwt.decode(encodedToken, ENCODE_SECRET, algorithms=['HS256'])
        status = True
    except jwt.exceptions.ExpiredSignatureError as e:
        print (e)
    except Exception as e:
        print (e)

    return status
