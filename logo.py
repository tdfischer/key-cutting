#!/usr/bin/env python

def pos(x, y):
  print "G1 X%d Y%d"%(x * scale, y * scale)

scale = 1

print "G94"
print "G20"
print "G90"
print "G64 P0.00500"
print "S10584"
print "G0 Z0.1"
print "M3"
print "G1 F3000 X-0.1"


# top line
pos(0, 0)
pos(66, -25)
pos(118, -25)
pos(133, 0)
pos(200, 0)
pos(200, 75)

# speaker

pos(180, 75)
pos(220, 125)
pos(220, 75)
pos(250, 50)
pos(250, 150)
pos(220, 125)

# bottom line
pos(200, 125)
pos(200, 200)
pos(133, 200)
pos(118, 175)
pos(81, 175)
pos(66, 200)
pos(0, 200)

# resistor
pos (0, 150)
pos (-30, 112)
pos (30, 87)
pos (-30, 62)
pos (0, 50)
pos (0, 0)
