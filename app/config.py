import os

class Config:
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@admin-db:3306/local-python2023'
	SECRET_KEY = os.urandom(24)