import psycopg2

try:
    connect = psycopg2.connect(dbname='OnlineShop',
                               user='postgres',
                               password='JustStan13',
                               host='127.0.0.1'
                               )
    with connect.cursor() as cursor:

        all_products = cursor.execute('SELECT * FROM products')
        print(f"products table: {cursor.fetchall()}")
        pass
except:
    print("Can't establish connection to database")