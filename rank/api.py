"""This module merges the API routers for the project application."""
from ninja import NinjaAPI

from applications.accounts.api import router as accounts_router

api = NinjaAPI()

api.add_router("/accounts", accounts_router)
