import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""

def cache_query(func):

    def wrapper(*args, **kwargs):
        query=kwargs["query"]
        if query in query_cache:
            return query_cache[query]
        return_val =func(*args, **kwargs)
        query_cache[query]=return_val
        return return_val
    return wrapper

def with_db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")  
        try:
            return func(conn, *args, **kwargs) 
        finally:
            conn.close() 
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")