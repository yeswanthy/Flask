#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/first-flast-app')

from app import app as application
