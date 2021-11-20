from .config import allowedKeys

def apiKeyIsValid(key:str):
    return key in allowedKeys