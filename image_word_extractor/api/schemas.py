from pydantic import BaseModel
from typing import List, Dict


class Document(BaseModel):
    base64: str
    word_list: List[Dict]
    text_list: List[str]
