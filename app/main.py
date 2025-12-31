from fastapi import FastAPI

from app.api import notifications, users


app = FastAPI(title="Team Reminder Service")


@app.get("/health")
async def health_check():
    # TODO: extend with DB / queue / dependencies checks
    return {"status": "ok"}


# Routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
