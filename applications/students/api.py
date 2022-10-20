"""This module contains the API for the accounts application."""
from ninja import Router

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"
