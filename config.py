import os
import secrets
class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mwashe:github2122@localhost/pitchlist'
    SECRET_KEY=secrets.token_urlsafe(16)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'mwasheberit@gmail.com'
    MAIL_PASSWORD = 'github2122'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG=True



config_options={
    "development":DevelopmentConfig,
    "production":ProductionConfig,
}