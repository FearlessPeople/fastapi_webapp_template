# -*- coding: utf-8 -*-

from tortoise import fields
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator


class OnlineUser(models.Model):
    id = fields.IntField(pk=True, description="id")
    userid = fields.CharField(max_length=20, null=False, unique=True, description="用户id")

    class Meta:
        table = "sys_online_user"
        table_description = "在线用户表"


# 输出模型
OnlineUser_Pydantic = pydantic_model_creator(OnlineUser, name="OnlineUser")
# 输入模型
OnlineUserIn_Pydantic = pydantic_model_creator(OnlineUser, name="OnlineUserIn")
