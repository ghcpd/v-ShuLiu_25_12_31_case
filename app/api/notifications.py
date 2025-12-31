from typing import List

from fastapi import APIRouter, HTTPException

from app.models import (
    Reminder,
    ReminderCreate,
    ReminderList,
    SendResult,
    ErrorResponse,
)
from app.repositories import reminder_repo, user_repo
from app import services


router = APIRouter()


@router.post("/", response_model=Reminder, responses={400: {"model": ErrorResponse}})
async def create_reminder(payload: ReminderCreate):
    user = user_repo.get_user(payload.owner_id)
    if not user:
        # Here we follow the structured error pattern.
        raise HTTPException(status_code=400, detail="Owner user does not exist")
    reminder = reminder_repo.create_reminder(payload)
    return reminder


@router.get("/user/{owner_id}", response_model=ReminderList)
async def list_reminders_for_user(owner_id: int):
    reminders = reminder_repo.list_reminders_for_user(owner_id)
    return ReminderList(items=reminders)


@router.post("/send/{reminder_id}")
async def send_single_reminder(reminder_id: int):
    # NOTE: this endpoint intentionally does not use response_model.
    # It also duplicates some logic from services to reflect organic growth.
    reminders: List[Reminder] = reminder_repo.list_reminders_for_user(owner_id=0)
    target = None
    for r in reminders:
        if r.id == reminder_id:
            target = r
            break
    if not target:
        # Here we again return a plain dict instead of ErrorResponse.
        return {"detail": "Reminder not found"}

    result = services.schedule_reminder_send(target)
    return {"reminder_id": result.reminder_id, "status": "scheduled", "detail": result.detail}


@router.post("/send/immediate/{owner_id}", response_model=list[SendResult])
async def send_immediate_for_user(owner_id: int):
    # This endpoint uses the shared service and a proper response model.
    reminders = reminder_repo.list_reminders_for_user(owner_id)
    if not reminders:
        # Another inconsistency: different status code and error shape.
        raise HTTPException(status_code=404, detail="No reminders for user")
    return services.send_reminders_immediately(reminders)
