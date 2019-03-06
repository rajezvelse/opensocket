from socketplay.main import sio
from sanic.log import logger


@sio.on('join_discussion_channel', namespace='/chat')
async def join_discussion_channel(sid, *args):
    logger.info('[JOINED DISCUSSION CHANNEL] sid({}) - Client joined to discussion channel'.format(sid))
    sio.enter_room(sid=sid, room='discussion_channel', namespace='/chat')


@sio.on('leave_discussion_channel', namespace='/chat')
async def leave_discussion_channel(sid, *args):
    logger.info('[LEFT DISCUSSION CHANNEL] sid({}) - Client left from discussion channel'.format(sid))
    sio.leave_room(sid=sid, room='discussion_channel', namespace='/chat')
