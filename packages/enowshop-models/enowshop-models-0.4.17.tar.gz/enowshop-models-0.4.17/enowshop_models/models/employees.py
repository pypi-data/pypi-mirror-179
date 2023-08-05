from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy import func, event
from sqlalchemy.orm import relationship

from enowshop_models.base import Base
from enowshop_models.helpers.helpers import generate_data, generate_uuid


class Employees(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    uuid = Column(String(36))
    keycloak_uuid = Column(String(37))
    last_name = Column(String(50))
    cpf = Column(String(11), unique=True)
    position = Column(String(100))
    salary = Column(Integer)
    birth_date = Column(Date)
    admission_date = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    employees_phones = relationship('EmployeesPhones')


event.listen(Employees, 'before_insert', generate_data)
event.listen(Employees, 'before_insert', generate_uuid)
