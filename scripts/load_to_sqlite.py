import sqlite3
import pandas as pd
import os

# Conectar a SQLite
def connect_db(db_name="financial_data.db"):
    conn = sqlite3.connect(db_name)
    return conn

# Crear tablas en la base de datos
def create_tables(conn):
    cursor = conn.cursor()

    # Crear tabla para "CONSOLIDATED STATEMENTS OF OPERATIONS"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS statements_of_operations (
            fiscal_year INTEGER,
            total_net_sales INTEGER,
            total_cost_of_sales INTEGER,
            total_operating_expenses INTEGER,
            net_income INTEGER,
            PRIMARY KEY (fiscal_year)
        );
    ''')

    # Crear tabla para "CONSOLIDATED BALANCE SHEETS"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balance_sheets (
            fiscal_year INTEGER,
            total_current_assets INTEGER,
            total_assets INTEGER,
            total_current_liabilities INTEGER,
            total_liabilities INTEGER,
            total_liabilities_and_shareholders_equity INTEGER,
            PRIMARY KEY (fiscal_year)
        );
    ''')

    # Crear tabla para "CONSOLIDATED STATEMENTS OF CASH FLOWS"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS statements_of_cash_flows (
            fiscal_year INTEGER,
            net_income INTEGER,
            cash_generated_by_operating_activities INTEGER,
            cash_used_in_financing_activities INTEGER,
            PRIMARY KEY (fiscal_year)
        );
    ''')

    conn.commit()

# Insertar datos en la tabla
def insert_data(conn, table_name, data):
    cursor = conn.cursor()
    temp = ', '.join(['?'] * len(data))
    query = f"INSERT OR IGNORE INTO {table_name} VALUES ({temp});"
    cursor.execute(query, tuple(data))
    conn.commit()

# Cargar el dataframe desde parquet a SQLite
def load_dataframe_to_db(conn, df, table_name):
    for _, row in df.iterrows():
        data = row.tolist()
        insert_data(conn, table_name, data)

parquet_dir = "silver"

# Conexion a SQLite
conn = connect_db()

# Crear tablas en la base de datos
create_tables(conn)

# Cargar los archivos parquet para cada seccion
sections = ["statements_of_operations", "balance_sheets", "statements_of_cash_flows"]
for section in sections:
    # Path del archivo parquet correspondiente
    parquet_file = os.path.join(parquet_dir, f"{section}.parquet")

    if os.path.exists(parquet_file):
        # Leer el archivo parquet
        df = pd.read_parquet(parquet_file)

        # Cargar el dataframe en la tabla correspondiente
        load_dataframe_to_db(conn, df, section)

# Cerrar la conexion a la base de datos
conn.close()
