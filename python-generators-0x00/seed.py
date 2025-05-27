import csv
from mysql.connector import  connect, MySQLConnection , Error


def connect_db():
    conn=  connect(host="localhost", user="root", password="7943")
    if conn.is_connected():
        return  conn
    else:
        raise Error("Couldnt connect")

def create_database(connecton:MySQLConnection):
    cursor =None
    try:
        cursor= connecton.cursor()
        cursor.execute('''
        CREATE DATABASE IF NOT EXISTS ALX_prodev;
        ''')
    finally:
        if cursor !=None:
            cursor.close()


def connect_to_prodev()->MySQLConnection:
    conn= None
    try:
        conn = connect(host="localhost", user="root", password="7943", database="ALX_prodev")
        return conn
    except Error as e:
        if conn !=None:
            conn.close()


def create_table(connection:MySQLConnection):
    cursor =None
    try:
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS user_data (
                                  user_id VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
                                  name  VARCHAR(255) NOT NULL,
                                  email VARCHAR(255) NOT NULL,
                                  age DECIMAL(5,2) NOT NULL
                               );'''
        )
    finally:
        if cursor !=None:
            cursor.close()

def insert_data(connection:MySQLConnection , data):
    cursor =None
    try:
        cursor =connection.cursor()
        if data:
            with open(data, mode="r", encoding="utf-8") as file:
                reader= csv.DictReader(file)
                for row in reader:
                    cursor.execute('''
                    INSERT INTO user_data (name , email, age)
                    VALUES(%s, %s, %s)
                    ''',
                        (row["name"], row["email"], row["age"]))
                connection.commit()
    finally:
        if cursor!=None:
            cursor.close()


