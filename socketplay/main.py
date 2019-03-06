import socketio
from core import importdir

sio = socketio.AsyncServer(async_name="sanic")

importdir.do('socketplay/events', globals())
importdir.do('socketplay/connection', globals())
importdir.do('socketplay/namespaces', globals())
importdir.do('socketplay/rooms', globals())