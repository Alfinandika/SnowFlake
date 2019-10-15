from app import app
from flaskext.mysql import MySQL

# Twitter configurations
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
 
# MySQL configurations
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'snowflake'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)