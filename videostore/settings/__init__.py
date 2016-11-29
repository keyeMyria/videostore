class Test:
    SQLALCHEMY_DATABASE_URI = "postgresql://videostore:videostore@localhost:5432/videostore_test"


class Development:
    SQLALCHEMY_DATABASE_URI = "postgresql://videostore:videostore@localhost:5432/videostore_dev"


class Production:
    SQLALCHEMY_DATABASE_URI = "postgresql://videostore:videostore@localhost:5432/videostore"


environments = {
    'test': Test,
    'development': Development,
    'production': Production,
}
    
