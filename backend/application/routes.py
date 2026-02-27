from flask import current_app as app
from flask import request,send_from_directory
from flask_security import  auth_required , roles_required , current_user, SQLAlchemyUserDatastore , hash_password
from flask_security.utils import verify_and_update_password 
from .models import db , User , Role , Package , Booking , CustomerProfile , ProfessionalProfile
from datetime import datetime
from sqlalchemy import and_ , or_
@app.route("/")
def home():
    return "Welcome to my application!"

@app.route("/login" , methods=["POST"])
def login():
    if request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")
        datastore:SQLAlchemyUserDatastore = app.security.datastore  
        user = datastore.find_user(email=email)
        print(user)
        if user :
            if verify_and_update_password(password , user   ):
                return {"message":"Login successful" , "user": user.email , "token" : user.get_auth_token() , "role": user.roles[0].name}, 200
            else:
                return {"message":"Invalid password"}, 401
        else:
            return {"message":"email does not exist"}, 401
    else:
        return {"message":"Method not allowed"}, 405

@app.route("/register" , methods=["POST"])
def register():
    if request.args.get("role") == "customer":
        print("customer registration")
        name = request.json.get("name")
        email = request.json.get("email")
        password = request.json.get("password")
        address = request.json.get("address")
        mobile = request.json.get("mobile")
        print("the name is:", name)
        print("the email is:", email)
        print("the mobile is:", mobile)
        print("the address is:", address)
        datastore = app.security.datastore
        if datastore.find_user(email=email):
            return {"message":"email already exists"}, 400
        print("creating user")
        user = datastore.create_user(name=name , email=email , password=hash_password(password) , roles=["customer"])
        db.session.commit()
        customer_profile = CustomerProfile(name=name , email=email , address=address , mobile=mobile , user_id=user.id , status="Active")
        db.session.add(customer_profile)
        db.session.commit()
        return {"message":"Customer registered successfully"}, 201
    elif request.args.get("role") == "professional":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        address = request.form.get("address")
        mobile = request.form.get("mobile")
        resume = request.files.get("resume")
        print("the name is:", name  )
        datastore = app.security.datastore
        print("hi")
        if datastore.find_user(email=email):
            return {"message":"email already exists"}, 400
        print("Hello")
        user = datastore.create_user(name=name , email=email , password=hash_password(password) , roles=["professional"])

        db.session.commit()
        
        resume_url = None
        if resume:
            resume_url = f"static/{email}.pdf"
            resume.save(resume_url)
        
        professional_profile = ProfessionalProfile(name=name , email=email , address=address , mobile=mobile , resume_url=resume_url , user_id=user.id , status="Registered")
        db.session.add(professional_profile)
        db.session.commit()
        return {"message":"Professional registered successfully"}, 201

# @app.route("/protected")
# @auth_required("token")
# @roles_required("admin")
# def protected():
#     return {"message":"This is a protected route"}, 200


@app.route("/api/professionals")
@auth_required("token")
def get_professionals():
    professionals = ProfessionalProfile.query.all()
    result = { "Active": [] , "Registered": [] , "Flagged":[] }
    for professional in professionals:
        print(professional.name , professional.status  )
        if professional.status=="Active":
            result["Active"].append({
                "prof_id" : professional.id,
                "Professional Name": professional.name,
                "Professional Email": professional.email,
                "Address": professional.address,
                "Mobile": professional.mobile,
                "Professional Resume URL": professional.resume_url,
                "Status": professional.status
            })
        elif professional.status=="Registered":
            result["Registered"].append({
                "prof_id" : professional.id,
               "Professional Name": professional.name,
                "Professional Email": professional.email,
                "Address": professional.address,
                "Mobile": professional.mobile,
                "Professional Resume URL": professional.resume_url,
                "Status": professional.status
            })
        elif professional.status=="Flagged":
            result["Flagged"].append({
                "prof_id" : professional.id,
                "Professional Name": professional.name,
                "Professional Email": professional.email,
                "Address": professional.address,
                "Mobile": professional.mobile,
                "Professional Resume URL": professional.resume_url,
                "Status": professional.status
            })
    print(result)
    return result, 200


@app.route("/api/customers")
def get_customers():
    customers = CustomerProfile.query.all()
    result = {"Active" : [] , "Flagged" : []}
    for customer in customers:
        if customer.status == "Active":
            result["Active"].append({
                "customer_id": customer.id,
                "Customer Name": customer.name,
                "Customer Email": customer.email,
                "Address": customer.address,
                "Mobile": customer.mobile,
                "Status" : customer.status
            })
        elif customer.status == "Flagged":
            result["Flagged"].append({
                "customer_id": customer.id,
                "Customer Name": customer.name,
                "Customer Email": customer.email,
                "Address": customer.address,
                "Mobile": customer.mobile,
                "Status" : customer.status
            })
    return  result, 200


@app.route("/api/approve-professional/<int:prof_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def approve_professional(prof_id):
    professsional  = db.session.query(ProfessionalProfile).filter_by(id=prof_id).first()
    if professsional:
        if professsional.status == "Registered":
            professsional.status = "Active"
            db.session.commit()
            return {"message": "Professional approved successfully"}, 200
        else:
            return {"message": "Professional is not in Registered status"}, 400
    else:
        return {"message": "Professional not found"}, 404
    

@app.route("/api/reject-professional/<int:prof_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def reject_professional(prof_id):
    professsional  = db.session.query(ProfessionalProfile).filter_by(id=prof_id).first()
    if professsional:
        if professsional.status == "Registered":
            professsional.status = "Rejected"
            db.session.commit()
            return {"message": "Professional rejected successfully"}, 200
        else:
            return {"message": "Professional is not in Registered status"}, 400
    else:
        return {"message": "Professional not found"}, 404

@app.route("/api/flag-professional/<int:prof_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def flag_professional(prof_id):
    professsional  = db.session.query(ProfessionalProfile).filter_by(id=prof_id).first()
    if professsional:
        if professsional.status == "Active":
            professsional.status = "Flagged"
            db.session.commit()
            return {"message": "Professional flagged successfully"}, 200
        else:
            return {"message": "Professional is not in Active status"}, 400
    else:
        return {"message": "Professional not found"}, 404
   

    
@app.route("/api/unflag-professional/<int:prof_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def unflag_professional(prof_id):
    professsional  = db.session.query(ProfessionalProfile).filter_by(id=prof_id).first()
    if professsional:
        if professsional.status == "Flagged":
            professsional.status = "Active"
            db.session.commit()
            return {"message": "Professional unflagged successfully"}, 200
        else:
            return {"message": "Professional is not in Flagged status"}, 400
    else:
        return {"message": "Professional not found"}, 404
   

@app.route("/api/flag-customer/<int:cust_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def flag_customer(cust_id):
    customer  = db.session.query(CustomerProfile).filter_by(id=cust_id).first()
    if customer:
        if customer.status == "Active":
            customer.status = "Flagged"
            db.session.commit()
            return {"message": "Customer flagged successfully"}, 200
        else:
            return {"message": "Customer is not in Active status"}, 400
    else:
        return {"message": "Customer not found"}, 404
   

    
@app.route("/api/unflag-customer/<int:cust_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def unflag_customer(cust_id):
    customer  = db.session.query(CustomerProfile).filter_by(id=cust_id).first()
    if customer:
        if customer.status == "Flagged":
            customer.status = "Active"
            db.session.commit()
            return {"message": "Customer unflagged successfully"}, 200
        else:
            return {"message": "Customer is not in Flagged status"}, 400
    else:
        return {"message": "Customer not found"}, 404
   

@app.route("/api/create-package" , methods=["POST"])
@auth_required("token")
@roles_required("professional")
def create_package():
    title = request.json.get("title")
    description = request.json.get("description")
    price = request.json.get("price")
    start_date = request.json.get("start_date")
    end_date = request.json.get("end_date")
    prof_id = current_user.id
    package = db.session.query(Package).filter_by(title=title).first()
    if package:
        return {"message": "Package with this title already exists"}, 400
    package = Package(title=title , description=description , price=price , start_date=datetime.strptime(start_date , "%Y-%m-%d").date() , end_date=datetime.strptime(end_date , "%Y-%m-%d").date() , prof_id=prof_id , status="Active")
    db.session.add(package)
    db.session.commit()
    print("Package created successfully")
    return {"message": "Package created successfully"}, 201



@app.route("/api/get-packages" , methods=["GET"])
@auth_required("token")
def get_packages():
    if current_user.roles[0].name == "professional":
        packages = db.session.query(Package).filter_by(prof_id=current_user.id).all()
        packs = []
        for package in packages:
            packs.append({
                "id": package.id,
                "title": package.title,
                "description": package.description,
                "price": package.price,
                "start_date": package.start_date.strftime("%Y-%m-%d"),
                "end_date": package.end_date.strftime("%Y-%m-%d"),
                "status": package.status
            })
        print(packs)
        return packs, 200
    elif current_user.roles[0].name == "customer":
        packages = db.session.query(Package).filter(and_(Package.status=="Active" , Package.start_date <=datetime.now().date() , Package.end_date >=datetime.now().date() )).all()
        packs = []
        for package in packages:
            packs.append({
                "id": package.id,
                "title": package.title,
                "description": package.description,
                "price": package.price,
                "start_date": package.start_date.strftime("%Y-%m-%d"),
                "end_date": package.end_date.strftime("%Y-%m-%d"),
                "status": package.status , 
                "professional_name": package.professional.name,
                "professional_email": package.professional.email,
                "professional_mobile": package.professional.professional_profile.mobile,
            })
        return packs, 200



@app.route("/api/getpackage/<int:pack_id>" , methods=["GET"])
def get_package(pack_id):
    package = db.session.query(Package).filter(and_(Package.id==pack_id , Package.status=="Active" ,Package.start_date <=datetime.now().date() , Package.end_date >=datetime.now().date() )).first()
    if package:
        return {
            "id": package.id,
            "title": package.title,
            "description": package.description,
                "price": package.price,
                "start_date": package.start_date.strftime("%Y-%m-%d"),
                "end_date": package.end_date.strftime("%Y-%m-%d"),
                "status": package.status , 
                "professional_name": package.professional.name,
                        "professional_email": package.professional.email,
                        "professional_mobile": package.professional.professional_profile.mobile,
            } , 200
    else:
        return {"message": "Package not found or inactive"}, 404


@app.route("/api/book-package/<int:pack_id>" , methods=["POST"])
@auth_required("token")
@roles_required("customer")
def book_package(pack_id):
    package= db.session.query(Package).filter_by(id=pack_id).first()
    if package:
        if package.status != "Active" and not (package.start_date <=datetime.now().date() and package.end_date >=datetime.now().date()):
            return {"message": "Package is not active"}, 400
        start_date = request.json.get("start_date")
        start_time = request.json.get("start_time")
        total_price = package.price
        booking = Booking( total_price=total_price , start_time=datetime.strptime(start_time , "%H:%M").time() , end_time=datetime.strptime(start_time , "%H:%M").time() , date=datetime.strptime(start_date , "%Y-%m-%d").date() , status="Requested" , prof_id=package.prof_id , pack_id=pack_id , cust_id=current_user.id)
        db.session.add(booking)
        db.session.commit()
        return {"message": "Package booked successfully"}, 201

@app.route("/api/getbookings") 
@auth_required("token")
def getbookings():
    if current_user.roles[0].name =="customer":
        requested_bookings = db.session.query(Booking).filter(and_(Booking.cust_id == current_user.id , Booking.status=="Requested")).all()
        requested_bookings_list = []
        for booking in requested_bookings:
            requested_bookings_list.append({
                "booking_id": booking.id,
                "package_title": booking.package.title,
                "start_time": booking.start_time.strftime("%H:%M"),
                "end_time": booking.end_time.strftime("%H:%M"),
                "date": booking.date.strftime("%Y-%m-%d"),
                "status": booking.status ,
                "professional_email": booking.professional.email,
                "professional_mobile": booking.professional.professional_profile.mobile,
                "professional_name" : booking.professional.name
            })

        accepted_bookings = db.session.query(Booking).filter(and_(Booking.cust_id == current_user.id , Booking.status=="Accepted")).all()
        accepted_bookings_list = []
        for booking in accepted_bookings:
            accepted_bookings_list.append({
                "booking_id": booking.id,
                "package_title": booking.package.title,
                "start_time": booking.start_time.strftime("%H:%M"),
                "end_time": booking.end_time.strftime("%H:%M"),
                "date": booking.date.strftime("%Y-%m-%d"),
                "status": booking.status ,
                "professional_email": booking.professional.email,
                "professional_mobile": booking.professional.professional_profile.mobile,
                "professional_name" : booking.professional.name
            })
        rejected_bookings = db.session.query(Booking).filter(and_(Booking.cust_id == current_user.id ,or_( Booking.status=="Rejected" , Booking.status=="Completed"))).all() 
        rejected_bookings_list = []
        for booking in rejected_bookings:
            rejected_bookings_list.append({
                "booking_id": booking.id,
                "package_title": booking.package.title,
                "start_time": booking.start_time.strftime("%H:%M"),
                "end_time": booking.end_time.strftime("%H:%M"),
                "date": booking.date.strftime("%Y-%m-%d"),
                "status": booking.status ,
                "professional_email": booking.professional.email,
                "professional_mobile": booking.professional.professional_profile.mobile,
                "professional_name" : booking.professional.name
            })
        bookings = {"Accepted" : accepted_bookings_list , "Requested" : requested_bookings_list , "Rejected/Completed" : rejected_bookings_list}
        print("Requested")
        return bookings, 200

    if current_user.roles[0].name =="professional":
        requested_bookings = db.session.query(Booking).filter(and_(Booking.prof_id == current_user.id , Booking.status=="Requested")).all()
        requested_bookings_list = []
        for booking in requested_bookings:
            requested_bookings_list.append({
                "booking_id": booking.id,
                "package_title": booking.package.title,
                "start_time": booking.start_time.strftime("%H:%M"),
                "end_time": booking.end_time.strftime("%H:%M"),
                "date": booking.date.strftime("%Y-%m-%d"),
                "status": booking.status ,
                "customer_email": booking.customer.email,
                "customer_mobile": booking.customer.customer_profile.mobile,
                "customer_name" : booking.customer.name
            })

        accepted_bookings = db.session.query(Booking).filter(and_(Booking.prof_id == current_user.id , Booking.status=="Accepted")).all()
        accepted_bookings_list = []
        for booking in accepted_bookings:
            accepted_bookings_list.append({
                "booking_id": booking.id,
                "package_title": booking.package.title,
                "start_time": booking.start_time.strftime("%H:%M"),
                "end_time": booking.end_time.strftime("%H:%M"),
                "date": booking.date.strftime("%Y-%m-%d"),
                "status": booking.status ,
                "customer_email": booking.customer.email,
                "customer_mobile": booking.customer.customer_profile.mobile,
                "customer_name" : booking.customer.name
            })
        rejected_bookings = db.session.query(Booking).filter(and_(Booking.prof_id == current_user.id ,or_( Booking.status=="Rejected" , Booking.status=="Completed"))).all() 
        rejected_bookings_list = []
        for booking in rejected_bookings:
            rejected_bookings_list.append({
                "booking_id": booking.id,
                "package_title": booking.package.title,
                "start_time": booking.start_time.strftime("%H:%M"),
                "end_time": booking.end_time.strftime("%H:%M"),
                "date": booking.date.strftime("%Y-%m-%d"),
                "status": booking.status ,
                "customer_email": booking.customer.email,
                "customer_mobile": booking.customer.customer_profile.mobile,
                "customer_name" : booking.customer.name
            })
        bookings = {"Accepted" : accepted_bookings_list , "Requested" : requested_bookings_list , "Rejected/Completed" : rejected_bookings_list}
        print("Requested")
        return bookings, 200

@app.route("/api/accept-booking/<int:booking_id>" , methods=["GET"])
@auth_required("token")
@roles_required("professional")
def accept_booking(booking_id):
    booking = db.session.query(Booking).filter_by(id=booking_id , prof_id=current_user.id).first()
    if booking:
        if booking.status == "Requested":
            booking.status = "Accepted"
            db.session.commit()
            return {"message": "Booking accepted successfully"}, 200
        else:
            return {"message": "Booking is not in Requested status"}, 400
    else:
        return {"message": "Booking not found"}, 404
    
@app.route("/api/reject-booking/<int:booking_id>" , methods=["GET"])
@auth_required("token")
@roles_required("professional")
def reject_booking(booking_id):
    booking = db.session.query(Booking).filter_by(id=booking_id , prof_id=current_user.id).first()
    if booking:
        if booking.status == "Requested":
            booking.status = "Rejected"
            db.session.commit()
            return {"message": "Booking rejected successfully"}, 200
        else:
            return {"message": "Booking is not in Requested status"}, 400
    else:
        return {"message": "Booking not found"}, 404


@app.route("/api/admin-search" , methods=["GET"])
@auth_required("token")
def admin_search():
    query_type = request.args.get("query_type")
    query=request.args.get("query")

    if query_type == "customer":

        custs = db.session.query(CustomerProfile).filter(or_(CustomerProfile.name.contains(query) ,CustomerProfile.email.contains(query  ))).all()
        custs_list= []
        for customer in custs: 
            custs_list.append(
                {
                "customer_id": customer.id,
                "Customer Name": customer.name,
                "Customer Email": customer.email,
                "Address": customer.address,
                "Mobile": customer.mobile,
                "Status" : customer.status
            }
            )
        return custs_list , 200
    
    elif query_type == "professional":

        profs = db.session.query(ProfessionalProfile).filter(or_(ProfessionalProfile.name.contains(query) ,ProfessionalProfile.email.contains(query  ))).all()
        profs_list= []
        for prof in profs: 
            profs_list.append(
                {
                "professional_id": prof.id,
                "Professional Name": prof.name,
                "Professional Email": prof.email,
                "Address": prof.address,
                "Mobile": prof.mobile,
                "Status" : prof.status
            }
            )
        return profs_list , 200
    else:
        return {"message": "Invalid query type"}, 400


from .task import add_together
@app.route("/starttask")
def task():
    a = 5 
    b = 6
    result = add_together.delay(a,b)
    return {"the_result" : result.id} 


from celery.result import AsyncResult


from .task import customer_csv
@app.route("/exportcustomercsv"  )
@auth_required("token")
def exportcustomercsv():
    if current_user.roles[0].name =="customer":
        result  = customer_csv.delay(current_user.id)
        return {"task_id" : result.id}
    else:
        return "you are not authorised to execute the task"
    



@app.get("/result")
def download_csv() :
    id = request.args.get("id")
    result = AsyncResult(id)
    if not result.ready() :
        return {"message" : "CSV generation is in progress.."} , 202
    return send_from_directory("static" , result.result) , 200
    