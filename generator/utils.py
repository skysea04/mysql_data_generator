from typing import Tuple
import mysql.connector

db = mysql.connector.connect(
    host='db',
    user='root',
    # password='password',
    port='3306',
    database='test',
)

cursor = db.cursor()

def search_table() -> Tuple[list, bool]:
    cursor.execute('SHOW TABLES;')
    table_names = cursor.fetchall()
    tables = []
    for t_name in table_names:
        tables.append(t_name[0])

    if len(tables) == 0:
        print('ErrMsg: There is no any table')
        return None, False
    
    return tables, True


def select_table(tables: list) -> str:
    option_str = '\n'.join(
        f'{i} - {t}' for i, t in enumerate(tables, 1)
    )
    while True:
        index_str = input(f'Select the table you want to modify:\n{option_str}\nChoose from above: ')
        
        if index_str == '':
            continue
        
        try:
            index = int(index_str)
        except:
            print('\n***Please enter number***\n')
            continue
        
        if not (0 < index <= len(tables)):
            print('\n***Pleas enter valid number***\n')
            continue

        # This is table_name
        return tables[index-1]


def get_fields(table_name: str) -> list:
    fields = []
    cursor.execute(f'DESC {table_name}')
    fields_query = cursor.fetchall()
    for f in fields_query:
        if f[0] == 'id':
            continue
        fields.append(f[0])
    
    return fields