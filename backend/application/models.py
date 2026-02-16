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

