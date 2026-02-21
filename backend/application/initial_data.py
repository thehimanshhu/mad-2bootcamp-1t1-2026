from flask import current_app as app
from .models import db , Package 
from flask_security import SQLAlchemyUserDatastore, hash_password
from datetime import datetime
with app.app_context():
    db.create_all()
    datastore:SQLAlchemyUserDatastore = app.security.datastore
    datastore.find_or_create_role(name="admin")
    datastore.find_or_create_role(name="customer")
    datastore.find_or_create_role(name="professional")
    if not datastore.find_user(email = "admin@email.com"):
        datastore.create_user(name = "Admin" , email = "admin@email.com", password = hash_password("admin123") ,roles=["admin"])
     
    db.session.commit()