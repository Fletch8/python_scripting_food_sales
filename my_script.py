# Read only

def read_only():
    ''' only Reads the file  '''
    try:
        file1 = open('data.txt')
        text = file1.read()
        print(text)
        file1.close()
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    ''' writes to a file '''

    file2 = open('more_data.txt', 'w')
    file2.write('tomotoes')
    file2.close()

# with open('data.txt') as f:
#     text = f.read()
#     print(text)

def read_food_sales():
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            
            order_date = split_food_sale[0]

            all_dates.append(order_date)
    print(all_dates)

    with open('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')

def append_text():
    with open('dates.txt', 'a') as f:
        f.write('03/17/21')
        print('done')

if __name__ == '__main__':
    # read_only()
    # write_only()
    # read_food_sales()
    append_text()
