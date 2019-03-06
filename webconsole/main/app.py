# import sys
# from pathlib import Path
# sys.path.append(str(Path('.').absolute().parent))  # Add dir to PYTHONPATH

from sanic import Sanic
from sanic.log import logger
from jinja2 import Environment, PackageLoader
from core import importdir
import os

# Importing settings
from webconsole.main import settings

# Create application
application = Sanic()
application.config.from_object(settings.DEFAULT_SETTINGS)

jinjaEnv = Environment(loader=PackageLoader('webconsole', 'ui'))

# Serves files from the static folder to the URL /static
application.static('/assets', os.path.join(settings.BASE_DIR, 'ui', 'assets'))
application.static('/ui-templates', os.path.join(settings.BASE_DIR, 'ui', 'templates'))
# Importing application routing
import webconsole.main.urls


@application.listener('before_server_start')
async def on_server_start(app, loop):
    logger.info("[APPLICATION STARTED]")


@application.listener('after_server_stop')
async def on_server_stop(app, loop):
    logger.info("[APPLICATION STOPPED]")
