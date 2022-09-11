import sqlite3


class DBConnection:
    def __init__(self, db_name):
        self.conn = sqlite3.connect('dal/' + db_name + ".db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def query(self, sql):
        result = self.cursor.execute(sql)
        result_list = []
        for row in result.fetchall():
            result_dict = {}
            for r in row.keys():
                result_dict[r] = row[r]
            result_list.append(result_dict)
        return result_list

    def query_and_print(self, sql):
        print(self.query(sql))

    def create_table(self, table_name, column_list):
        columns_str = ', '.join(column_list)
        query = f"CREATE TABLE {table_name}(id, {columns_str})"
        self.execute(query)

    def close(self):
        self.conn.close()
