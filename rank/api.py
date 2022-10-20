"""This module merges the API routers for the project application."""
from ninja import NinjaAPI

from applications.accounts.api import router as accounts_router
from applications.events.api import router as events_router
from applications.leaderboard.api import router as leaderboard_router
from applications.ranking.api import router as ranking_router
from applications.students.api import router as students_router

api = NinjaAPI()

api.add_router("/accounts", accounts_router)
api.add_router("/events", events_router)
api.add_router("/leaderboard", leaderboard_router)
api.add_router("/ranking", ranking_router)
api.add_router("/students", students_router)
