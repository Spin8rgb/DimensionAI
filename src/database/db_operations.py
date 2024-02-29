import sqlite3

def create_connection(db_file):
    """Crea una connessione al database SQLite specificato dal db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connessione al database SQLite versione", sqlite3.version)
    except Exception as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Crea una tabella utilizzando la connessione 'conn' e la stringa SQL fornita"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def insert_data(conn, data):
    """
    Inserisce i dati nella tabella.
    'data' è una tupla che contiene i dati da inserire.
    """
    sql = ''' INSERT INTO my_table(name, value)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def query_data(conn, query):
    """Esegue una query SQL per leggere i dati."""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    database = "path/to/your_database.db"

    sql_create_my_table = """ CREATE TABLE IF NOT EXISTS my_table (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        value real
                                    ); """

    # Crea una connessione al database
    conn = create_connection(database)

    # Crea una tabella
    if conn is not None:
        create_table(conn, sql_create_my_table)
    else:
        print("Errore! impossibile creare la connessione al database.")

    # Inserimento di dati di esempio
    with conn:
        data = ("NomeEsempio", 123.45)
        insert_data(conn, data)

    # Query per leggere i dati
    query = "SELECT * FROM my_table"
    query_data(conn, query)

    # Ricorda di chiudere la connessione al database
    conn.close()
