from operator import index
from turtle import title
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from  database_connection import Base
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
    member_address=relationship('MemberAddress',back_populates="members")

    #user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class ProfessionType(Base):
    __tablename__ = "profession_types"
    id = Column(Integer, primary_key=True, index=True)
    profession_name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

class MemberAddress(Base):
    __tablename__ = "members_address"    
    id = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    address_region: Mapped[str] = mapped_column()
    address_zone: Mapped[str] = mapped_column()
    address_wereda: Mapped[str] = mapped_column()
    annual_contribution: Mapped[float] = mapped_column()
    membership_year:Mapped[str]=mapped_column()
    member_id: Mapped[int] = mapped_column(ForeignKey("members.id"))
    members=relationship("Member",back_populates="member_address")

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

class EmployeeTax(Base):
    __tablename__='employee_taxes'
    id=Column(Integer,primary_key=True,index=True)
    employee_name:Mapped[str]=mapped_column()
    tin_no:Mapped[int]=mapped_column()
    basic_salary:Mapped[float]=mapped_column()
    transport_allowance:Mapped[float]=mapped_column()
    additional_benefits:Mapped[str]=mapped_column()
    taxable_income:Mapped[float]=mapped_column()
    tax_with_hold:Mapped[str]=mapped_column()
    net_pay:Mapped[float]=mapped_column()
    brance_name:Mapped[str]=mapped_column()


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username:Mapped[str]=mapped_column()
    role:Mapped[str]=mapped_column()
    password:Mapped[str]=mapped_column()
    status:Mapped[str]=mapped_column()
