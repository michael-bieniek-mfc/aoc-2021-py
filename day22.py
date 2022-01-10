from functools import reduce

f = open("day22.dat", "r")
contents = f.read().splitlines()

# on x=-20..26,y=-36..17,z=-47..7

bounds = (-50, 50)

def process_step(instr_in, cubes_in):
  cubes_out = set(cubes_in)
  instr = instr_in.split(" ")
  is_on = True if instr[0] == "on" else False
  coords = instr[-1].split(",")

  lower_bounds, upper_bounds = bounds

  x_range = [int(part) for part in coords[0].split("=")[-1].split("..") if lower_bounds <= int(part) <= upper_bounds]
  y_range = [int(part) for part in coords[1].split("=")[-1].split("..") if lower_bounds <= int(part) <= upper_bounds]
  z_range = [int(part) for part in coords[2].split("=")[-1].split("..") if lower_bounds <= int(part) <= upper_bounds]
  
  if any([len(x_range) == 0, len(y_range) == 0, len(z_range) == 0]):
    # at least one range out of bounds
    # return same set
    return cubes_out

  for x in range(x_range[0],x_range[-1] + 1):
    for y in range(y_range[0],y_range[-1] + 1):
      for z in range(z_range[0],z_range[-1] + 1):
        if is_on:
          # turn on (add)
          cubes_out.add((x, y, z))
        else:
          # turn off (remove)
          if (x, y, z) in cubes_out:
            cubes_out.remove((x, y, z))
  return cubes_out

"""
Approach we'll take here is to split cubes up instead of initializing an ungodly sized set
"""
def process_step_pt2(instr_in, on_cubes):
  cubes_out = list(on_cubes)
  instr = instr_in.split(" ")
  is_on = True if instr[0] == "on" else False
  coords = instr[-1].split(",")

  x_range = tuple(int(part) for part in coords[0].split("=")[-1].split(".."))
  y_range = tuple(int(part) for part in coords[1].split("=")[-1].split(".."))
  z_range = tuple(int(part) for part in coords[2].split("=")[-1].split(".."))


  # find cubes that overlap
  overlapping = list(filter(lambda cube: any([
    all([ cube[0][0] <= x_range[0] <= cube[0][-1], cube[1][0] <= y_range[0] <= cube[1][-1], cube[2][0] <= z_range[0] <= cube[2][-1] ]),
    all([ cube[0][0] <= x_range[-1] <= cube[0][-1], cube[1][0] <= y_range[-1] <= cube[1][-1], cube[2][0] <= z_range[-1] <= cube[2][-1] ]),
  ]), on_cubes))

  if len(overlapping) == 0:
    if is_on:
      cubes_out.append((x_range, y_range, z_range))
  else:
    # overlapping
    print("overlapping", instr_in)
    for overlap in overlapping:
      x, y, z = overlap
      # determine overlap area
      x_overlap = x[-1] - x_range[0]
      y_overlap = y[-1] - y_range[0]
      z_overlap = z[-1] - z_range[0]
      overlap_area = x_overlap * y_overlap * z_overlap

      if is_on:
        # only add the range that doesn't overlap
        pass
      else:
        # break-up
        # what's the overlap
        print("Overlapping area to be turned off", )
    
  return cubes_out

def process_rows(in_rows):
  init_set = set()
  set_ptr = init_set
  for row in in_rows:
    set_ptr = process_step(row, set_ptr)
  return len(set_ptr)


#print("Part 1", process_rows(contents))

# Part 2 will require optimizations

def reduce_cube_count(acc, cube):
  x, y, z = cube
  return acc + abs(x[0] - x[-1]) * abs(y[0] - y[-1]) * abs(z[0] - z[-1])

def process_rows_pt2(in_rows):
  on_cubes = []
  cubes_ptr = on_cubes
  for row in in_rows:
    cubes_ptr = process_step_pt2(row, cubes_ptr)
  
  # now count through reduce
  count_on = reduce(reduce_cube_count, cubes_ptr, 0)
  
  return count_on

print("Part 2", process_rows_pt2(contents))