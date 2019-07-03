import psycopg2

def connect1():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT MAX(age) FROM mfb_user")

        result = cur.fetchone()[0]
        print("Age of the oldest person:" + " " + str(result))
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
            
def connect2():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT DISTINCT id, screenname, name
    FROM (SELECT id ,COUNT(id)
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
            
            
def connect3():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT DISTINCT id, screenname, name
	FROM (SELECT id, screenname, name, COUNT(Einkommen)
	FROM mfb_user
	GROUP BY id
	ORDER BY COUNT(Einkommen) DESC
	LIMIT 1)")

        result = cur.fetchone()[0]
        print("Person with the highest income:" + " " + str(result))
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
            
def connect4():
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
            
            
            
def connect5():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT
        DISTINCT
        id
        FROM(
            SELECT
        id, COUNT(userid)
        FROM
        isfanof
        GROUP
        BY
        userid
        ORDER
        BY
        COUNT(userid)
        DESC
        LIMIT
        1))")

        result = cur.fetchone()[0]
        print("Person with the highest number of fans:" + " " + str(result))
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
            
            
def connect6():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT
        DISTINCT
        id, screenname, name
        FROM
        mfb_ser
        EXCEPT
        SELECT
        id
        FROM
        isfanof
        NATURAL
        JOIN
        relationship)")

        result = cur.fetchone()[0]
        print("Number of users who have no fans and no romantic relationship:" + " " + str(result))
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
