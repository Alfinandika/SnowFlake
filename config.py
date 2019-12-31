from app import app
from flaskext.mysql import MySQL

# Twitter configurations
ACCESS_TOKEN = "289784806-SAsXLwkRT5A7z0UyNpgtiuJZYltcgFkBU2myfIq2"
ACCESS_TOKEN_SECRET = "Xc5gGSbfemnpyAmGOsVMLVAwbvEDo523G8hWtYNilDf7w"
CONSUMER_KEY = "2vs609e7LjJ6l1tbvTjJsvaMr"
CONSUMER_SECRET = "dYBVdA393wDf5sGQ4bQmRlY9qpSEQ9KcveE5vezL6cawJ1bkl1"
 
# MySQL configurations
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'snowflake'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)