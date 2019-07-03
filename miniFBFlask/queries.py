import psycopg2


def get_oldest():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")

        cur = conn.cursor()

        cur.execute("SELECT MAX(age) FROM facebook_user")

        result = cur.fetchone()[0]
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    return result


def get_user_data_based_on_user_id(user_id):
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")

        cur = conn.cursor()

        cur.execute(f"SELECT id, screenname, name FROM facebook_user where id = {user_id}")

        result = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result



print(get_user_data_based_on_user_id(483674751))
