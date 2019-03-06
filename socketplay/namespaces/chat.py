import socketio
from socketplay.main import sio
from sanic.log import logger


class ChatNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        logger.info("[NAMESPACE SUBSCRIBED] sid({}) - Client connected to namespace 'chat'")
        pass

    def on_disconnect(self, sid):
        logger.info("[NAMESPACE UNSUBSCRIBED] sid({}) - Client disconnected from namespace 'chat'")
        pass

    async def on_message(self, sid, message):
        await self.emit('message', message, skip_sid=sid, room=message.get('room', None))


sio.register_namespace(ChatNamespace('/chat'))