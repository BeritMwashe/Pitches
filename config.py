class Config:
    pass



class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG=True



config_options={
    "development":DevelopmentConfig,
    "production":ProductionConfig,
}