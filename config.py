import secrets
class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mwashe:github2122@localhost/pitchlist'
    SECRET_KEY=secrets.token_urlsafe(16)


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG=True



config_options={
    "development":DevelopmentConfig,
    "production":ProductionConfig,
}