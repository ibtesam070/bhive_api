from fastapi import Depends
from ..utils.hash_pass import hash_password, verify_password
from sqlalchemy.orm import Session
from ..models.user_model import User
import os
from dotenv import load_dotenv
from ..constants.values import JWT_ALGORITHM
import jwt
from datetime import datetime, timedelta, timezone

load_dotenv()


class AuthController:
    @staticmethod
    def signup(email: str, password: str, db: Session):
        try:
            # Check In db if email already exists
            user = db.query(User).filter(User.email == email).first()
            if user:
                return {"success": False, "data": "User already exists"}

            # Hash password
            hashed_password = hash_password(password)

            # Create a new user
            user = User(email=email, password=hashed_password)
            db.add(user)
            db.commit()
            db.refresh(user)

            # Create jwt token
            jwt_secret = os.getenv("JWT_SECRET")
            expiration = datetime.now(timezone.utc) + timedelta(hours=24)
            payload = {
                "sub": str(user.id),
                "exp": expiration,
                "iat": datetime.now(timezone.utc),
            }
            jwt_token = jwt.encode(payload, jwt_secret, algorithm=JWT_ALGORITHM)

            return {"success": True, "data": jwt_token}
        except Exception as e:
            db.rollback()
            return {"success": False, "data": "unable to signup the user"}

    @staticmethod
    def login(email: str, password: str, db: Session):
        try:
            # Get user from db
            user = db.query(User).filter(User.email == email).first()

            if not user:
                return {"success": False, "data": "Invalid email or password"}

            # Verify password
            is_valid = verify_password(password, user.password)

            if not is_valid:
                return {"success": False, "data": "Invalid email or password"}

            # Create jwt token
            jwt_secret = os.getenv("JWT_SECRET")
            expiration = datetime.now(timezone.utc) + timedelta(hours=24)
            payload = {
                "sub": str(user.id),
                "exp": expiration,
                "iat": datetime.now(timezone.utc),
            }
            jwt_token = jwt.encode(payload, jwt_secret, algorithm=JWT_ALGORITHM)

            return {"success": True, "data": jwt_token}
        except Exception as e:
            db.rollback()
            return {"success": False, "data": "unable to login the user"}
