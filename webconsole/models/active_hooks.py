from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean
)

from webconsole.models.base import Base


class ActiveHooks(Base):
    __tablename__ = 'active_hooks'

    id = Column(Integer, autoincrement=True, primary_key=True)
    sid = Column(String(255), nullable=False)
    hooked_at = Column(DateTime, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'sid': self.sid,
            'hooked_at': self.hooked_at
        }
