import pandas as pd
from sqlalchemy import create_engine,text



student = pd.read_csv("artifacts/data.csv")


# Credentials to connect to Database
user = 'root'  # user name
pw = 'newpassword123'  # password
db = 'student_db'  # database name
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")

# to_sql() - function to push the dataframe onto a SQL 
student.to_sql('student_raw', con = engine, if_exists = 'replace', chunksize = 1000, index = False)




###### To read the data from MySQL Database
sql = 'select * from student_raw;'
student= pd.read_sql_query(text(sql), engine.connect())


