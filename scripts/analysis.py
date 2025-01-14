import sqlite3
import pandas as pd

conn = sqlite3.connect("financial_data.db")

df_operations = pd.read_sql_query("SELECT * FROM statements_of_operations;", conn)
df_balance = pd.read_sql_query("SELECT * FROM balance_sheets;", conn)

# Crecimiento de sales
df_operations['growth'] = df_operations['total_net_sales'].pct_change() * 100

# Margen neto
df_operations['net_margin'] = df_operations['net_income'] / df_operations['total_net_sales'] * 100

# Cambio en assets
df_balance['assets_change'] = df_balance['total_assets'].pct_change() * 100

# Cambio en liabilities
df_balance['liabilities_change'] = df_balance['total_liabilities'].pct_change() * 100

df_operations[['fiscal_year', 'total_net_sales', 'growth', 'net_margin']].to_parquet('gold/growth_net_margin.parquet')
df_balance[['fiscal_year', 'total_assets', 'assets_change', 'total_liabilities', 'liabilities_change']].to_parquet('gold/assets_liabilities_change.parquet')

# Cerrar la conexion
conn.close()
