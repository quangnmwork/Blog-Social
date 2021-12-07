import os
basedir = os.path.abspath(os.path.dirname(__file__))


MAIL_USERNAME = os.environ.get('FLASKY_ADMIN')
print(MAIL_USERNAME)