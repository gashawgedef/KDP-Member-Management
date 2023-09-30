from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..database.database_connection import Base
from sqlalchemy.orm import relationship


class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    profession: Mapped[str] = mapped_column()
    birth_date: Mapped[str] = mapped_column()
    birth_place_region: Mapped[str] = mapped_column()
    birth_place_zone: Mapped[str] = mapped_column()
    birth_place_wereda: Mapped[str] = mapped_column()
    birth_place_kebele:Mapped[str]=mapped_column()

    #user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
