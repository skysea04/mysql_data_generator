import mysql.connector

from utils import cursor, search_table, select_table

def main():
    tables, ok = search_table()
    if not ok:
        return
    table = select_table(tables)
    turncate(table)


def turncate(table):
    try:
        cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
        cursor.execute(f'TRUNCATE TABLE {table}')
        cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
        print(f'Truncate Table `{table}` Successfully')
    except mysql.connector.Error as err:
        print(f'ErrMsg: {err.msg}')


if __name__ == '__main__':
    main()