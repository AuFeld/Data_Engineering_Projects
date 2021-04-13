import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Etablishes database connection and returns the connection and cursor
    references. 
    :return: returns (cur, conn) a cursor and connection reference
    """

    # connect to default database
    # conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=admin")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=admin")
    cur = conn.cursor()

    return cur, conn

def drop_tables(cur, conn):
    """
    Runs all the drop table queries in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """
    Runs all the cerate table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Driver main function
    """
    cur, conn = create_database()

    drop_tables(cur, conn) 
    print("Table dropped successfully!")

    create_tables(cur, conn)
    print("Table created succuessfully!")

    conn.close()


if __name__ == "__main__":
    main()