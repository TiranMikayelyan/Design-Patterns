# WITHOUT OCP
class Order:
    def __init__(self, weight):
        self.weight = weight

    def calculate_shipping(self, shipping_type):

        if shipping_type == "standard":
            return 1000

        elif shipping_type == "express":
            return 2500

        elif shipping_type == "pickup":
            return 0

        elif shipping_type == "international":
            return self.weight * 2000

        elif shipping_type == "drone":
            return 5000 + self.weight * 1500


order = Order(3)

print(order.calculate_shipping("standard"))
print(order.calculate_shipping("express"))
print(order.calculate_shipping("pickup"))
print(order.calculate_shipping("international"))
print(order.calculate_shipping("drone"))


# WITH OCP

class ShippingMethod:
    def calculate(self, weight):
        pass


class StandardShipping(ShippingMethod):
    def calculate(self, weight):
        return 1000


class ExpressShipping(ShippingMethod):
    def calculate(self, weight):
        return 2500


class PickupShipping(ShippingMethod):
    def calculate(self, weight):
        return 0


class InternationalShipping(ShippingMethod):
    def calculate(self, weight):
        return weight * 2000


class DroneShipping(ShippingMethod):
    def calculate(self, weight):
        return 5000 + weight * 1500


class Order:
    def __init__(self, weight):
        self.weight = weight

    def calculate_shipping(self, shipping_method):
        return shipping_method.calculate(self.weight)


order = Order(3)

standard = StandardShipping()
express = ExpressShipping()
pickup = PickupShipping()
international = InternationalShipping()
drone = DroneShipping()

print(order.calculate_shipping(standard))
print(order.calculate_shipping(express))
print(order.calculate_shipping(pickup))
print(order.calculate_shipping(international))
print(order.calculate_shipping(drone))


class SameDayShipping(ShippingMethod):  # Here we can see OCP meaning
    def calculate(self, weight):
        return 4000 + weight * 1000


same_day = SameDayShipping()

print(order.calculate_shipping(same_day))
