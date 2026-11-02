from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    source: str = Field(min_length=1, max_length=200)
    raw_text: str = Field(min_length=1)


class DocumentRead(BaseModel):
    id: UUID
    title: str
    source: str
    char_count: int
    ingested_at: datetime
