class SQLQuery:
    def __init__(self, query):
        self.query = query

    def execute(self):
        print(self.query)


class SQLQueryBuilder:
    def __init__(self):
        self.columns = []
        self.table = None
        self.conditions = []
        self.order = None

    def select(self, *columns):
        self.columns = list(columns)
        return self

    def from_table(self, table):
        self.table = table
        return self

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def order_by(self, column):
        self.order = column
        return self

    def build(self):
        query = "SELECT " + ", ".join(self.columns)
        query += " FROM " + self.table

        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)

        if self.order:
            query += " ORDER BY " + self.order

        return SQLQuery(query)


query = (
    SQLQueryBuilder()
    .select("name", "age")
    .from_table("users")
    .where("age > 18")
    .where("city = 'Yerevan'")
    .order_by("name")
    .build()
)

query.execute()
