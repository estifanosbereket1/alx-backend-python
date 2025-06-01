import time
import sqlite3 
import functools

#### paste your with_db_decorator here

""" your code goes here"""

def retry_on_failure(retries, delay):

    def decorator (func):
        def wrapper(*args, **kwargs):
            retry_counnt=0
            while retries>retry_counnt:
                try:                
                    return_val= func(*args, **kwargs)
                    return return_val
                except sqlite3.Error as e:
                    retry_counnt+=1
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def with_db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")  
        try:
            return func(conn, *args, **kwargs) 
        finally:
            conn.close() 
    return wrapper

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)