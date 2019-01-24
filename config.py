
class BaseConfig:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/saavn"
    REDIS_HOST = "localhost"
    REDIS_PASSWORD = ""
    REDIS_PORT = 6379
    WTF_CSRF_ENABLED = True

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/saavn"

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/saavn"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/saavn"

class WorkerConfig:
    REDIS_URL = 'redis://localhost:6379/0'
    QUEUES = ['default']


PresentConfig = BaseConfig
