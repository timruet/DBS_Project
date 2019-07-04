import psycopg2



DATABASE = "postgres"
USER     = "postgres"
PASSWORD = "postgres"

def get_user_data_based_on_user_id(user_id):
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database=DATABASE, user=USER, password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"SELECT id, screenname, name, age, income "
                    f"FROM facebook_user "
                    f"where id = {user_id}")

        result = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result


def get_user_data_based_on_user_name(user_name):
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database=DATABASE, user=USER, password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"SELECT id, screenname, name, age, income "
                    f"FROM facebook_user "
                    f"where name = {user_name}")

        result = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result

def get_number_of_records():
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database=DATABASE, user=USER, password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"SELECT COUNT(id) FROM facebook_user")

        result = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result


def get_user_fans_by_user_id(user_id):
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database=DATABASE, user=USER, password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"SELECT DISTINCT facebook_user.screenname "
                    f"FROM facebook_user "
                    f"INNER JOIN is_fan_of "
                    f"ON facebook_user.id = is_fan_of.fanid "
                    f"WHERE is_fan_of.idolid = {user_id}")

        result = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result

def get_who_user_dates_by_user_id(user_id):
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database=DATABASE, user=USER, password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"SELECT DISTINCT facebook_user.screenname "
                    f"FROM facebook_user "
                    f"INNER JOIN dates ON facebook_user.id = dates.userid_2 "
                    f"WHERE dates.userid_1 = {user_id}")

        result = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result




def get_who_user_marries_by_user_id(user_id):
    conn = None
    result = None

    try:
        conn = psycopg2.connect(host="localhost", database=DATABASE, user=USER, password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"SELECT DISTINCT facebook_user.screenname "
                    f"FROM facebook_user "
                    f"INNER JOIN is_married_to imt on facebook_user.id = imt.userid_2 "
                    f"WHERE imt.userid_1 = {user_id}")

        result = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result



if __name__ == "__main__":
    print(get_who_user_dates_by_user_id(1031571313352224768))