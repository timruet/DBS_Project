import psycopg2

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT MAX(age) FROM mfb_user")

        result = cur.fetchone()[0]
        return result
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
