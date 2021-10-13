from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for x in range(7):
 robotArm.moveRight()
robotArm.grab()
for x in range(8): 
    for x in range(1):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(2):
        robotArm.moveLeft()
    robotArm.grab()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()