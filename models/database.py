import psycopg2

from models.exceptions import RecordNotFound, TooManyRecords


class DB:
    _connection = psycopg2.connect(dbname='OnlineShop',
                                   user='postgres',
                                   password='JustStan13',
                                   host='127.0.0.1')

    def query(self, query, **kwargs):
        with self._connection.cursor() as cursor:
            cursor.execute(query, kwargs)
            columns = [col[0] for col in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return rows

    def query_single(self, query, **kwargs):
        result = self.query(query, **kwargs)
        if not result:
            raise RecordNotFound()
        if len(result) > 1:
            raise TooManyRecords()
        return result[0]


db = DB()
