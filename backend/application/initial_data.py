from flask import current_app as app
from .models import db 
from flask_security import SQLAlchemyUserDatastore, hash_password

with app.app_context():
    db.create_all()
    datastore:SQLAlchemyUserDatastore = app.security.datastore
    datastore.find_or_create_role(name="admin")
    datastore.find_or_create_role(name="customer")
    datastore.find_or_create_role(name="professional")
    if not datastore.find_user(email = "admin@email.com"):
        datastore.create_user(name = "Admin" , email = "admin@email.com", password = "admin123" ,roles=["admin"])
    
    if not datastore.find_user(email = "customer@email.com"):
        datastore.create_user(name = "Customer" , email = "customer@email.com", password = "customer123" ,roles=["customer"])
    
    if not datastore.find_user(email = "professional@email.com"):
        datastore.create_user(name = "Professional" , email = "professional@email.com", password = "professional123" ,roles=["professional"])
    db.session.commit()