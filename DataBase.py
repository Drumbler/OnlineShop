import psycopg2


class DB:
    connection = psycopg2.connect(dbname='OnlineShop',
                                  user='postgres',
                                  password='JustStan13',
                                  host='127.0.0.1')

    def get_goods(self):
        with self.connection.cursor() as cursor:
            all_products = cursor.execute('SELECT * FROM products')
            columns = [col[0] for col in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return rows


db = DB()
