#Paint Can Calculator
import math

def paint_calc(height,width,cover):
  sqft = height*width
  cans = math.ceil(sqft/cover)
  print(f"You need {cans} cans to paint the wall"
  )

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


