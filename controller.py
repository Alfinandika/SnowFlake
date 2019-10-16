from config import mysql
from flask import jsonify
import pymysql
from app import app



app.app_context().push()
def datasets():
    
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT class, text as sentence FROM datasets")
		rows = cursor.fetchall()
		return rows
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

def insert(classN, text):
	try:
		sql = "INSERT INTO datasets(class, text) VALUES(%s, %s)"
		data = (classN, text)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('User added successfully!')
		resp.status_code = 200
		return resp

	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
