# -*- coding: utf-8 -*-

from uvicorn import run

from api import app

# app = create_app()

if __name__ == '__main__':
    run(host="0.0.0.0",app="main:app", reload=True)
