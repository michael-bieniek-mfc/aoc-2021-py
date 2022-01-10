import math
import timeit
f = open("day15.dat", "r")

contents = f.read()
rows = contents.splitlines()

grid = list(map(lambda x: list(map(int, list(x))), rows))

# establish bounds
max_x = len(grid[0])
max_y = len(grid)

exit_coord = (max_x, max_y)

print("Start coord", (1,1))
print("End coord", exit_coord)

risks = []
min_risk = math.inf
min_risk_path = None
min_path_traversal = ''

# get coord at x, y as int
# top left is (1,1)
def get(coord, in_list):
  ( x, y ) = coord
  if any([x > max_x, y > max_y,x < 1,y < 1]):
    return None
  return int(in_list[y - 1][x - 1])


def debug_grid(in_grid, visited_set):

  # let's get some basics of its shape
  max_x = len(in_grid[0])
  max_y = len(in_grid)

  print("\n")

  def map_func(coord):
    return "X" if coord in visited_set else str(get(coord, in_grid)) 

  for y in range(max_y):
    row = [(x + 1, y + 1) for x in range(max_x)]
    pop_row = list(map(map_func, row))
    print("".join(pop_row))

def enter_point(in_grid, coord, dest, visited, risk = 0):

  goal = dest
  if visited == None:
    visited = []

  new_visited = list(visited)
  
  ( x, y ) = coord
  up = (x, y - 1)
  down = (x, y + 1)
  right = (x + 1, y)
  left = (x - 1, y)
  valid_dir = []
  if y != 1:
    valid_dir.append(up)
  if y != max_y:
    valid_dir.append(down)
  if x != 1:
    valid_dir.append(left)
  if x != max_x:
    valid_dir.append(right)
 
 
  # do we see the exit point from here?
  if goal in valid_dir:
    # adding risk 1 for exit
    new_visited.append(goal)
    if(risk + 1 < min_risk):
      min_risk = 
      min_risk_path = list(new_visited)
    return risk + 1

  possible_dirs = list(filter(lambda coord: get(coord, in_grid) != None and coord not in new_visited, [down, right] ))
  for dirs in possible_dirs:
    new_risk = risk + get(dirs, in_grid)
  
    if new_risk < min_risk:
      # worth traversing since risk is still low
      new_visited = list(visited)
      new_visited.append(dirs)
      enter_point(in_grid, dirs, dest, new_visited, new_risk)

  return None


def shortest_distance_between(a, b, in_grid):


def get_traversal_risk(path, in_grid):
  new_path = list(filter(lambda x: x != (1,1), path))
  return sum(list(map(lambda x: get(x, in_grid), new_path)))

start_visisted = [(1,1)]
print(timeit.timeit(lambda: enter_point(grid, (1,1), start_visisted, 'Start:', 0), number = 1))

#print(min_path_traversal)
print(get_traversal_risk(min_risk_path, grid))

debug_grid(grid, min_risk_path)

