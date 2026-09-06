# WITHOUT LSP
class Employee:
    def work(self):
        print("Employee is working")

    def take_break(self):
        print("Employee is taking a break")


class Developer(Employee):
    def work(self):
        print("Developer is coding")


class Robot(Employee):
    def work(self):
        print("Robot is working")

    def take_break(self):
        raise Exception("Robot cannot take a break")


def manage_employee(employee):
    employee.work()
    employee.take_break()


developer = Developer()
robot = Robot()

manage_employee(developer)
manage_employee(robot)


# WITH LSP

class Employee:
    def work(self):
        print("Employee is working")


class HumanEmployee(Employee):
    def take_break(self):
        print("Human is taking a break")


class Developer(HumanEmployee):
    def work(self):
        print("Developer is coding")


class Robot(Employee):
    def work(self):
        print("Robot is working")


def manage_employee(employee):
    employee.work()


def manage_human_employee(employee):
    employee.work()
    employee.take_break()


developer = Developer()
robot = Robot()

manage_human_employee(developer)
manage_employee(robot)
