import aiohttp_jinja2
import jinja2
from aiohttp import web

from main import setup_routes
from utils.db_api import setup_db


async def init_func():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    app['static_root_url'] = '/static'
    app.router.add_static('/static/', path='./static', name='static')
    db = await setup_db()
    app['db'] = db
    await setup_routes(app)
    return app
