# WITHOUT SRP
class Order:
    def __init__(self, products, customer_email):
        self.products = products
        self.customer_email = customer_email

    # Order calculation
    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product["price"] * product["quantity"]

        return total

    # Discount
    def apply_discount(self, total, customer_type):
        if customer_type == "vip":
            return total * 0.8

        elif customer_type == "student":
            return total * 0.9

        return total

    # Database
    def save_to_database(self):
        print("Saving order to database")

    # Email
    def send_confirmation_email(self):
        print(f"Sending email to {self.customer_email}")

    # Invoice
    def generate_invoice(self):
        print("Generating PDF invoice")

    def print_invoice(self):
        print("Printing invoice")

    # Delivery
    def send_to_delivery(self):
        print("Sending order to delivery service")


products = [
    {"name": "Laptop", "price": 500000, "quantity": 1},
    {"name": "Mouse", "price": 10000, "quantity": 2}
]

order = Order(products, "user@gmail.com")

total = order.calculate_total()
total = order.apply_discount(total, "vip")

order.save_to_database()
order.send_confirmation_email()
order.generate_invoice()
order.print_invoice()
order.send_to_delivery()






# WITH SRP
class Order:
    def __init__(self, products, customer_email):
        self.products = products
        self.customer_email = customer_email

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product["price"] * product["quantity"]

        return total


class Discount:
    def apply_discount(self, total, customer_type):
        if customer_type == "vip":
            return total * 0.8

        elif customer_type == "student":
            return total * 0.9

        return total


class OrderRepository:
    def save(self, order):
        print("Saving order to database")


class EmailService:
    def send_confirmation(self, order):
        print(f"Sending email to {order.customer_email}")


class Invoice:
    def generate(self, order):
        print("Generating PDF invoice")

    def print_invoice(self, order):
        print("Printing invoice")


class DeliveryService:
    def send(self, order):
        print("Sending order to delivery service")


products = [
    {"name": "Laptop", "price": 500000, "quantity": 1},
    {"name": "Mouse", "price": 10000, "quantity": 2}
]

order = Order(products, "user@gmail.com")

discount = Discount()
repository = OrderRepository()
email = EmailService()
invoice = Invoice()
delivery = DeliveryService()

total = order.calculate_total()
total = discount.apply_discount(total, "vip")

repository.save(order)
email.send_confirmation(order)
invoice.generate(order)
invoice.print_invoice(order)
delivery.send(order)
