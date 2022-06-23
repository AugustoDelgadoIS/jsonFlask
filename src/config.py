from distutils.debug import DEBUG


class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Atticus182@'
    MYSQL_DB = 'api_flask'


config = {
    'development' : DevelopmentConfig
}