from app import app
from flaskext.mysql import MySQL

# Twitter configurations
ACCESS_TOKEN = "289784806-oMOXkCEy2YS79TmtWYn8gYim2rprjD5FY2n2GPL0"
ACCESS_TOKEN_SECRET = "6oqPSLtlC2ZAQWq9p9cuV53yP1mFL8NoTEAjyoZjVWTs1"
CONSUMER_KEY = "8XG3Iu5OfQ9NeQS4rJDxD9bfh"
CONSUMER_SECRET = "kc677CoU5jxapDK5cbldPVLDchkhyPTCDGKPsl1VlDz5PtXXxF"
 
# MySQL configurations
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'snowflake'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)