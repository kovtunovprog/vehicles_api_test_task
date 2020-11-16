#!/usr/bin/env python

from aiohttp import web

from utils import init_func

app = init_func()

if __name__ == '__main__':
    web.run_app(app)
