
import time
from typing import List
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enum import member
from itertools import count
import pandas as pd
import io
import os
import smtplib

from typing import Optional
from fastapi import BackgroundTasks, HTTPException, Query, Response,status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models

SENT_EMAILS_FILE = "C:/Users/ggashaw/Documents/sent_emails.txt"
def load_sent_emails() -> set:
    sent_emails = set()
    if os.path.exists(SENT_EMAILS_FILE):
        with open(SENT_EMAILS_FILE, "r") as f:
            for line in f:
                sent_emails.add(line.strip())
    return sent_emails

def save_sent_emails(sent_emails: set):
    with open(SENT_EMAILS_FILE, "w") as f:
        for email in sent_emails:
            f.write(email + "\n")

# def create_members(request: schemas.Members,db:Session):
#     new_member=models.Member(
#         first_name=request.first_name,
#         middle_name=request.middle_name,
#         last_name=request.last_name,
#         gender=request.gender,
#         phone=request.phone,
#         email=request.email,
#         birth_date=request.birth_date,
#         birth_place_region=request.birth_place_region,
#         birth_place_zone=request.birth_place_zone,
#         birth_place_wereda=request.birth_place_wereda,
#         birth_place_kebele=request.birth_place_kebele,
#         work_place=request.work_place,
#         country=request.country,
#         address_region=request.address_region,
#         address_zone=request.address_zone,
#         address_wereda=request.address_wereda,
#         payment_status=request.payment_status,
#         member_status=request.member_status,
#         membership_year=request.membership_year,
#         is_staff=request.is_staff
#         )
#     db.add(new_member)
#     db.commit()
#     db.refresh(new_member)
#     return new_member

def create_members(request: schemas.Members, db: Session, background_tasks: BackgroundTasks):
    # Create the member in the database
    new_member = models.Member(
        first_name=request.first_name,
        middle_name=request.middle_name,
        last_name=request.last_name,
        gender=request.gender,
        phone=request.phone,
        email=request.email,
        birth_date=request.birth_date,
        birth_place_region=request.birth_place_region,
        birth_place_zone=request.birth_place_zone,
        birth_place_wereda=request.birth_place_wereda,
        birth_place_kebele=request.birth_place_kebele,
        work_place=request.work_place,
        country=request.country,
        address_region=request.address_region,
        address_zone=request.address_zone,
        address_wereda=request.address_wereda,
        payment_status=request.payment_status,
        member_status=request.member_status,
        membership_year=request.membership_year,
        is_staff=request.is_staff
    )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    
    # Send email notification
    email_subject = "Congratulations!."
    email_message = f"Dear {new_member.first_name} {new_member.middle_name} {new_member.last_name} you have been registered  as staff member with email {new_member.email}. Thank you for being Abay Bank Staff Member"
    background_tasks.add_task(write_log, email_subject, new_member.email, email_message)
    
    return new_member

def get_all_members(db: Session, pagination_params: schemas.Pagination, first_name: str = None, status: str = None):
    query = db.query(models.Member).order_by(models.Member.first_name)

    if first_name is not None:
        query = query.filter(models.Member.first_name.ilike(f"%{first_name}%"))

    if status is not None:
        query = query.filter(models.Member.member_status == status)

    total_results = query.count()

    query = query.offset((pagination_params.page - 1) * pagination_params.perPage)
    query = query.limit(pagination_params.perPage)

    data = query.all()

    return {"count": total_results, "data": data}



# async def export_members_excel(
#     db: Session,
#     first_name: Optional[str] = None,
#     status: Optional[str] = None,
# ):
#     query = db.query(models.Member).order_by(models.Member.first_name)

#     if first_name:
#         query = query.filter(models.Member.first_name == first_name)

#     if status:
#         query = query.filter(models.Member.member_status == status)

#     members = query.all()

#     # Convert members data to DataFrame
#     member_dicts = [member.__dict__ for member in members]
#     df = pd.DataFrame(member_dicts)

#     # Prepare Excel file
#     output = io.BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')
#     df.to_excel(writer, index=False, sheet_name='Members')
#     writer.close()  # Close the writer to finalize the Excel file

#     # Get the Excel file content
#     excel_data = output.getvalue()

#     # Return Excel as downloadable file
#     return StreamingResponse(
#         io.BytesIO(excel_data),
#         media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#         headers={"Content-Disposition": "attachment; filename=members.xlsx"}
#     )

async def export_members_excel(
    db: Session,
    first_name: Optional[str] = None,
    status: Optional[str] = None,
):
    query = db.query(models.Member).order_by(models.Member.first_name)

    if first_name:
        query = query.filter(models.Member.first_name == first_name)

    if status:
        query = query.filter(models.Member.member_status == status)

    members = query.all()
    column_order = [
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'phone',
        'email',
        'birth_date',
        'birth_place_region',
        'birth_place_zone',
        'birth_place_wereda',
        'birth_place_kebele',
        'work_place',
        'country',
        'address_region',
        'address_zone',
        'address_wereda',
        'payment_status',
        'member_status',
        'membership_year',
        'is_staff'
    ]

    # Convert members data to DataFrame
    member_dicts = [member.__dict__ for member in members]
    df = pd.DataFrame(member_dicts, columns=column_order)

    # Define headers for the data
    headers = {
        'first_name': 'ስም',
        'middle_name': 'የአባት ስም',
        'last_name': 'የአያት ስም',
        'gender': 'ጾታ',
        'phone': 'ስልክ',
        'email': 'ኢ-ሜይል',
        'birth_date': 'የትውልድ ቀን',
        "birth_place_region":"የትውልድ ክልል",
        "birth_place_zone": "የትውልድ ዞን",
        "birth_place_wereda":"የትውልድ ወረዳ",
        "birth_place_kebele":"የትውልድ ቀበሌ",
       "work_place": "መስሪያ ቤት",
       "country": "ሃገር",
       "address_region": "የስራ ክልል",
        "address_zone": "የስራ ዞን",
        "address_wereda": "የስራ ወረዳ",
        "payment_status": "የክፍያ ሁኔታ"  ,
        "member_status": "የአባልነት ሁኔታ",
        "membership_year": "የአባልነት ዘመን",
        "is_staff": "የቅልማ ስታፍ?",
        # Add more headers for other columns as needed
    }
    

    # Rename DataFrame columns using the headers
  
    df = df.rename(columns=headers)

    # Prepare Excel file
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Members')
    writer.close()  # Close the writer to finalize the Excel file

    # Get the Excel file content
    excel_data = output.getvalue()

    # Return Excel as downloadable file
    return StreamingResponse(
        io.BytesIO(excel_data),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=members.xlsx"}
    )


def get_member_by_id(id:int,db:Session):
    member_data=db.query(models.Member).filter(models.Member.id==id)
    if not member_data.first():
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
    return member_data

def get_single_member(id:int, db:Session):
    data = db.query(models.Member).filter(models.Member.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return data

def update_member(id:int,request: schemas.Members,db:Session):
    blog = db.query(models.Member).filter(models.Member.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_member(id, db:Session):
    blog = db.query(models.Member).filter(models.Member.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable in the database",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return blog
    
# def get_all_emails(db: Session) -> List[str]:
# def get_all_emails() -> List[str]:
#     # all_members = db.query(models.Member).all()
#     all_members=["gashawgedef@gmail.com","getachewdereje6@gmail.com","melkamu372@gmail.com","getachewgedef12@gmail.com"]
    
#     if not all_members:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="No member info in the list",
#         )
    
#     all_emails = list(set(member for member in all_members))
#     return all_emails
def get_all_emails() -> List[str]:
    all_members = ["gashawgedef@gmail.com", "getachewdereje6@gmail.com", "getachewgedef12@gmail.com"]
    
    if not all_members:
        raise ValueError("No member info in the list")
    
    all_emails = list(set(all_members))  # Remove duplicates if any
    return all_emails

# def send_email_multiple(db: Session, email_subject: str, email_message: str):
#     all_emails = get_all_emails(db)
    
#     for email in all_emails:
#         if send_email(email_subject, email, email_message):
#             write_log(email_subject, email, email_message)
#         else:
#             print(f"Failed to send email to {email}")
# def send_email_multiple( email_subject: str, email_message: str, retries: int = 3, delay: float = 2.0):
#     all_emails = get_all_emails()
    
#     for email in all_emails:
#         success = False
#         for attempt in range(retries):
#             if send_email(email_subject, email, email_message):
#                 write_log(email_subject, email, email_message)
#                 success = True
#                 print(f"Email sent successfully to {email} on attempt {attempt + 1}")
#                 break
#             else:
#                 print(f"Failed to send email to {email} on attempt {attempt + 1}")
#                 time.sleep(delay)  # Wait before retrying
#         if not success:
#             print(f"Failed to send email to {email} after {retries} attempts")
# def send_email_multiple(email_subject: str, email_message: str, retries: int = 3, delay: float = 2.0):
#     all_emails = get_all_emails()

#     for email in all_emails:
#         success = False
#         for attempt in range(retries):
#             if send_email(email_subject, email, email_message):
#                 write_log(email_subject, email, email_message)
#                 success = True
#                 print(f"Email sent successfully to {email} on attempt {attempt + 1}")
#                 break
#             else:
#                 print(f"Failed to send email to {email} on attempt {attempt + 1}")
#                 time.sleep(delay)  # Wait before retrying
#         if not success:
#             print(f"Failed to send email to {email} after {retries} attempts")
# def send_email_multiple(email_subject: str, email_message: str, retries: int = 3, delay: float = 2.0):
#     all_emails = get_all_emails()
#     sent_emails = set()

#     for email in all_emails:
#         if email in sent_emails:
#             print(f"Email already sent to {email}, skipping...")
#             continue
        
#         success = False
#         for attempt in range(retries):
#             if send_email(email_subject, email, email_message):
#                 write_log(email_subject, email, email_message)
#                 sent_emails.add(email)  # Mark this email as sent
#                 success = True
#                 print(f"Email sent successfully to {email} on attempt {attempt + 1}")
#                 break
#             else:
#                 print(f"Failed to send email to {email} on attempt {attempt + 1}")
#                 time.sleep(delay)  # Wait before retrying
        
#         if not success:
#             print(f"Failed to send email to {email} after {retries} attempts")


def send_email_multiple(email_subject: str, email_message: str):
    all_emails = get_all_emails()
    sent_emails = load_sent_emails()

    for email in all_emails:
        if email in sent_emails:
            print(f"Email already sent to {email}, skipping...")
            continue
        
        if send_email(email_subject, email, email_message):
            write_log(email_subject, email, email_message)
            sent_emails.add(email)  # Mark this email as sent
            save_sent_emails(sent_emails)
            print(f"Email sent successfully to {email}")
        else:
            print(f"Failed to send email to {email}")
    print("Email sent completed")
# def load_sent_emails() -> set:
#     sent_emails = set()
#     if os.path.exists(SENT_EMAILS_FILE):
#         with open(SENT_EMAILS_FILE, "r") as f:
#             for line in f:
#                 sent_emails.add(line.strip())
#     return sent_emails

# def save_sent_emails(sent_emails: set):
#     with open(SENT_EMAILS_FILE, "w") as f:
#         for email in sent_emails:
#             f.write(email + "\n")            
def send_email(email_subject: str, email_address: str, email_message: str):
    sender_email = "gashawgedef@gmail.com"
    receiver_email = email_address
    password = "ugec npjo wmex oagi"
    # password = "enzakuna12@29"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email_subject

    # Add message body
    message.attach(MIMEText(email_message, "plain"))

    try:
        # Connect to SMTP server (Gmail) and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

def write_log(email_subject: str, email_address: str, email_message: str):
    log_file_path = "C:/Users/ggashaw/Documents/log.txt"

    with open(log_file_path, mode="a") as log:
        log.write(f"Email sent to: {email_address}\n")
        log.write(f"Subject: {email_subject}\n")
        log.write(f"Message: {email_message}\n")
        log.write("\n")  # Add a separator between log entries

    # Send email
    send_email(email_subject, email_address, email_message)

# def write_log(email_subject: str, email_address: str, email_message: str):
#     # Send email
#     send_email(email_subject, email_address, email_message)
def write_log(email_subject: str, email_address: str, email_message: str):
    log_file_path = "C:/Users/ggashaw/Documents/log.txt"
    # Specify absolute path here
    with open(log_file_path, mode="a") as log:
        log.write(f"Email sent to: {email_address}\n")
        log.write(f"Subject: {email_subject}\n")
        log.write(f"Message: {email_message}\n")
        log.write("\n")  # Add a separator between log entries
    
    # Send email
    send_email(email_subject, email_address, email_message)



def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"Sent Message: {q}\n"
        background_tasks.add_task(write_log, message)
    return q



def  get_these():
    return {"detail":"Gashaw Gedef"}