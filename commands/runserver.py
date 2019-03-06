from core.BaseCommand import BaseCommand
from webconsole.main.settings import SETTINGS
from webconsole.main.app import application
from socketplay.main import sio


class Command(BaseCommand):
    description = "Start server instance"

    def create_args(self):
        self.parser.add_argument('--host', '-H', type=str, default=SETTINGS['SERVER_HOST'], help='Host in which the server to be run')
        self.parser.add_argument('--port', '-P', type=int, default=SETTINGS['SERVER_PORT'], help='Port in which the server to be run')

    def execute(self, **kwargs):
        sio.attach(application)
        application.run(host=kwargs['host'], port=kwargs['port'])
