from fastapi import APIRouter

# from api.user.v1.user import user_router as user_v1_router
# from api.auth.auth import auth_router
from api.home.home import home_router

router = APIRouter()
# router.include_router(user_v1_router, prefix="/api/v1/users", tags=["User"])
# router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(home_router, prefix="/home", tags=["Home"])

__all__ = ["router"]
