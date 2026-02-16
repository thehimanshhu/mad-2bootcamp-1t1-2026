from flask import current_app as app
from flask import request
from flask_security import verify_password , auth_required , roles_required
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


@app.route("/protected")
@auth_required("token")
@roles_required("admin")
def protected():
    return {"message":"This is a protected route"}, 200