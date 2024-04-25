# -*- coding: utf-8 -*-

import json
import os
import sys

import requests

opd = os.path.dirname
curr_path = opd(os.path.realpath(__file__))
proj_path = opd(opd(opd(curr_path)))
sys.path.insert(0, proj_path)

from backend.core.config import settings


class WeChatRobot:
    """
    企业微信群机器人工具类
    """

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_text(self, content):
        """
        向企业微信群机器人推送文本消息
        """
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        return self._send(data)

    def send_markdown(self, content, title=None):
        """
        向企业微信群机器人推送 Markdown 格式的消息
        """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        if title:
            data["markdown"]["title"] = title
        return self._send(data)

    def send_news(self, title, description, picurl):
        """
        向企业微信群机器人推送 News 格式的消息
        """
        data = {
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": f"{title}",
                        "description": f"{description}",
                        "url": f"{picurl}",
                        "picurl": f"{picurl}"
                    }
                ]
            }
        }
        return self._send(data)

    def _send(self, data):
        """
        发送消息的内部方法
        """
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        response = requests.post(self.webhook_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return True
        else:
            return False


# 使用示例：
if __name__ == "__main__":
    # 创建 WeChatRobot 实例
    robot = WeChatRobot(settings.webhook_url)
