from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
move = 9
robotArm.grab()
for x in range(5):
    for x in range(move):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(move-1):
        robotArm.moveLeft()
    robotArm.grab()
    move = move-2
robotArm.drop()
robotArm.wait()