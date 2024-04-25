# -*- coding: utf-8 -*-

import os
import sys

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise

opd = os.path.dirname
curr_path = opd(os.path.realpath(__file__))
proj_path = opd(opd(curr_path))
sys.path.insert(0, proj_path)

from backend.api.v1 import v1
from backend.core.config import settings
from backend.core.logger import Loggers


async def close_database():
    """
    关闭数据库
    :return:
    """
    await Tortoise.close_connections()


async def init_database():
    """
    创建数据库和表
    :return:
    """
    await Tortoise.init(
        db_url=settings.db_url,
        modules={'models': ['backend.models']},
        use_tz=False,  # 关闭时区设置
        timezone='UTC'  # 设置时区为 UTC
    )
    await Tortoise.generate_schemas()


def create_app():
    """
    创建app
    :return:
    """
    c_app = FastAPI(**settings.FastAPI_SETTINGS)

    # 设置跨域传参
    c_app.add_middleware(
        CORSMiddleware,
        **settings.CORS
    )
    c_app.include_router(v1, prefix="/api")

    return c_app


app = create_app()


@app.on_event("startup")
async def startup_event():
    """
    uvicorn启动事件
    :return:
    """
    # 添加在应用程序启动之前运行初始化数据库
    await init_database()
    # 将uvicorn输出的全部让loguru管理
    Loggers.init_config()


@app.on_event("shutdown")
async def shutdown_event():
    """
    uvicorn关闭事件
    :return:
    """
    # 添加在应用程序关闭时关闭所有数据库链接
    await close_database()
