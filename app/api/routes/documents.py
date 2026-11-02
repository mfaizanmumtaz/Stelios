from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.document import DocumentCreate, DocumentRead
router = APIRouter(tags=["documents"])


@router.post(
    "/documents",
    response_model=DocumentRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_document(payload: DocumentCreate) -> DocumentRead:

    # data proccessing

    return DocumentRead(
        id=uuid4(),
        title=payload.title,
        source=payload.source,
        char_count=len(payload.raw_text),
        ingested_at=datetime.now(UTC),
    )
