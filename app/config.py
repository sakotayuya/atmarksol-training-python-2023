import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/python2023'
  SECRET_KEY = os.urandom(24)