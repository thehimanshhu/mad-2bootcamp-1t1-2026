from flask import current_app as app
from flask import request,send_from_directory
from flask_security import  auth_required , roles_required , current_user, SQLAlchemyUserDatastore , hash_password
from flask_security.utils import verify_and_update_password 
from .models import db , User , Role , Package , Booking , CustomerProfile , ProfessionalProfile
from datetime import datetime
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

