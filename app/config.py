import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'FFFFFFFF0X'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:adsl1234@db:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True