# -*- coding: utf-8 -*-

from tortoise import fields
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    id = fields.IntField(pk=True, description="id")
    username = fields.CharField(max_length=20, null=False, description="用户名")
    password = fields.CharField(max_length=128, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=False, description="昵称")

    class Meta:
        table = "sys_user"
        table_description = "用户表"

    # 调用父类save函数，保存用户时生成用户的hash密码值
    # async def save(
    #         self,
    #         using_db: Optional[BaseDBAsyncClient] = None,
    #         update_fields: Optional[Iterable[str]] = None,
    #         force_create: bool = False,
    #         force_update: bool = False,
    # ) -> None:
    #     if force_create or "password" in update_fields:
    #         self.password = get_password_hash(self.password)
    #
    #     await super(User, self).save(using_db, update_fields, force_create, force_update)


# 输出模型，注意这里输出模型的时候不输出password
User_Pydantic = pydantic_model_creator(User, name="User", exclude=['password'])
# 输入模型
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude=['id'])
