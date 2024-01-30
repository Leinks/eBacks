import time
from typing import Dict

import jwt

from config.config import Settings


def token_response(token: str, email: str, name: str, _id:str):
    return {"accessToken": token, "uni": _id, "email": email, "name": name}


secret_key = Settings().secret_key


def sign_jwt(user_id: str, name: str, _id:str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {"user_id": user_id, "expires": time.time() + 2400}
    return token_response(jwt.encode(payload, secret_key, algorithm="HS256"), user_id, name, _id)


def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token.encode(), secret_key, algorithms=["HS256"])
    return decoded_token if decoded_token["expires"] >= time.time() else {}
