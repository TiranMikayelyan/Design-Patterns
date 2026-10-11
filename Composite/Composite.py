from abc import ABC, abstractmethod


class EmployeeComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Employee(EmployeeComponent):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def get_salary(self):
        return self.salary


class Department(EmployeeComponent):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, component):
        self.members.append(component)

    def remove(self, component):
        self.members.remove(component)

    def show_details(self):
        print(f"Department: {self.name}")

        for member in self.members:
            member.show_details()

    def get_salary(self):
        return sum(member.get_salary() for member in self.members)


employee1 = Employee("Aram", "QA Engineer", 300000)
employee2 = Employee("Ani", "Developer", 500000)
employee3 = Employee("Karen", "Team Lead", 600000)

qa_department = Department("QA")
qa_department.add(employee1)

dev_department = Department("Development")
dev_department.add(employee2)
dev_department.add(employee3)

company = Department("Company")
company.add(qa_department)
company.add(dev_department)

company.show_details()

print("Total salary:", company.get_salary())
