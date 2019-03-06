from webconsole.controllers.base_controller import BaseController
from webconsole.models.active_hooks import ActiveHooks
from webconsole.main.database import scoped_session
import datetime


class ActiveHooksController(BaseController):
    model = ActiveHooks

    async def insert(self, data):
        with scoped_session() as db:
            instance = self.model()
            instance.sid = data.get('sid', None)
            instance.hooked_at = datetime.datetime.now()
            db.add(instance)

            record = db.query(self.model).order_by(self.model.id.desc()).first().serialize()
            return record

    async def delete(self, sid):
        with scoped_session() as db:
            db.query(self.model).filter_by(sid=sid).delete()
            return True
