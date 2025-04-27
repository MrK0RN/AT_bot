import pg8000.native

class Pg8000DB:
    def __init__(self, database, user, password, host='localhost', port=5434):
        self.conn = pg8000.native.Connection(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

    def execute(self, query, params=None, fetch=False):
        """
        Выполнить SQL-запрос с параметрами.
        :param query: SQL-запрос с именованными плейсхолдерами (:param)
        :param params: dict с параметрами для подстановки
        :param fetch: если True - вернуть результат запроса
        :return: результат запроса или None
        """
        if params is None:
            params = {}

        result = self.conn.run(query)

        if fetch:
            return result  # список кортежей с данными SELECT
        else:
            return None  # для INSERT/UPDATE/DELETE

    def close(self):
        self.conn.close()