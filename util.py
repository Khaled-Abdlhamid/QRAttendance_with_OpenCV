import pyodbc

def get_id(server= 'DESKTOP-H3TOI6A\SQLEXPRESS', database= 'access_db', table= 'access_table'):
    '''Connects to an SQL server and gets the id column for Access'''

    connection_path = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    conn = pyodbc.connect(connection_path)
    cursor = conn.cursor()

    id_query = "SELECT access_id FROM " + table
    cursor.execute(id_query)

    id_list = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return id_list


