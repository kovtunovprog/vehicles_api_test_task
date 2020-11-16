from datetime import datetime

from utils.db_api.quick_commands import check_vin


async def validation(db, data: dict, FIELDS):
    code = 1
    text = ''
    if set(data.keys()) != FIELDS:
        code = 422
        text= 'Unsupported field set'
    try:
        year = int(data['year'])
    except ValueError:
        code = 422
        text = 'Year is not a number'
        return code, text
    if year < 1900 or year > datetime.now().year:
        code = 422
        text = 'Invalid year value'
    al = await check_vin(db, data['vin'])
    print(al)
    if (al) is False:
        code = 409
        text = 'Already exists'

    return code, text