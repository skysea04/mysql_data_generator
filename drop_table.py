import mysql.connector
from utils import cursor, search_table, select_table


def main():
    tables, ok = search_table()
    if not ok:
        return
    tables.append('All')
    table = select_table(tables)

    if table == 'All':
        tables.remove('All')
        for table in tables:
            drop_table(table)
    else:
        drop_table(table)
    


def drop_table(table):
    try:
        cursor.execute(f'DROP TABLE {table}')
        print(f'DROP TABLE `{table}` Successfully')
    except mysql.connector.Error as e:
        print(f'ErrMsg: {e}')


if __name__ == '__main__':
    main()
