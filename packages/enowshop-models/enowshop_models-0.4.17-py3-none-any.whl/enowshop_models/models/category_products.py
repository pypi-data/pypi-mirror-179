from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from enowshop_models.base import Base


class CategoryProducts(Base):
    __tablename__ = 'category_products'

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey('products.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship('Category')
    product = relationship('Products')

    __mapper_args__ = {"eager_defaults": True}

