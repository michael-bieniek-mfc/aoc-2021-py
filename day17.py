"""
--- Day 17: Trick Shot ---
The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
"""

target_split = "x=60..94, y=-171..-136".split(", ")
x_target = list(map(int,target_split[0][2:].split("..")))
y_target = list(map(int,target_split[1][2:].split("..")))

print("Target range is (x,y):", x_target, y_target)

def test_in_trench(pos, x_target, y_target):
  (x,y) = pos
  return all([ x >= x_target[0], x <= x_target[1], y >= y_target[0], y <= y_target[1] ])

def test_past_trench(pos, x_target, y_target):
  (x,y) = pos
  return any([x > x_target[1], y < y_target[0]])

watermark_y = 0

def process_step(pos, vel):
  
  global watermark_y
  
  ( pos_x, pos_y ) = pos
  ( vel_x, vel_y ) = vel
  
  new_pos = (pos_x + vel_x, pos_y + vel_y)

  new_vel_x = vel_x
  if vel_x > 0:
    new_vel_x -= 1
  elif vel_x < 0:
    new_vel_x += 1

  if vel_y == 0:
    # high point
    watermark_y = pos_y
  
  new_vel = (new_vel_x, vel_y - 1)
  #print("Position:", new_pos, "Velocity:", new_vel)
  return (new_pos, new_vel)



def try_velocity(vel, max_steps = 10000):
  curr_pos = (0,0)
  curr_vel = vel
  for step in range(max_steps):    
    (curr_pos, curr_vel) = process_step(curr_pos, curr_vel)
    if test_in_trench(curr_pos, x_target, y_target):
      #print("In trench!")
      return step
    if test_past_trench(curr_pos, x_target, y_target):
      return None

results = []

for x in range(100):
  for y in range(1000):
    watermark_y = 0
    if try_velocity((x, y - 500)) is not None:
      results.append((x, y - 500, watermark_y))

print(watermark_y)
print(sorted(results, key = lambda x: x[-1]))
print("Part 2", len(results))