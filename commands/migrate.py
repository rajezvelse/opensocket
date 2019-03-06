from core.BaseCommand import BaseCommand
from webconsole.main.settings import SETTINGS, BASE_DIR
from webconsole.main.app import application
from alembic.config import Config
from alembic import command
import os


class Command(BaseCommand):
    description = "Update database schema"

    def execute(self, **kwargs):
        alembic_cfg = Config(os.path.join(BASE_DIR, "alembic.ini"))
        alembic_cfg.set_main_option("script_location", "webconsole:migrations")

        # Make migrations
        command.revision(alembic_cfg, "", autogenerate=True)
        # Migarate
        command.upgrade(alembic_cfg, "head")
