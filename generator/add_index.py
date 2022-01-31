import mysql.connector

from utils import cursor, search_table, select_table, get_fields

def main():
    tables, ok = search_table()
    if not ok:
        return
    table = select_table(tables)
    fields = get_fields(table)
    
    fields_len = len(fields)
    fields_str = ', '.join(fields)
    index_fields = []

    # Choose field number in this index
    while True:
        index_fields_num_str = input(f'\nTable `{table}` has these fields: [{fields_str}]\nField count: {fields_len}\nChoose how many fields you want to add in the index (1 ~ {fields_len}), default[1]: ')

        if index_fields_num_str == '':
            index_fields_num = 1
        else:
            try:
                index_fields_num = int(index_fields_num_str)
            except:
                print(f'\n***Please enter number(1 ~ {fields_len})***')
                continue
        
        if not (0 < index_fields_num <= fields_len):
            print(f'\n***Please enter valid number(1 ~ {fields_len})***')
            continue
        break
    
    # Choose each field by order
    for order in range(1, index_fields_num+1):
        while True:
            fields_str_per_line = '\n'.join(
                f'{i} - {t}' for i, t in enumerate(fields, 1)
            )
            index_field_str = input(f'\nTable `{table}` remain these fields:\n{fields_str_per_line}\nChoose the index\'s {get_order_str(order)} column: ')
            try:
                index_field_idx = int(index_field_str)
            except:
                print(f'\n***Please enter number(1 ~ {fields_len})***')
                continue
        
            if not (0 < index_field_idx <= fields_len):
                print(f'\n***Please enter valid number(1 ~ {fields_len})***')
                continue
            
            index_fields.append(fields[index_field_idx-1])
            fields.remove(fields[index_field_idx-1])
            fields_len = len(fields)
            print(f'Index fields: {index_fields}')

            break

    index_name = input('Enter the index\'s name: ')
    index_fields_str = ', '.join(index_fields)

    try:
        cursor.execute(f'ALTER TABLE {table} ADD INDEX {index_name}({index_fields_str})')
        print(f'Add Index {index_name} Successfully')
    except mysql.connector.Error as e:
        print('ErrMsg: ', e)


def get_order_str(i: int) -> str:
    if i == 1:
        return '1st'
    elif i == 2:
        return '2nd'
    elif i == 3:
        return '3rd'
    else:
        return f'{i}th'


if __name__ == '__main__':
    main()