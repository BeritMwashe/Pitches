class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mwashe:github2122@localhost/pitchlist'



class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG=True



config_options={
    "development":DevelopmentConfig,
    "production":ProductionConfig,
}