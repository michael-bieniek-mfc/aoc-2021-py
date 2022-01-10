# loading input
f = open("day11.dat", "r")

contents = f.read()
# split into lines
rows = contents.splitlines()

max_x = len(rows[0])
max_y = len(rows)

grid = list(map(lambda x: list(map(int, list(x))), rows))

def inc_energy(in_grid, flashes):
  out_grid = copy_grid(in_grid)
  for x in range(max_x):
    for y in range(max_y):
      out_grid = inc_energy_at_pt(out_grid, x + 1, y + 1, flashes)
  # adjust anything > 9 to 0
  out_grid = list(map(lambda x: list(map(lambda y: 0 if y > 9 else y, x)), out_grid))
  return out_grid

def copy_grid(in_grid):
  out_grid = list(map(lambda x: list(x), in_grid))
  return out_grid

def debug_grid(in_grid):
  print("\n")
  for row in in_grid:
    print("".join(list(map(str, row))))

def inc_energy_at_pt(in_grid, x, y, flashes):
  new_grid = copy_grid(in_grid)
  if any([ x > max_x, x < 1, y > max_y, y < 1]):
    # beyond the map, do nothing
    # print("Beyond map")
    return new_grid
  energy = in_grid[y - 1][x - 1]
  
  if energy < 10:
    # hasn't flashed yet
    new_energy = energy + 1   
    new_grid[y - 1][x - 1] = new_energy 
    if new_energy > 9:
      # we're flashing   
      flashes.append(True)   
      # radiate outwards in all 9 directions, recursively
      new_grid = inc_energy_at_pt(new_grid, x + 1, y, flashes)
      new_grid = inc_energy_at_pt(new_grid, x + 1, y + 1, flashes)
      new_grid = inc_energy_at_pt(new_grid, x + 1, y - 1, flashes)
      new_grid = inc_energy_at_pt(new_grid, x - 1, y, flashes)
      new_grid = inc_energy_at_pt(new_grid, x - 1, y + 1, flashes)
      new_grid = inc_energy_at_pt(new_grid, x - 1, y - 1, flashes)
      new_grid = inc_energy_at_pt(new_grid, x, y + 1, flashes)
      new_grid = inc_energy_at_pt(new_grid, x, y - 1, flashes)
  return new_grid

def step(in_grid):
  # increase energy
  flashes = []
  new_grid = inc_energy(in_grid, flashes)
  return {
    "grid": new_grid,
    "flashes": len(flashes)
  }
out_grid = copy_grid(grid)

tot_flashes = 0

for flash in range(1000):  
  result = step(out_grid)
  out_grid = result["grid"]
  tot_flashes = tot_flashes + result["flashes"]
  if result["flashes"] == 100:
    print(flash, "all flashed")

