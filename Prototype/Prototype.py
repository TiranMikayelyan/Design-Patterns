import copy


class Employee:
    def __init__(self, name, position, salary, skills):
        self.name = name
        self.position = position
        self.salary = salary
        self.skills = skills

    def clone(self):
        return copy.deepcopy(self)

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        print(f"Skills: {self.skills}")
        print("-" * 30)


employee1 = Employee("Aram", "Junior QA", 250000, ["Python", "SQL"])

employee2 = employee1.clone()
employee3 = employee1.clone()

employee2.position = "Middle QA"
employee2.salary = 400000

employee3.skills.append("Selenium")

employee1.show_info()
employee2.show_info()
employee3.show_info()
