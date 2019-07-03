import psycopg2

def get_oldest():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

        cur = conn.cursor()

        cur.execute("SELECT MAX(age) FROM mfb_user")

        result = cur.fetchone()[0]
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
            
            
def get_person_with_most_dates():
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
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
            
            
def get_user_with_highest_income():
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
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
            
            
def get_number_of_users_with_more_than_two_marriages():
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
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
            
            
            
def get_user_with_most_fans():
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
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
            
            
            
def get_number_of_users_without_fans_or_relationship():
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
    cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
	return result
