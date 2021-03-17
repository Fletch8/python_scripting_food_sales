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

# 2. Put all of the region inside of a region.txt (Region)
# 3. Put all of the city inside of a city.txt (City)
# 4. Put all of the category inside of a category.txt

def write_regions():
    all_regions = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            region = split_food_sale[1]
            all_regions.append(region)

    with open('regions.txt', 'w') as f:
        for region in all_regions:
            f.write(region)
            f.write('\n')

def write_city():
    all_cities = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            city = split_food_sale[2]
            all_cities.append(city)

    with open('cities.txt', 'w') as f:
        for city in all_cities:
            f.write(city)
            f.write('\n')

def write_catagory():
    all_catagories = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            catagory = split_food_sale[3]
            all_catagories.append(catagory)

    with open('catagory.txt', 'w') as f:
        for catagory in all_catagories:
            f.write(catagory)
            f.write('\n')



if __name__ == '__main__':
    # read_only()
    # write_only()
    # read_food_sales()
    # append_text()
    # write_regions()
    # write_city()
    write_catagory()