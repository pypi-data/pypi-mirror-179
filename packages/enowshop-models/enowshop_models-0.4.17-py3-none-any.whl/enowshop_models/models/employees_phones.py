
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, DateTime, func, event

from enowshop_models.base import Base
from enowshop_models.helpers.helpers import generate_data
from sqlalchemy.dialects.postgresql import ENUM


class EmployeesPhones(Base):
    __tablename__ = 'employees_phones'

    id = Column(Integer, primary_key=True)
    type = Column(ENUM('Cell', 'Telephone', name='PhoneTypesEmployees'))
    number = Column(String(12))
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    employees_id = Column(Integer, ForeignKey('employees.id'))


event.listen(EmployeesPhones, 'before_insert', generate_data)