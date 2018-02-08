import psycopg2

DBName = 'news'


def db_connect(query):
    dbconn = psycopg2.connect(database=DBName)
    cursor = dbconn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    dbconn.close()
    return results
