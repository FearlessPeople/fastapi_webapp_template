# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends
import sys,os
opd = os.path.dirname
curr_path = opd(os.path.realpath(__file__))
proj_path = opd(opd(opd(curr_path)))
sys.path.insert(0, proj_path)

from backend.core.security import get_password_hash, get_current_user
from backend.models import User
from backend.models import UserIn_Pydantic, User_Pydantic, Success

router = APIRouter(prefix="/users", tags=["用户相关"], dependencies=[Depends(get_current_user)])


@router.post("/me", summary="当前用户")
async def curr_user(user_obj: User = Depends(get_current_user)):
    return Success(data=await User_Pydantic.from_tortoise_orm(user_obj))


@router.post("/save", summary="新增用户")
async def save_user(user: UserIn_Pydantic):
    hash_password = get_password_hash(user.password)
    insert_user = User(username=user.username, password=hash_password, nickname=user.nickname)
    await insert_user.save()
    return Success(data="添加成功")
