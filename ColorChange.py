import maya.cmds as cmds
import random

def ColorChange(passIN):
    objects = cmds.ls(sl=True)
    for j in objects:
        if passIN == "red":
            cmds.color(j, rgb=(1, 0, 0))
        if passIN == "green":
            cmds.color(j, rgb=(0, 1, 0))
        if passIN == "blue":
            cmds.color(j, rgb=(0, 0, 1))
ColorChange("blue")