
import pyodbc
import mysql.connector

def get_db():
    conn_str = (
        r'DRIVER={ODBC Driver 18 for SQL Server};'
        r'SERVER=tcp:p2ptrail.database.windows.net,1433;'
        r'DATABASE=p2p_trail;'
        r'UID=p2padmin;'
        r'PWD=Techworks@1234'
    )
    cnxn = pyodbc.connect(conn_str)
    return cnxn

def get_db2():
    conn_str = (
        r'DRIVER={ODBC Driver 18 for SQL Server};'
        r'SERVER=tcp:p2pdata.database.windows.net,1433;'
        r'DATABASE=p2p_data;'
        r'UID=p2padmin1;'
        r'PWD=techworks@1234'
    )
    cnxn = pyodbc.connect(conn_str)
    return cnxn

def get_db1():
    config = {
        'user': 'if0_36200926',
        'password': 'bSJ2pXZiaM',
        'host': 'sql110.infinityfree.com',
        'database': 'if0_36200926_p2pdata',
        'raise_on_warnings': True
    }

    cnxn = mysql.connector.connect(**config)
    return cnxn
get_db1()
