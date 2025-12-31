from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from app.models import User, UserCreate, Reminder, ReminderCreate, ReminderFrequency


# NOTE: This is a very naive in-memory store. Some other parts of the codebase
# assume a relational database exists, but that integration is not finished yet.


class InMemoryUserRepository:
    def __init__(self) -> None:
        self._users: Dict[int, User] = {}
        self._next_id = 1

    def create_user(self, data: UserCreate) -> User:
        user = User(id=self._next_id, email=data.email, name=data.name)
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def list_users(self) -> List[User]:
        return list(self._users.values())

    def get_user(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)


class InMemoryReminderRepository:
    def __init__(self) -> None:
        self._reminders: Dict[int, Reminder] = {}
        self._next_id = 1

    def create_reminder(self, data: ReminderCreate) -> Reminder:
        reminder = Reminder(
            id=self._next_id,
            owner_id=data.owner_id,
            title=data.title,
            message=data.message,
            channel=data.channel,
            time_of_day=data.time_of_day,
            frequency=data.frequency,
            created_at=datetime.utcnow(),
        )
        self._reminders[self._next_id] = reminder
        self._next_id += 1
        return reminder

    def list_reminders_for_user(self, owner_id: int) -> List[Reminder]:
        return [r for r in self._reminders.values() if r.owner_id == owner_id]


# TODO: add a proper abstraction/interface if/when we introduce a real database


user_repo = InMemoryUserRepository()
reminder_repo = InMemoryReminderRepository()
