import maya.cmds as cmds

def OrderNamesMaya(passIn):
    objects = cmds.ls(sl=True)
    counter = 1
    for obj in objects:
        print(obj)
        cmds.rename(obj, Start(passIn, counter))
        counter = counter + 1



def Start(passIn, counter):
    digits = CutWord(passIn, 1).count('#')
    cutUp = passIn.partition('#' * digits)
    replacement = str(counter).zfill(digits)
    newName = cutUp[0] + replacement + cutUp[2]
    return newName


def CutWord(word, returnSpot):
    x = word.count("#")
    y = '#' * x
    cutWord = word.partition(y)
    return cutWord[returnSpot]


#c = ["Leg_###_Jnt", "Leg_###_Jnt", "Leg_###_Jnt", "Arm_###_Jnt", "Arm_###_Jnt", "Arm_###_Jnt"]
#OrderNames(c)
OrderNamesMaya("Leg_####_Jnt")