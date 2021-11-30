from typing import Union
from .config import allowedKeys


def apiKeyIsValid(key: Union[str, None]) -> bool:
    return key in allowedKeys