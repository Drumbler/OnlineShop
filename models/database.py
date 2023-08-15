import psycopg2


class DB:
    _connection = psycopg2.connect(dbname='OnlineShop',
                                  user='postgres',
                                  password='JustStan13',
                                  host='127.0.0.1')

    def query(self, query):
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return rows


db = DB()
