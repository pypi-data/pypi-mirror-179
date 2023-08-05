from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func, event
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import relationship

from enowshop_models.base import Base
from enowshop_models.helpers.helpers import generate_uuid, generate_data


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36))
    keycloak_uuid = Column(String(37))
    name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    cpf = Column(String(11), unique=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user_address = relationship('UserAddress')
    user_phones = relationship('UsersPhones')


event.listen(Users, 'before_insert', generate_uuid)
event.listen(Users, 'before_insert', generate_data)
