#!/bin/bash

# 设置gunicorn进程的pid文件路径
PID_FILE="gunicorn.pid"

# 设置gunicorn启动命令
GUNICORN_CMD="gunicorn main:app -c gunicorn.py --daemon"

# 函数：启动gunicorn
start_gunicorn() {
    if [ -f "$PID_FILE" ]; then
        echo "Gunicorn is already running."
    else
        echo "Starting Gunicorn..."
        $GUNICORN_CMD
        echo "Gunicorn started."
    fi
}

# 函数：停止gunicorn
stop_gunicorn() {
    if [ -f "$PID_FILE" ]; then
        echo "Stopping Gunicorn..."
        kill -TERM $(cat "$PID_FILE")
        rm "$PID_FILE"
        echo "Gunicorn stopped."
    else
        echo "Gunicorn is not running."
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
        echo "Gunicorn is running with PID: $(cat "$PID_FILE")"
    else
        echo "Gunicorn is not running."
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
