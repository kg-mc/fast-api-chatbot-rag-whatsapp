
from typing import Optional
from pydantic import BaseModel

class MessageSchema(BaseModel):
    profile_name: str
    message_from: str
    body: str