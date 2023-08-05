
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, event
from sqlalchemy.dialects.postgresql import ENUM

from enowshop_models.base import Base
from enowshop_models.helpers.helpers import generate_data


class ProvidersPhones(Base):
    __tablename__ = 'providers_phones'

    id = Column(Integer, primary_key=True)
    type = Column(ENUM('Cell', 'Telephone', name='PhoneTypesProviders'))
    number = Column(String(12))
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    provider_id = Column(Integer, ForeignKey('providers.id'))


event.listen(ProvidersPhones, 'before_insert', generate_data)