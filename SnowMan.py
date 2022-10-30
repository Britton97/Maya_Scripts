import maya.cmds as cmds
import random


def my_function():
  xPos = 0
  yPos = 0
  while xPos < 10:
    while yPos < 10:
        newSphere = cmds.polySphere()
        cmds.move(xPos,0, yPos, newSphere)
        x = random.uniform(.1,1)
        y = random.uniform(.1, 1)
        z = random.uniform(1, 1)
        cmds.scale(x,y,z, newSphere)
        yPos += 1
    yPos = 0
    xPos += 1

def Snow_Man():
    base = cmds.polySphere()
    cmds.move(0,2,0, base)
    cmds.scale(2,2,2,base)

    middle = cmds.polySphere()
    cmds.move(0,4,0, middle)
    cmds.scale(1.5,1.5,1.5, middle)

    top = cmds.polySphere()
    cmds.move(0, 5.5, 0, top)
    cmds.scale(1, 1, 1, top)

    hat = cmds.polyCylinder()
    cmds.move(0,6.8,0, hat)
    cmds.scale(.735,.694,.735, hat)

    brim = cmds.polyCylinder()
    cmds.move(0,6.238,0, brim)
    cmds.scale(1.048,.19,1.048, brim)

Snow_Man()