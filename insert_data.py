from typing import Tuple
from utils import db, cursor, search_table, select_table, get_fields


def main():
    tables, ok = search_table()
    if not ok:
        return
    table = select_table(tables)
    fields = get_fields(table)

    fields_str = ', '.join(fields)
    values_str = ', '.join(['%s' for _ in fields])
    fields_cnt = len(fields)
    min_n = 1
    max_n = min_n + 10000

    # Choose data number to insert
    while True:
        insert_num_str = input('How many data you want to insert\nUnit: 10000 (ex. enter 1 ->  insert 10000)\nChoose number: ')
        
        if insert_num_str == '':
            print('\n**Please enter a number**\n')
            continue
        try:
            insert_num = int(insert_num_str)
        except:
            print('\n**Please enter a number**\n')
            continue

        if insert_num < 0:
            print('\n**Please enter a positive number**\n')
            continue

        break

    for _ in range(insert_num):
        insert_table(min_n, max_n, table, fields_str, values_str, fields_cnt)
        min_n += 10000
        max_n += 10000
    

def insert_table(min_n: int, max_n: int, table: str, fields_str: str, values_str: str, fields_cnt: int):
    sql = f'INSERT INTO {table} ({fields_str}) VALUES ({values_str})'
    val = [create_tuple(fields_cnt, i) for i in range(min_n, max_n)]
    
    cursor.executemany(sql, val)
    db.commit()

    print(f'Insert Data To Table `{table}` id {min_n} ~ {max_n-1}')


def create_tuple(num, i) -> Tuple:
    return tuple([(i*n if n%2!= 0 else i%(n*1000)) for n in range(1, num+1)]) 


if __name__ == '__main__':
    main()