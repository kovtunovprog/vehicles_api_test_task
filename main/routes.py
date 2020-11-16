from aiohttp import web

from main.views import index, ApiVehiclesView, get_instance, edit, delete


async def setup_routes(app):
    app.add_routes([
        web.get('/', index),
        web.view('/api/1.0/vehicles', ApiVehiclesView),
        web.get('/api/1.0/vehicles/{id}', get_instance),
        web.put('/api/1.0/vehicles/{id}', edit),
        web.delete('/api/1.0/vehicles/{id}', delete)
    ])
