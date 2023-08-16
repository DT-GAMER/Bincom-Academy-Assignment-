import psycopg2

# Database connection parameters
db_params = {
    "dbname": "BabynamesDB",
    "user": "Dominion",
    "password": "xdgureefhjikgdsdhhjgg",
    "host": "localhost",  
    "port": "5432",       
}

def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS baby_names (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT,
        year INT
    )
    """
    cursor.execute(create_table_query)

def insert_name(cursor, name, gender, year):
    insert_query = "INSERT INTO baby_names (name, gender, year) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, gender, year))

def retrieve_names(cursor):
    retrieve_query = "SELECT * FROM baby_names"
    cursor.execute(retrieve_query)
    return cursor.fetchall()

def update_name(cursor, name, new_gender, new_year):
    update_query = "UPDATE baby_names SET gender = %s, year = %s WHERE name = %s"
    cursor.execute(update_query, (new_gender, new_year, name))

def delete_name(cursor, name):
    delete_query = "DELETE FROM baby_names WHERE name = %s"
    cursor.execute(delete_query, (name,))


def main():
    try:
        # Establish database connection
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Create the table
        create_table(cursor)
        conn.commit()

        # Insert names
        insert_name(cursor, "Josephine", "Female", 2000)
        insert_name(cursor, "Dominic", "Male", 2002)
        conn.commit()

        # Retrieve and display names
        names = retrieve_names(cursor)
        for name in names:
            print(name)

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()

