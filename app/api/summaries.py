from typing import List
from fastapi import APIRouter
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema
from app.api import crud

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)
    response_object = {"id": summary_id, "url": payload.url}
    return response_object


@router.get("/", response_model=List[SummaryResponseSchema], status_code=200)
async def get_all_summaries() -> List[SummaryResponseSchema]:
    return await crud.get_all()


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummaryResponseSchema:
    return await crud.get(id)
