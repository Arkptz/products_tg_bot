from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session, sessionmaker
from sqlalchemy import create_engine, MetaData, Column, Integer, String, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
from config import db_path

engine = create_engine(f'sqlite:///{db_path}', echo=True,
                       connect_args={"check_same_thread": False})
conn = engine.connect()

class Base(DeclarativeBase):
    pass


class ProductDb(Base):
    __tablename__ = "Product"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(300))
    clicks: Mapped[int] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, product_name={self.product_name!r}"


class FlowDb(Base):
    __tablename__ = "Flow"
    id: Mapped[int] = mapped_column(primary_key=True)
    flow_exp: Mapped[str] = mapped_column(String(300))
    clicks: Mapped[int] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Flow(id={self.id!r}, flow={self.flow_exp}!r)"

class AdminDb(Base):
    __tablename__ = "Admin"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()


class ExpenditureDb(Base):
    __tablename__ = "Expenditure"
    id: Mapped[int] = mapped_column(primary_key=True)
    time: Mapped[float] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    user_id: Mapped[int] = mapped_column()
    product: Mapped[str] = mapped_column()
    flow_direction: Mapped[str] = mapped_column()
    count: Mapped[float] = mapped_column()
    price: Mapped[float] = mapped_column()

class ComingDb(Base):
    __tablename__ = "Coming"
    id: Mapped[int] = mapped_column(primary_key=True)
    time: Mapped[float] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    user_id: Mapped[int] = mapped_column()
    product: Mapped[str] = mapped_column()
    count: Mapped[float] = mapped_column() 



