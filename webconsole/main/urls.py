from webconsole.main.app import application
from webconsole.views.views import index

application.add_route(index, '/', methods=['GET'], name='index')
