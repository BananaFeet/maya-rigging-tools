import maya.cmds as mc

# Creates "markers" to selected object(s)--preferably joints.
selection = mc.ls(sl=True)
selJnts = selection[0:]

for position in selJnts:
    trans = mc.xform(position, ws=True, q=True, t=True)
    rot = mc.xform(position, ws=True, q=True, ro=True)
    tx, ty, tz = trans[0], trans[1], trans[2]
    rx, ry, rz = rot[0], rot[1], rot[2]

    mrkr = mc.polySphere(n="marker", sx=20, sy=20, r=.20)
    mc.color(mrkr, rgb=(0.663, 0.182, 0.482))

    mc.xform(mrkr, ws=True, t=(tx, ty, tz))
    mc.xform(mrkr, ws=True, ro=(rx, ry, rz))

    print("Markers have been placed")
