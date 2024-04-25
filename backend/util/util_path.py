# -*- coding: utf-8 -*-

import os


class PathUtil:
    """
    路径工具类
    """

    @staticmethod
    def project_path():
        """
        项目根路径：这里到backend目录下
        :return:
        """
        return os.path.dirname(os.path.dirname(__file__))


if __name__ == '__main__':
    print(PathUtil.project_path())
