from urllib import parse
from socketplay.main import sio
from sanic.log import logger
from sanic.response import json
from webconsole.controllers.active_hooks import ActiveHooksController
from socketplay.connection.authentication import check_authentication


@sio.on('connect')
async def on_connect(sid, environ):
    try:
        query_params = dict(parse.parse_qsl(environ['QUERY_STRING']))
        await check_authentication(sid, query_params.get('token', None))
    except Exception as e:
        logger.info('[AUTH ERROR] sid({}) - Client connection failed'.format(sid))
        return False

    logger.info('[CONNECTED] sid({}) - Client connected'.format(sid))
    controller = ActiveHooksController()
    data = await controller.insert({'sid': sid})

    return json(data)
