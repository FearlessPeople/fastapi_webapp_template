# -*- coding: utf-8 -*-

import asyncio
import os
import secrets

description = """
## Fastapi的一个webapp框架模板,实现了前后端分离技术架构
"""


class Settings:
    """
    应用程序配置类
    """
    FastAPI_SETTINGS = dict(title="Fastapi的一个webapp框架模板",
                            description=description,  # 描述
                            version="0.0.1",  # 版本号
                            )
    sem = asyncio.Semaphore(30)  # 控制项目中 异步请求其他网址时的并发量
    retry = 30  # 网络访重试次数
    # 数据库 配置
    DB = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": 'root',
        "password": '123456',
        "database": 'xianyu',
        "charset": "utf8mb4"
    }
    db_url: str = "mysql://{user}:{password}@{host}:{port}/{database}?charset={charset}".format(**DB)
    CORS = dict(allow_origins=['*'],  # 设置允许的origins来源
                allow_credentials=True,
                allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
                allow_headers=["*"])  # 允许跨域的headers，可以用来鉴别来源等作用。

    # 程序配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(BASE_DIR, '../logs')  # 日志文件位置
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # JWT 相关
    #  随机生成的base64位字符串
    SECRET_KEY = secrets.token_urlsafe(32)
    # 加密算法
    ALGORITHM = "HS256"
    # token时效
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    # frida server 地址
    FRIDA_SERVER = '127.0.0.1:1234'

    # 企业微信推送开关
    WX_PUSH_OPEN = False
    # 企业微信机器人通知地址
    WX_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=企微key"
    # 钉钉推送开关
    DING_PUSH_OPEN = False
    # 钉钉机器人通知地址
    DING_WEBHOOK_URL = "https://56789"


settings = Settings()
