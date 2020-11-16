from datetime import datetime

from aiohttp import web
from aiohttp_jinja2 import template
from bson.errors import InvalidId

from utils.db_api.quick_commands import create, get_veh_by_id, get_veh_list, update_instance, delete_instance
from utils.validation import validation


@template('index.html')
async def index(request):
    return {}


FIELDS = {'vendor', 'model', 'year', 'color', 'vin'}


class ApiVehiclesView(web.View):
    async def get(self):
        # Returns list of all vehicles or if have get params returns filtered vehicles list
        db = self.request.app['db']

        get_filter = {}
        for f in FIELDS:
            get_value = self.request.query.get(f)
            if f in self.request.query and get_value != '':
                get_filter[f] = get_value

        veh_list = await get_veh_list(db, get_filter)
        if not veh_list['vehicles'] != []:
            return web.Response(status=422, text='Does not exist')
        return web.json_response(status=200, data=veh_list)

    async def post(self):
        # Created new vehicle
        db = self.request.app['db']
        post_data = await self.request.json()
        code, text = await validation(db, post_data, FIELDS)
        if code != 1:
            return web.Response(status=code, text=text)
        data = dict(post_data)
        veh_id = await create(db=db, data=data)
        data['_id'] = str(veh_id)
        # Return created vehicle
        return web.json_response(status=201, data=data)


async def get_instance(request):
    db = request.app['db']
    veh_id = request.match_info['id']
    try:
        veh = await get_veh_by_id(db, veh_id)
    except InvalidId:
        return web.Response(text=f'Vehicle {veh_id} does not exist ')
    return web.json_response(status=201, data=veh)


async def edit(request):
    # Edited vehicle
    db = request.app['db']
    veh_id = request.match_info['id']
    put_data = await request.json()
    code, text = await validation(db, put_data, FIELDS)
    if code != 1:
        return web.Response(status=code, text=text)
    await update_instance(db, veh_id, put_data)
    return web.Response(status=202)


async def delete(request):
    # Delete vehicle
    veh_id = request.match_info['id']
    db = request.app['db']
    await delete_instance(db, veh_id)
    return web.json_response(status=204)


