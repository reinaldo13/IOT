import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="QTI4dm1N",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from auth_group"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    auth_group = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in auth_group:
        print("Id = ", row[0])
        print("name = ", row[1])


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")