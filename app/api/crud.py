from typing import List, Union
from fastapi import HTTPException
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="Dummy dummy")
    await summary.save()
    return summary.id


async def get_all() -> List:
    return await TextSummary.all().values()


async def get(id: int) -> Union[dict, None]:
    summaries = await TextSummary.filter(id=id).first().values()
    if summaries:
        return summaries[0]
    raise HTTPException(status_code=404, detail="Summary not found")
