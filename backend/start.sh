#!/bin/bash

# ANSI 转义序列
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 启动 gunicorn 服务
gunicorn main:app -c gunicorn.py --daemon

# 检查 gunicorn 是否成功启动
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Gunicorn started successfully.${NC}"
else
    echo -e "${RED}Failed to start Gunicorn.${NC}"
fi
