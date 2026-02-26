from flask import Flask
from application.models  import db , User , Role
from flask_security import Security  , SQLAlchemyUserDatastore
from application.config import LocalConfig
from flask_cors import CORS
from application.celery_init import celery_init_app
def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalConfig)
    db.init_app(app)
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app , datastore , register_blueprint=False)
    CORS(app)
    @app.security.unauthn_handler
    def unauthn_handler( mechanisms , headers  ):
        print("the mechanisms are:", mechanisms)
        print("the headers are:", headers)
        return {"message":"Auth Required"}, 401
    @app.security.unauthz_handler
    def unauthz_handler(func_name , params):
        print("the func_name is:", func_name)
        print("the params are:", params)
        return {"message":"you are not allowed to view this route"}, 403

    app.app_context().push()
    return app


app = create_app()
celery = celery_init_app(app)

from application.initial_data import *
from application.routes import *
if __name__ == "__main__":
    app.run(debug=True)