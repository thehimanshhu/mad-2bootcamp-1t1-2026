from celery import shared_task
from time import sleep
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
    return f"./static/{csv_filename}"
