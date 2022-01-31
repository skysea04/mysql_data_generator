import mysql.connector
from  mysql.connector import errorcode

from utils import cursor
from models import tables


for table_name, table_desc in tables.items():
    try:
        cursor.execute(table_desc)
        print(f'Create Table `{table_name}` Successfully')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f'ErrMsg: Table `{table_name}` Already exists')
        else:
            print(f'ErrMsg: {err.msg}')


cursor.close()
