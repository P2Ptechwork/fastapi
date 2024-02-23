
import pyodbc

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
def get_db1():
    conn_str = (
        r'DRIVER={ODBC Driver 18 for SQL Server};'
        r'SERVER=tcp:p2pdata.database.windows.net,1433;'
        r'DATABASE=p2p_data;'
        r'UID=p2padmin1;'
        r'PWD=techworks@1234'
    )
    cnxn = pyodbc.connect(conn_str)
    return cnxn