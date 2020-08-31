#Importing...
import maya.cmds as mc

#For every object selected, a locator will be created and snapped to selection.

# Select the object(s)
obj = mc.ls(sl=True)

# Storing the selections into an array and 'slicing' the array: extract elements based on a start and stop.
# Array[Start:End]. For example [x:] means index 'x' through end.
items = obj[0:]

for position in items:
    #Get location of selection (translations, rotations)
    trans = mc.xform(position, ws=True, q=True, t=True)
    rot = mc.xform(position, ws=True, q=True, ro=True)
    tx, ty, tz = trans[0], trans[1], trans[2]
    rx, ry, rz = rot[0], rot[1], rot[2]

    #Create Locator
    Loc = mc.spaceLocator()

    #Snap Locator(s) to selected object(s)
    mc.xform(Loc, ws=True, t=(tx, ty, tz))
    mc.xform(Loc, ws=True, ro=(rx, ry, rz))

    #Success!
    print "Oh Snap!"