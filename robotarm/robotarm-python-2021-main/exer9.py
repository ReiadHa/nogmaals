from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')


for i in range(1,5):
  for x in range(i):
    robotArm.grab()
    for x in range(5):
      robotArm.moveRight()
    robotArm.drop()
    for x in range(5):
      robotArm.moveLeft()
  robotArm.moveRight()


robotArm.wait()