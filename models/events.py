from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Событие Игнатченко Владислава",
                "image": "https://linktomymage.com/image.png",
                "description": "Практическая работа №7 выполнена Игнатченко Владиславом.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Уфа, УУНиТ"
            }
        }