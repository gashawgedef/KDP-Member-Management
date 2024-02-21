from datetime import date
from msilib import Table
from operator import index
from turtle import title
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKey,Table
from sqlalchemy.orm import Mapped, mapped_column

from  database_connection import Base
from sqlalchemy.orm import relationship

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    birth_date: Mapped[str] = mapped_column()
    birth_place_region: Mapped[str] = mapped_column()
    birth_place_zone: Mapped[str] = mapped_column()
    birth_place_wereda: Mapped[str] = mapped_column()
    birth_place_kebele:Mapped[str]=mapped_column()
    work_place: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    address_region: Mapped[str] = mapped_column()
    address_zone: Mapped[str] = mapped_column()
    address_wereda: Mapped[str] = mapped_column()
    payment_status: Mapped[str]=mapped_column()  
    member_status : Mapped[str]=mapped_column()
    membership_year: Mapped[date] = mapped_column()
    is_staff: Mapped[bool]=mapped_column()
    educational_background = relationship("EducationalBackground", back_populates="member")

class EducationalBackground(Base):
    __tablename__ = "educational_backgrounds"
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    institution = Column(String)
    degree = Column(String)
    field_of_study = Column(String)
    year_completed = Column(Integer)
    member = relationship("Member", back_populates="educational_background")
    #user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class ProfessionType(Base):
    __tablename__ = "profession_types"
    id = Column(Integer, primary_key=True, index=True)
    profession_name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()



class MembershipPlan(Base):
    __tablename__ = 'membership_plan'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    duration = Column(String)
  



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    status = Column(Boolean)
    assigned_roles = relationship("Role", secondary="user_roles", backref="users")

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)
    description = Column(String)
    assigned_users = relationship("User", secondary="user_roles", backref="roles_assigned")

user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    extend_existing=True
)


class DonationType(Base):
    __tablename__='donation_Types'
    id=Column(Integer,primary_key=True,index=True)
    donation_name:Mapped[str]=mapped_column()
    description:Mapped[str]=mapped_column()

class Announcement(Base):
    __tablename__='announcemnents'
    id=Column(Integer,primary_key=True,index=True)
    title:Mapped[str]=mapped_column()
    content:Mapped[str]=mapped_column()
    posted_date:Mapped[str]=mapped_column()

class Project(Base):
    __tablename__='projects'
    id=Column(Integer,primary_key=True,index=True)
    project_name:Mapped[str]=mapped_column()
    description:Mapped[str]=mapped_column()
    start_date:Mapped[str]=mapped_column()
    end_date:Mapped[str]=mapped_column()
    estimated_budget:Mapped[str]=mapped_column()
    status:Mapped[str]=mapped_column()


class RecieptIssuer(Base):
    __tablename__='receipts_issuer'
    id=Column(Integer,primary_key=True,index=True)
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    place_region: Mapped[str] = mapped_column()
    place_zone: Mapped[str] = mapped_column()
    place_wereda: Mapped[str] = mapped_column()
    place_kebele: Mapped[str] = mapped_column()
    receipt_items = relationship('RecieptItems', back_populates='receipt_issuer')

class RecieptItems(Base):
    __tablename__='receipt_items'
    id=Column(Integer,primary_key=True,index=True)
    receipt_issuer_id = Column(Integer, ForeignKey('receipts_issuer.id'))
    identifier: Mapped[str] = mapped_column()
    from_number: Mapped[str] = mapped_column()
    to_number: Mapped[str] = mapped_column()
    date_taken: Mapped[date] = mapped_column()
    return_date: Mapped[date] = mapped_column(default=None)
    amount_birr: Mapped[float] = mapped_column(default=0.0)
    receipt_issuer = relationship('RecieptIssuer', back_populates='receipt_items')
   


