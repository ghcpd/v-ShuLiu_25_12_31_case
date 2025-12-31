from datetime import datetime
from typing import List

from app.models import Reminder, SendResult


# NOTE: This is intentionally simplistic and partially duplicated in
# `notifications` routes to reflect organic growth.


def schedule_reminder_send(reminder: Reminder) -> SendResult:
    # Pretend to schedule a reminder. In reality we just return success.
    # TODO: integrate with a real task queue or scheduler.
    now = datetime.utcnow()
    # This function does not actually check schedule; it's a placeholder.
    return SendResult(reminder_id=reminder.id, success=True, detail=f"Scheduled at {now.isoformat()}")


def send_reminders_immediately(reminders: List[Reminder]) -> List[SendResult]:
    # In a real system, this might fan out to external providers.
    results: List[SendResult] = []
    for r in reminders:
        results.append(
            SendResult(reminder_id=r.id, success=True, detail="Sent synchronously (fake)")
        )
    return results
