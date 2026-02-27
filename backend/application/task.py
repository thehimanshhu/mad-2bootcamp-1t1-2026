from celery import shared_task
from time import sleep
from jinja2 import Template 
from .mail import send_email
@shared_task(name = "add_together" , ignore_result = False)
def add_together(a, b ):
    sleep(10)
    return a + b

from .models import Role , db , Package , Booking
import csv
@shared_task(name="customer" , ignore_result = False)
def customer_csv(cust_id):
    sleep(10)
    bookings = db.session.query(Booking).filter_by(cust_id = cust_id).all()
    csv_filename = f"customer-{cust_id}.csv"

    with open(f"./static/{csv_filename}" , "w") as file:
        writerobj = csv.writer( file , delimiter=",")
        writerobj.writerow(["Sr NO." , "Package Name" , "Professional Name" , "Professional Email" , "Booking Date" , "Booking Status"])

        for index, booking in enumerate(bookings):
            writerobj.writerow([index + 1, booking.package.title , booking.professional.name , booking.professional.email , booking.date , booking.status])
    return csv_filename



from .utility import render_email_template
@shared_task(name="Admin_monthly_Report" , ignore_result = False)
def admin_monthly_report():
    bookings = db.session.query(Booking).all()
    admin = db.session.query(Role).filter_by(name = "admin").first().users[0]   
    username = "Admin"

    email_content = render_email_template( username , bookings , "./templates/admin_montly_report.html")
    send_email(admin.email , "Here is montly booking report!!" ,  email_content)
    return "Email Sent!!"
    

