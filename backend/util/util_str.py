# -*- coding: utf-8 -*-

import random
import string


class StrUtil:
    """
    字符串工具类
    """

    @staticmethod
    def random_str(random_length=8):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(random_length)]
        return ''.join(str_list)
