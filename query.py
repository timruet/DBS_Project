import psycopg2

def get_oldest():
	conn = None
	try:
		conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

		cur = conn.cursor()

		cur.execute("SELECT MAX(age) FROM mfb_user")

		result1 = cur.fetchone()[0]

		cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return result1
			
			
def get_user_with_most_dates():
	conn = None
	result2 = None
	try:
		conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

		cur = conn.cursor()

		cur.execute("SELECT DISTINCT id FROM (SELECT id ,COUNT(id) FROM dates GROUP BY id ORDER BY COUNT(id) DESC LIMIT 1) as a")

		result2 = cur.fetchone()[0]
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return result2
			
			
def get_user_with_highest_income():
	conn = None
	result3 = None
	try:
		conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

		cur = conn.cursor()

		cur.execute("SELECT DISTINCT id FROM (SELECT id, COUNT(income) FROM mfb_user GROUP BY id ORDER BY COUNT(income) DESC LIMIT 1) as a")

		result3 = cur.fetchone()[0]
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return result3
			
			
def get_number_of_users_with_more_than_two_marriages():
	conn = None
	result4 = None
	try:
		conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

		cur = conn.cursor()

		cur.execute("SELECT COUNT(id) FROM(SELECT id, COUNT(id) FROM dates GROUP BY id HAVING COUNT(id) >= 2 ORDER BY COUNT(id) DESC) as a")

		result4 = cur.fetchone()[0]
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return result4
			
			
			
def get_user_with_most_fans():
	conn = None
	result5 = None
	try:
		conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

		cur = conn.cursor()

		cur.execute("SELECT DISTINCT id FROM(SELECT id, COUNT(id) FROM is_fan GROUP BY id ORDER BY COUNT(id) DESC LIMIT 1) as a")

		result5 = cur.fetchone()[0]
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return result5
			
			
			
def get_number_of_users_without_fans_or_relationship():
	conn = None
	result6 = None
	try:
		conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345")

		cur = conn.cursor()

		cur.execute("SELECT DISTINCT COUNT(id) FROM mfb_user EXCEPT SELECT id FROM is_fan NATURAL JOIN dates NATURAL JOIN marriage")

		result6 = cur.fetchone()[0]
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return result6


print (get_oldest())
print(get_user_with_most_dates())
print(get_user_with_highest_income())
print(get_number_of_users_with_more_than_two_marriages())
print(get_user_with_most_fans())
print(get_number_of_users_without_fans_or_relationship())
