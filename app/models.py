from datetime import datetime, time
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class Channel(str, Enum):
    email = "email"
    slack = "slack"
    sms = "sms"  # not really implemented yet


class User(BaseModel):
    id: int
    email: EmailStr
    name: str
    is_active: bool = True


class UserCreate(BaseModel):
    email: EmailStr
    name: str


class ReminderFrequency(str, Enum):
    once = "once"
    daily = "daily"
    weekly = "weekly"


class Reminder(BaseModel):
    id: int
    owner_id: int
    title: str
    message: str
    channel: Channel = Channel.email
    # Simple schedule representation for now
    time_of_day: Optional[time] = None
    frequency: ReminderFrequency = ReminderFrequency.once
    created_at: datetime


class ReminderCreate(BaseModel):
    owner_id: int
    title: str
    message: str
    channel: Channel = Channel.email
    time_of_day: Optional[time] = None
    frequency: ReminderFrequency = ReminderFrequency.once


class SendResult(BaseModel):
    reminder_id: int
    success: bool
    detail: Optional[str] = None


class ErrorResponse(BaseModel):
    detail: str
    # NOTE: some endpoints don't use this model yet


class ReminderList(BaseModel):
    items: List[Reminder]
