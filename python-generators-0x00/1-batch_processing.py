from seed import connect_to_prodev

def  stream_users_in_batches(batch_size):
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)

    try:
        while True:
            users=cursor.fetchmany(batch_size)
            if not users:
                break
            yield users
    finally:
        cursor.close()
        conn.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        yield [user for user in batch if user["age"] > 25]
