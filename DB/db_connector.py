from typing import Optional
from sqlalchemy import create_engine, MetaData, Column, Integer, String, DateTime, ForeignKey
import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from .models import Base, engine, FlowDb, ProductDb


Base.metadata.create_all(engine)
SessionDb = sessionmaker(bind=engine)()

# test = ProductDb(product_name='Сыр2')
# test2 = ProductDb(product_name='молоко2')
# flow_list = [FlowDb(
#     flow_exp='дом'), FlowDb(flow_exp='дом2'), FlowDb(
#     flow_exp='дом3'), FlowDb(flow_exp='дом4')]
# SessionDb.add_all([test, test2, *flow_list])
# print(SessionDb.query(ProductDb).all())
# # session.add_all([test, test2])
# SessionDb.commit()
