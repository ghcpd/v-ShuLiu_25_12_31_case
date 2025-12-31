from fastapi import APIRouter, HTTPException

from app.models import User, UserCreate, ErrorResponse
from app.repositories import user_repo


router = APIRouter()


@router.post("/", response_model=User, responses={400: {"model": ErrorResponse}})
async def create_user(payload: UserCreate):
    # Extremely naive duplicate check based on email, just for demo purposes.
    existing = [u for u in user_repo.list_users() if u.email == payload.email]
    if existing:
        # Here we use a structured error response.
        raise HTTPException(status_code=400, detail="User with this email already exists")
    user = user_repo.create_user(payload)
    return user


@router.get("/", response_model=list[User])
async def list_users():
    # NOTE: no pagination, no filtering.
    return user_repo.list_users()


@router.get("/{user_id}")
async def get_user(user_id: int):
    # NOTE: this endpoint does NOT use a response_model on purpose.
    user = user_repo.get_user(user_id)
    if not user:
        # Here we return a plain dict, not ErrorResponse.
        return {"detail": "User not found"}
    return user.dict()
