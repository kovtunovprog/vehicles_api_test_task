from bson.objectid import ObjectId


async def create(db, data: dict = None):
    # Insert new instance to db
    veh = await db.vehicles.insert_one(data)
    return veh.inserted_id


async def get_veh_list(db, data: dict = None):
    # Return dict format {'vehicles': [vehicles list]}
    if data is None:
        data = {}
    veh_list = db.vehicles.find(data)
    veh_format_list = []
    async for veh in veh_list:
        veh['_id'] = str(veh['_id'])
        veh_format_list.append(veh)
    data = {'vehicles': veh_format_list}
    return data


async def get_veh_filtered(db, data: dict):
    vehicles = db.vehicles.find(data)
    vehicles_list = []
    async for veh in vehicles:
        veh['_id'] = str(veh['_id'])
        vehicles_list.append(veh)
    return vehicles_list


async def get_veh_by_id(db, veh_id=None):
    # Return instance by id
    if veh_id is None:
        return 'You have to give id'
    veh = await db.vehicles.find_one({'_id': ObjectId(veh_id)})
    if veh is None:
        return 'Object None'
    veh['_id'] = veh_id
    return veh


async def check_vin(db, vin=None):
    # Return instance by id
    if vin is None:
        return 'You have to give vin'
    print(vin)
    vin_res = await db.vehicles.find_one({'vin': vin})
    if vin_res:
        return False
    return True


async def update_instance(db, veh_id=None, data: dict = None):
    # Updated instance by id and returned instance
    if veh_id is None or data is None:
        return 'You have to give id'
    veh = await db.vehicles.update_one({'_id': ObjectId(veh_id)}, {'$set': data})
    # veh['_id'] = veh_id
    return veh


async def delete_instance(db, veh_id=None):
    if veh_id is None:
        return 'You have to give id'
    await db.vehicles.delete_one({'_id': ObjectId(veh_id)})
