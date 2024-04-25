# -*- coding: utf-8 -*-
from fastapi import APIRouter

from . import login, users

v1 = APIRouter(prefix="/v1")

v1.include_router(login.router)
v1.include_router(users.router)
