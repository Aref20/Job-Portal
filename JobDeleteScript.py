import pyodbc 
from datetime import datetime
import time
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=JBDB;UID=sa;PWD=aaaa')
cursor = conn.cursor()


cursor.execute('UPDATE job_job SET status = ? WHERE  expiration_date <= CAST( GETDATE() AS Date )','INACTIVE')
conn.commit()




   



 





