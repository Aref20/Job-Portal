import pyodbc
server = 'localhost'
username = 'sa'
password = 'Aaaa@1234'
PORT = '1433'

cnxn = pyodbc.connect(
        'DRIVER=ODBC Driver 17 for SQL Server;SERVER=' +
        server + ';PORT=' + PORT + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

print ('Using the following SQL Server version:')
tsql = "SELECT @@version;"
with cursor.execute(tsql):
        row = cursor.fetchone()
        print (str(row[0]))
        

