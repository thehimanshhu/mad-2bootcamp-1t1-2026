from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin , RoleMixin
db = SQLAlchemy()

class Role(db.Model, RoleMixin):
    __tablename__= "role"
    id = db.Column(db.Integer , primary_key = True , autoincrement= True)
    name= db.Column(db.String , unique =True , nullable=False)

class User(db.Model , UserMixin):
    __tablename__="user"
    id = db.Column(db.Integer , primary_key = True , autoincrement= True)
    name= db.Column(db.String  , nullable=False)
    email = db.Column(db.String , unique =True , nullable=False)
    password = db.Column(db.String , nullable=False)
    active = db.Column(db.Boolean , nullable=False)
    fs_uniquifier = db.Column(db.String , unique =True , nullable=False)
    roles=db.relationship("Role" , secondary="user_roles" , backref="users")

class UserRoles(db.Model):
    __tablename__="user_roles"
    id = db.Column(db.Integer , primary_key = True , autoincrement= True)
    user_id = db.Column(db.Integer , db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer , db.ForeignKey("role.id"))

class Package(db.Model):
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    title = db.Column(db.String, unique=True , nullable=False)
    price = db.Column(db.String , nullable=False)
    description= db.Column(db.String , nullable=False)
    prof_id = db.Column(db.Integer ,db.ForeignKey("user.id") , nullable=False )
    status = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date , nullable =False)
    end_date = db.Column(db.Date , nullable =False)
    bookings = db.relationship("Booking", backref="package", lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    title = db.Column(db.String, unique=True , nullable=False)
    total_price = db.Column(db.String , nullable=False)
    start_time = db.Column(db.Time , nullable =False)
    end_time = db.Column(db.Time , nullable =False) 
    date = db.Column(db.Date , nullable =False)
    status = db.Column(db.String, nullable=False)
    prof_id = db.Column(db.Integer ,db.ForeignKey("user.id") , nullable=False )
    pack_id =  db.Column(db.Integer ,db.ForeignKey("package.id") , nullable=False )
    cust_id = db.Column(db.Integer ,db.ForeignKey("user.id") , nullable=False)

class CustomerProfile(db.Model):
    id = db.Column(db.Integer, primary_key =True , autoincrement=True) 
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String )
    email = db.Column(db.String , unique=True , nullable=False)
    mobile =  db.Column(db.String)
    user_id = db.Column(db.Integer ,db.ForeignKey("user.id") , nullable=False )


class ProfessionalProfile(db.Model):
    id = db.Column(db.Integer, primary_key =True , autoincrement=True) 
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String )
    email = db.Column(db.String , unique=True , nullable=False)
    mobile =  db.Column(db.String)
    resume_url = db.Column(db.String, nullable = True)
    user_id = db.Column(db.Integer ,db.ForeignKey("user.id") , nullable=False )



