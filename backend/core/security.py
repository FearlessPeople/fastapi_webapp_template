# -*- coding: utf-8 -*-

# https://fastapi.tiangolo.com/zh/tutorial/security/oauth2-jwt/

import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Union

opd = os.path.dirname
curr_path = opd(os.path.realpath(__file__))
proj_path = opd(opd(opd(curr_path)))
sys.path.insert(0, proj_path)

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from backend.core.config import settings
from backend.models import User, OnlineUser
from backend.util.util_orm import upsert

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码: 明文密码 vs hash密码
    :param plain_password:  明文密码
    :param hashed_password: hash密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    获取密码hash值
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    创建token
    :param data: 字典
    :param expires_delta: 过期时间
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    解析token，获取当前用户
    :param token: 从请求头中取到 Authorization 的value
    :return: 当前用户对象
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证登录凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        userid: str = payload.get("sub")
        if userid is None:
            # 数据库中让该用户下线
            await OnlineUser(userid=userid).delete()
            raise credentials_exception
        else:
            # 将当前用户加入数据库在线用户清单中
            await upsert(OnlineUser, userid=userid)
    except JWTError as e:
        print(e)
        raise credentials_exception
    user = await User.get(id=userid)
    if user is None:
        raise credentials_exception
    return user
