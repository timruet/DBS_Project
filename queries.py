import psycopg2

def connect():
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="dbs", user="postgres", password="postgres")

        cur = conn.cursor()

        #1
	cur.execute(SELECT MAX(Age) FROM User)

        result = cur.fetchone()
        print("Age of the oldest person:" + " " + result)

        
	#2
	cur.execute(
		SELECT DISTINCT userid 
		FROM (
			SELECT userid, COUNT(userid)
        		FROM relationship
			WHERE Typ=dates
			GROUP BY userid
			ORDER BY COUNT(userid) DESC
			LIMIT 1))

        result = cur.fetchone()
        print("ID of the person with the highest number dates:" + " " + result)

	#3
        cur.execute(
		SELECT DISTINCT userid 
        	FROM (
			SELECT userid,COUNT(Einkommen)
        		FROM User
			GROUP BY userid
			ORDER BY COUNT(Einkommen) DESC
			LIMIT 1)


        result = cur.fetchone()
        print("ID of the person with the highest income:" + " " + result)


	#4
        cur.execute(
		SELECT COUNT(userid)
		FROM (
			SELECT dates, COUNT(userid) 
			FROM relationship
			WHERE Typ=marriage
			GROUP BY userid
			HAVING COUNT(userid)>2
			ORDER BY COUNT(userid) DESC)))


        result = cur.fetchone()
        print("Number of people who have more than one marriage:" + " " + result)


	#5
        cur.execute(
		SELECT DISTINCT userid
		FROM (
			SELECT userid,COUNT(userid)
			FROM isfanof 
			GROUP BY userid
			ORDER BY COUNT(userid) DESC
			LIMIT 1))


        result = cur.fetchone()
        print("ID of the person with the highest number of fans:" + " " + result)

		    
	#6
        cur.execute(
		SELECT DISTINCT userid 
		FROM User
		EXCEPT
		SELECT userid FROM isfanof NATURAL JOIN relationship)



        result = cur.fetchone()
        print("Number of users who have no fans and no romantic relationship:" + " " + result)


        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
