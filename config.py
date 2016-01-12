import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

LOG_FILE = 'debug.log'
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
