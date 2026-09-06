# WITHOUT DIP

class MySQLDatabase:
    def save(self, data):
        print("Saving to MySQL")


class OrderService:
    def __init__(self):
        self.database = MySQLDatabase()

    def save_order(self, order):
        self.database.save(order)


order_service = OrderService()
order_service.save_order("Order #123")



# WITH DIP

class Database:
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print("Saving to MySQL")


class PostgreSQLDatabase(Database):
    def save(self, data):
        print("Saving to PostgreSQL")


class OrderService:
    def __init__(self, database):
        self.database = database

    def save_order(self, order):
        self.database.save(order)


mysql = MySQLDatabase()
postgresql = PostgreSQLDatabase()

order_service1 = OrderService(mysql)
order_service1.save_order("Order #123")

order_service2 = OrderService(postgresql)
order_service2.save_order("Order #456")
