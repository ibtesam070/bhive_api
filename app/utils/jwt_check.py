import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timezone
from ..constants.values import JWT_ALGORITHM
import logging
import os

JWT_SECRET = os.getenv("JWT_SECRET")

auth_scheme = HTTPBearer()

def verify_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if payload.get("exp") and datetime.now(timezone.utc).timestamp() > payload["exp"]:
            raise HTTPException(status_code=401, detail="Token has expired")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> dict:
    token = credentials.credentials
    payload = verify_jwt(token)

    # Extract the user ID from the payload
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload: Missing 'sub'")

    return {"user_id": user_id}