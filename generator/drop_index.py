import mysql.connector
from collections import defaultdict
from utils import cursor, search_table, select_table

def main():
    tables, ok = search_table()
    if not ok:
        return
    table = select_table(tables)
    
    # Search indexes
    idxes = defaultdict(list)
    cursor.execute(f'SHOW INDEXES IN {table}')
    idx_queries = cursor.fetchall()
    for q in idx_queries:
        idx_name = q[2]
        col_name = q[4]
        if idx_name == 'PRIMARY':
            continue

        idxes[idx_name].append(col_name)
        
    idx_lst = [(k, v) for k, v in idxes.items()]
    option_tail_num = len(idxes) + 1

    if not idx_lst:
        print(f'Table `{table}` has no index')
        return

    # Choose index to drop
    while True:
        idx_per_line = '\n'.join(
            f'{i} - index: {key_value[0]}, columns: {key_value[1]}' for i, key_value in enumerate(idx_lst, 1)
        ) + f'\n{option_tail_num} - All Index (Dangerous)'
        idx_num_str = input(f'\nTable `{table}` has these indexes:\n{idx_per_line}\nChoose index you want to drop: ')
        try:
            idx_num = int(idx_num_str)
        except:
            print(f'\n***Please enter number(1 ~ {option_tail_num})***')
            continue
        
        if not (0 < idx_num <= option_tail_num):
            print(f'\n***Please enter valid number(1 ~ {option_tail_num})***')
            continue
        
        # Choose all index
        if idx_num == option_tail_num:
            for idx_info in idx_lst:
                drop_index(table, idx_info[0])
            return
        
        drop_index(table, idx_lst[idx_num-1][0])
        return


def drop_index(table, index):
    try:
        cursor.execute(f'ALTER TABLE {table} DROP INDEX {index}')
        print(f'Drop Index {index} Successfully')
    except mysql.connector.Error as e:
        print(f'ErrMsg: {e}')


if __name__ == "__main__":
    main()