# -*- coding: utf-8 -*-

import os
import sys
from datetime import timedelta

opd = os.path.dirname
curr_path = opd(os.path.realpath(__file__))
proj_path = opd(opd(opd(curr_path)))
sys.path.insert(0, proj_path)

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from backend.core.config import settings
from backend.core.security import verify_password, create_access_token
from backend.models import User, OnlineUser, ResponseToken
from backend.models.result import ResponseToken
from backend.models.token import Token
from backend.util.util_orm import upsert

router = APIRouter(tags=["认证相关"])


@router.post("/login", summary="登录")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> ResponseToken:
    http_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无效的用户名或密码",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if user := await User.get(username=form_data.username):  # 如果数据库中有该用户
        if verify_password(form_data.password, user.password):
            token = create_access_token({"sub": user.username})

            # 更新过期时间
            access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": str(user.id)}, expires_delta=access_token_expires
            )
            await upsert(OnlineUser, userid=user.id)
            return ResponseToken(data={"token": f"bearer {token}"}, access_token=access_token)
        raise http_exception

        # user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        # if not user:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Incorrect username or password",
        #         headers={"WWW-Authenticate": "Bearer"},
        #     )
        # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # access_token = create_access_token(
        #     data={"sub": user.username}, expires_delta=access_token_expires
        # )
        # return Token(access_token=access_token, token_type="bearer")
