#!/bin/bash

# 启动 gunicorn 服务
gunicorn main:app -c gunicorn.py --daemon

# 检查 gunicorn 是否成功启动
if [ $? -eq 0 ]; then
    echo "Gunicorn started successfully."
else
    echo "Failed to start Gunicorn."
fi
