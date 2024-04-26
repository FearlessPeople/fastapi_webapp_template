#!/bin/bash

# 设置gunicorn进程的pid文件路径
PID_FILE="gunicorn.pid"

# 设置gunicorn启动命令
GUNICORN_CMD="gunicorn main:app -c gunicorn.py --daemon"

# ANSI颜色代码
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 函数：获取当前时间
current_time() {
    echo -n "$(date +'%Y-%m-%d %H:%M:%S') "
}

# 函数：启动gunicorn
start_gunicorn() {
    if [ -f "$PID_FILE" ]; then
        echo -e "$(current_time)${GREEN}Gunicorn is already running.${NC}"
    else
        echo -e "$(current_time)${GREEN}Starting Gunicorn...${NC}"
        $GUNICORN_CMD
        echo -e "$(current_time)${GREEN}Gunicorn started.${NC}"
    fi
}

# 函数：停止gunicorn
stop_gunicorn() {
    if [ -f "$PID_FILE" ]; then
        echo -e "$(current_time)${GREEN}Stopping Gunicorn...${NC}"
        kill -TERM $(cat "$PID_FILE")
        rm "$PID_FILE"
        echo -e "$(current_time)${GREEN}Gunicorn stopped.${NC}"
    else
        echo -e "$(current_time)${RED}Gunicorn is not running.${NC}"
    fi
}

# 函数：重启gunicorn
restart_gunicorn() {
    stop_gunicorn
    start_gunicorn
}

# 函数：检查gunicorn状态
status_gunicorn() {
    if [ -f "$PID_FILE" ]; then
        echo -e "$(current_time)${GREEN}Gunicorn is running with PID: $(cat "$PID_FILE")${NC}"
    else
        echo -e "$(current_time)${RED}Gunicorn is not running.${NC}"
    fi
}

# 检查命令参数
case "$1" in
    start)
        start_gunicorn
        ;;
    stop)
        stop_gunicorn
        ;;
    restart)
        restart_gunicorn
        ;;
    status)
        status_gunicorn
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac

exit 0
