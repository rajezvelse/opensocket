from socketplay.main import sio
from sanic.log import logger
from sanic.response import json
from webconsole.controllers.active_hooks import ActiveHooksController


@sio.on('disconnect')
async def on_disconnect(sid):
    logger.info('[DISCONNECTED] sid({}) - Client disconnected'.format(sid))
    controller = ActiveHooksController()
    await controller.delete(sid)
    return
