import maya.cmds as cmds

txt = "Leg_##_Jnt_####"

count = txt.count("#")
if count > 0:
    x = txt.find("#" * count)

#remember .partition on the string

txt = "Leg_####_Jnt"
x = txt.partition("####")
print(x)

#asdfasdf

txt = "50"

x = txt.zfill(10)
print(x)