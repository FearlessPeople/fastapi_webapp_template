# -*- coding: utf-8 -*-

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    SUCCESS = 200
    FAIL = 500


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="业务状态码 200成功 500失败")
    data: Any = Field(default=None, description="数据结果")
    msg: str = Field(default="success", description="提示")


class Success(ResponseBasic):
    pass


class Fail(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = "failed"


class ResponseToken(Success):
    access_token: str
    token_type: str = Field(default="bearer")
