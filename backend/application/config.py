

class LocalConfig:
    """Local configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "mysecretsalt"
    SECRET_KEY = "mysecretkey"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    CACHE_TYPE='redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0