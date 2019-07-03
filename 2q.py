def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT DISTINCT id
    FROM (SELECT id, COUNT(id)
    FROM relationship
    WHERE Typ=marriage
    GROUP BY userid
    ORDER BY COUNT(userid) DESC
    LIMIT 1)")

        result = cur.fetchone()[0]
        print("Person with the highest number of dates:" + " " + str(result))
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
