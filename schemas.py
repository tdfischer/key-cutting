class KeySchema(object):
  pinPositions = []
  pinDepths = []
  shoulderLength = 0
  pinSurfaceLength = 0
  thickness = 0

class Kwikset5Pin(KeySchema):
  pinPositions = [
    0.247,
    0.397,
    0.547,
    0.697,
    0.847,
  ]

  pinDepths = [
    0,
    0.001,
    0.024,
    0.047,
    0.070,
    0.93,
    0.116,
    0.139
  ]

  shoulderLength = 0.05
  thickness = 0.05
  pinSurfaceLength = 0.07

class Schlage5Pin(KeySchema):
  pinPositions = [
    0.231,
    0.387,
    0.543,
    0.699,
    0.855
  ]

  pinDepths = [
    0.005,
    0.020,
    0.035,
    0.050,
    0.065,
    0.080,
    0.095,
    0.110,
    0.125,
    0.140
  ]

  shoulderLength = 0.05

  thickness = 0.06

  pinSurfaceLength = 0.035


