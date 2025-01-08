"""A Data Dictionary contains details regarding data withing a Business, Application, Process, etc.

A Data Dictionary object contains detailed information regarding data that is created and managed in support of any process (Business, Application, etc.)
The information captured for the data includes details regarding format, relationships to other data/information, lineage, lifecycle, etc.

    Attributes:
            workbook_filename (str): The full filename path to the Excel workbook
            worksheets (int):  A dictionary containing the Excel worksheets in the Excel workbook
            defined_names (str): An array of the defined names in the Excel workbook


    Methods
    -------

"""
from __future__ import annotations

__version__ = '2024.11'
__author__ = 'David Hartman'
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"