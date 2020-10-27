import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    # Flask Settings
    APP_NAME = "u-matter rest service"
    APP_PORT = 5000
    APP_HOST = "127.0.0.1"
    DEBUG = True

    DB_TYPE = "postgresql" # postgresql vs mysql

    # Mysql Settings 
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = ""
    MYSQL_PORT = 3306

    # PostgreSQL Settings
    PSQL_HOST = "localhost"
    PSQL_USER = "mmuser"
    PSQL_PASSWORD = "123456"
    PSQL_DB = "mattermost"
    PSQL_PORT = 5432

    # Mattermost settings
    DAILY_POINT_LIMIT = 10
    PER_TRANSACTION_POINT_LIMIT = 5
    WEEKLY_THRESHOLD = 40
    MM_SCHEME = "http"
    MM_URL = "localhost"
    MM_PORT = 8065
    MM_BOT_TOKEN = ""
    MM_SLASH_TOKEN = ""
    MM_SLASH_NAME = "/umatter"


    # LOG FILE PATH
    LOG_FILE_PATH = "event_logs.log"

class ProductionConfig(BaseConfig):
    """
    Production configurations
    """
    APP_PORT = 5000
    APP_HOST = "127.0.0.1"
    DEBUG = False

    DB_TYPE = "postgresql" # postgresql vs mysql

    MYSQL_HOST = "db"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DB = "umatter"
    MYSQL_PORT = 3306

    # PostgreSQL Settings
    PSQL_HOST = "localhost"
    PSQL_USER = "mmuser"
    PSQL_PASSWORD = "123456"
    PSQL_DB = "mattermost"
    PSQL_PORT = 5432
    
    MM_SCHEME = "http"
    MM_URL = "127.0.0.1"
    MM_PORT = 8065
    MM_BOT_TOKEN = "gxor34guo7nfppe6dxbatwfzoh"
    MM_SLASH_TOKEN = "xr9yxqr54ifsfxpxp66eynp7ty"
    WEEKLY_THRESHOLD = 40

class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """
    APP_PORT = 5000
    DEBUG = True

    DB_TYPE = "postgresql" # postgresql vs mysql

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DB = "umatter"
    MYSQL_PORT = 3306

    # PostgreSQL Settings
    PSQL_HOST = "localhost"
    PSQL_USER = "mmuser"
    PSQL_PASSWORD = "123456"
    PSQL_DB = "mattermost"
    PSQL_PORT = 5432

    MM_SCHEME = "http"
    MM_URL = "localhost"
    MM_PORT = 8065
    MM_BOT_TOKEN = "gxor34guo7nfppe6dxbatwfzoh"
    MM_SLASH_TOKEN = "t5m9n8zq4jrstfc9k5tjbp66qc"
    WEEKLY_THRESHOLD = 5

class TestingConfig(BaseConfig):
    """
    Testing configurations
    """


app_config = {  
    'default': ProductionConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}