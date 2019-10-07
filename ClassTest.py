class Robot:
    name = "robot"
    def info(self):
        print('내 이름은 ', self.name, ' 입니다.')


robot = Robot()
robot.info()
print(robot.name)
print(isinstance(robot, int))
print(isinstance(robot, Robot))
