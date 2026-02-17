from flask import current_app as app
from flask import request
from flask_security import verify_password , auth_required , roles_required
from .models import db , User , Role , Package , Booking , CustomerProfile , ProfessionalProfile
@app.route("/")
def home():
    return "Welcome to my application!"

@app.route("/login" , methods=["POST"])
def login():
    if request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")
        datastore = app.security.datastore  
        user = datastore.find_user(email=email)
        if user :
            if password ==user.password:
                return {"message":"Login successful" , "user": user.email , "token" : user.get_auth_token()}, 200
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
        user = datastore.create_user(name=name , email=email , password=password , roles=["customer"])
        db.session.commit()
        customer_profile = CustomerProfile(name=name , email=email , address=address , mobile=mobile , user_id=user.id)
        db.session.add(customer_profile)
        db.session.commit()
        return {"message":"Customer registered successfully"}, 201
    elif request.args.get("role") == "professional":
        name = request.json.get("name")
        email = request.json.get("email")
        password = request.json.get("password")
        address = request.json.get("address")
        mobile = request.json.get("mobile")
        resume_url = request.json.get("resume_url")
        datastore = app.security.datastore
        if datastore.find_user(email=email):
            return {"message":"email already exists"}, 400
        user = datastore.create_user(name=name , email=email , password=password , roles=["professional"])
        db.session.commit()
        professional_profile = ProfessionalProfile(name=name , email=email , address=address , mobile=mobile , resume_url=resume_url , user_id=user.id)
        db.session.add(professional_profile)
        db.session.commit()
        return {"message":"Professional registered successfully"}, 201

@app.route("/protected")
@auth_required("token")
@roles_required("admin")
def protected():
    return {"message":"This is a protected route"}, 200