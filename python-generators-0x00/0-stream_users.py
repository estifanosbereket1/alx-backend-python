from sympy.codegen import While

from seed import  connect_db, connect_to_prodev

def stream_users():
    connection= connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    try:
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            else:
                yield row
    finally:
        cursor.close()
        connection.close()
