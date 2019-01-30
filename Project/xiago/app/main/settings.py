
def get_db_uri(db_dict):
    host = db_dict.get("HOST", 'localhost')
    port = db_dict.get("PORT", 3306)
    user = db_dict.get("USER", 'root')
    password = db_dict.get("PASSWORD", '123456')
    dbname = db_dict.get("DBNAME", 'xiago')
    dbtype = db_dict.get("DBTYPE", 'mysql')
    driver = db_dict.get("DRIVER", 'pymysql')
    return '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(dbtype,driver,user,password,host,port,dbname)

class Config:
    DEBUG = False
    Testting = False
    SECRET_KEY = '123456'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Develop(Config):
    DEBUG = True

    database = {
        'HOST':'localhost',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'123456',
        'DBNAME':'project',
        'DBTYPE':'mysql',
        'DRIVER':'pymysql',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(database)


class Testing(Config):
    Testting = True

    database = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'DBNAME': 'mydb',
        'DBTYPE': 'mysql',
        'DRIVER': 'pymysql',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(database)

class Staging(Config):

    database = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'DBNAME': 'mydb',
        'DBTYPE': 'mysql',
        'DRIVER': 'pymysql',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(database)

class Production(Config):

    database = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'DBNAME': 'mydb',
        'DBTYPE': 'mysql',
        'DRIVER': 'pymysql',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(database)


config = {
    "develop":Develop,
    "test":Testing,
    'stage':Staging,
    'production':Production,
    'default':Develop,
}
