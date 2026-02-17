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
        datastore.create_user(name = "Admin" , email = "admin@email.com", password = "admin123" ,roles=["admin"])
    
    if not datastore.find_user(email = "customer@email.com"):
        datastore.create_user(name = "Customer" , email = "customer@email.com", password = "customer123" ,roles=["customer"])
    
    if not datastore.find_user(email = "professional@email.com"):
        datastore.create_user(name = "Professional" , email = "professional@email.com", password = "professional123" ,roles=["professional"])
    if db.session.query(Package).count() == 0:
        package1 = Package(title="Package 1", price="100", description="Description for Package 1", prof_id=1, status="available", start_date=datetime(2024,1,1), end_date=datetime(2024,12,31) )
        package2 = Package(title="Package 2", price="200", description="Description for Package 2", prof_id=1, status="available", start_date=datetime(2024,1,1), end_date=datetime(2024,12,31) )
        db.session.add(package1)
        db.session.add(package2)    
    db.session.commit()