from aiogram import Router

from .auth_handler import router as auth_router
router = Router(name=__name__)

router.include_routers(
    auth_router,
)