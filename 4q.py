def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT
        COUNT(userid)
        FROM(
            SELECT
        dates, COUNT(userid)
        FROM
        relationship
        WHERE
        Typ = marriage
        GROUP
        BY
        userid
        HAVING
        COUNT(userid) > 2
        ORDER
        BY
        COUNT(userid)
        DESC)))")

        result = cur.fetchone()[0]
        print("Number of people who have more than one marriage:" + " " + str(result))
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
