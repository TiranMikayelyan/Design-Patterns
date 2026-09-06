# WITHOUT ISP
class Worker:
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise Exception("Robot doesn't eat")

    def sleep(self):
        raise Exception("Robot doesn't sleep")


robot = Robot()

robot.work()
robot.eat()



# WITH ISP

class Workable:
    def work(self):
        print("Working")


class Eatable:
    def eat(self):
        print("Eating")


class Sleepable:
    def sleep(self):
        print("Sleeping")


class Human(Workable, Eatable, Sleepable):
    pass


class Robot(Workable):
    def work(self):
        print("Robot is working")


human = Human()
robot = Robot()

human.work()
human.eat()
human.sleep()

robot.work()
