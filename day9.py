# loading input
f = open("day9.dat", "r")

contents = f.read()
# split into lines
rows = contents.splitlines()

grid = list(map(lambda x: list(x), rows))

# establish bounds
max_x = len(grid[0])
max_y = len(grid)

# get coord at x, y as int
def get(x,y, in_list):
  if x > max_x or y > max_y or x < 1 or y < 1:
    return None
  return int(in_list[y - 1][x - 1])

def check_adj(x,y, in_list):
  curr = get(x, y, in_list)
  # check up -y
  up = get(x, y - 1, in_list)
  # check down +y
  down = get(x, y + 1, in_list)
  # check left -x
  left = get(x - 1, y, in_list)
  # check right +x
  right = get(x + 1, y, in_list)
  low_point = all([ up == None or up > curr, down == None or down > curr, left == None or left > curr, right == None or right > curr])
  return low_point

tot_risk = 0
low_points = []

for y, line in enumerate(grid):
  for x, point in enumerate(line):
    low_point = (check_adj(x + 1, y + 1, grid))
    if low_point:
      low_points.append({
        "x": x + 1,
        "y": y + 1,
        "val": get( x + 1, y + 1, grid)
      })
      tot_risk = tot_risk + 1 + get( x + 1, y + 1, grid)

print("Part 1 - Total Risk", tot_risk)
    
# Part 2
# Start with low points
# Branch out, recursively, until you hit top (9) or a dip

#print(low_points)

def part_of_basin(dir, curr):
  if dir == None:
    return False;
  return all([dir != 9, dir > curr])

def get_basin_value(x, y, in_list, points_traversed):
  
  curr = get(x, y, in_list)
  basin_pts = 1

  point = f'{x}:{y}'
  if point in points_traversed:
    # we've already seen this point
    return 0
  points_traversed.append(point)

  # check up -y
  up = get(x, y - 1, in_list)
  if(part_of_basin(up, curr)):
    basin_pts = basin_pts + get_basin_value(x, y - 1, in_list, points_traversed) 
  # check down +y
  down = get(x, y + 1, in_list)
  if(part_of_basin(down, curr)):
    basin_pts = basin_pts + get_basin_value(x, y + 1, in_list, points_traversed) 
  # check left -x
  left = get(x - 1, y, in_list)
  if(part_of_basin(left, curr)):
    basin_pts = basin_pts + get_basin_value(x - 1, y, in_list, points_traversed) 
  # check right +x
  right = get(x + 1, y, in_list)
  if(part_of_basin(right, curr)):
    basin_pts = basin_pts + get_basin_value(x + 1, y, in_list, points_traversed) 

  return basin_pts
  

basins = []

for point in low_points:
  points_traversed = []
  basin_size = get_basin_value(point["x"], point["y"], grid, points_traversed)
  basins.append({
    "point": point,
    "size": basin_size
  })


print("Part 2", sorted(basins, key=lambda x: x["size"], reverse = True)[0:3])
# 107, 102, 96
