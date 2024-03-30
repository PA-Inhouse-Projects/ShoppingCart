import sqlite3


class SQLClient:
    con = sqlite3.connect('ShoppingCartDB.db')
    cur = con.cursor()

    def __init__(self, **kwargs):
        operation = kwargs.get('operation')
        self.data = kwargs
        self.operation = {
            'create_table': self.create_table,
            'insert_table': self.insert_table,
            'fetch_all': self.fetch_all
        }
        if operation not in self.operation:
            return {'error': "operation does not supported"}

        self.operation[operation]()

    def create_table(self):
        column = []
        for key, value in self.data.get("fields").items():
            column.append(f"{key} {value}")
        opr = f"CREATE TABLE IF NOT EXISTS {self.data.get('table_name')}({', '.join(column)});"
        SQLClient.cur.execute(opr)
        SQLClient.con.commit()

    def insert_table(self):
        columns = []
        values = []
        for key, value in self.data.get("fields").items():
            columns.append(key)
            values.append(str(value))

        opr = f"INSERT INTO {self.data.get('table_name')}({', '.join(columns)}) VALUES ({', '.join(values)});"
        SQLClient.cur.execute(opr)
        SQLClient.con.commit()

    def fetch_all(self):
        if 'fields' in self.data.keys():
            fields = ', '.join(self.data.get('fields'))
        else:
            fields = '*'

        if 'condition' in self.data.keys():
            condition = 'WHERE '
            conditions = []
            for key, value in self.data.get('condition').items():
                conditions.append(f'{key} = {value}')
            condition += " AND ".join(conditions)
        else:
            condition = ""

        opr = f"SELECT {fields} FROM {self.data.get('table_name')} {condition};"
        return SQLClient.cur.execute(opr).fetchall()
