#!/usr/bin/env python
import sys
import schemas

# CONFIGURATION OPTIONS

# granularity: How many passes you want to mill with
granularity = 6

# invert: True if you're cutting the key upside down
invert = False

# bitHeight: How tall your cutting bit is
# If you've got an angled bit instead of a straight one, set this to end up
# cutting a straight edge.
bitHeight = 0.15

keyPIN = str(sys.argv[1])

schema = schemas.Schlage5Pin

print """
G94 ( use inches/min feed rate)
G20 ( use inches for coordinates )
G90 ( absolute coordinates )
G64 P0.00500 ( maximum deviation )
S10484 ( spindle speed for brass )
G0 Z0.1 ( lift up to avoid hitting the key )
G0 X0 Y0 ( move to the blade, just at the edge of the shoulder )
M3 ( start cutting )
G1 F3000 X-0.1 ( move over to the side before cutting the side off )
G1 X0 Y0 ( move into the key blade)"""

print "G1 Y%s ( move down the shoulder )"%(schema.thickness)

for cutLayer in range(1, granularity+1):
  layerDepth = (schema.thickness+bitHeight) * (cutLayer / float(granularity))
  print "G1 Z-%s ( start layer %s )"%(layerDepth, cutLayer)
  for cutPass in range(1, granularity+1):
    print ""
    if cutPass % 2 == 0:
      reverse = True
      print "( start pass %s in reverse, layer %s )"%(cutPass, cutLayer)
    else:
      reverse = False
      print "( start pass %s in forward, layer %s )"%(cutPass, cutLayer)
    if reverse:
      pinSet = reversed(range(0, len(keyPIN)))
    else:
      pinSet = range(0, len(keyPIN))
    for pinNumber in pinSet:
      pinType = int(keyPIN[pinNumber])
      pinCenter = schema.pinPositions[pinNumber]
      pinDepth = schema.pinDepths[pinType] * (cutPass / float(granularity))

      if invert:
        pinDepth = -pinDepth

      pinStart = pinCenter - schema.pinSurfaceLength
      pinEnd = pinCenter + schema.pinSurfaceLength

      if reverse:
        print "G1 Y%s X%s ( cut pin type %s at %s )"%(pinEnd, pinDepth, pinType, pinNumber)
        print "G1 Y%s"%(pinStart)
      else:
        print "G1 Y%s X%s ( cut pin type %s at %s )"%(pinStart, pinDepth, pinType, pinNumber)
        print "G1 Y%s"%(pinEnd)
    if reverse:
      print "G1 X0 Y0.05 ( move back down to the shoulder )"
    else:
      print "G1 Y1.17"

print ""
print "M2"
