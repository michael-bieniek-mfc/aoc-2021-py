from functools import reduce
from itertools import chain

f = open("day20.dat", "r")
contents = f.read()
rows = contents.splitlines()

contents_iter = iter(rows)

alg = next(contents_iter)
# nom nom blank line
next(contents_iter)

grid = list(map(lambda x: list(map(str, list(x))), contents_iter))


def debug_grid(in_grid):
  # let's get some basics of its shape
  max_y = len(in_grid)
  max_x = len(in_grid[0])
  print("\n")
  print("".join(list(map(lambda x: str(x % 10), range(max_x)))))
  for y in range(max_y):
    print("".join(in_grid[y]), y)

def count_hash(in_grid):
  return reduce(lambda acc, x: acc + x.count('#'), in_grid, 0)

border_width = 2

# function to add 2 dark spaces around grid to simulate inf
def pad_grid(in_grid, step):
  out_char = "." if step % 2 == 1 else "#"
  out_grid = []
  width = len(in_grid[0])
  for i in range(border_width):
    out_grid.append([out_char] * (width + border_width * 2))  
  for row in in_grid:
    new_row = list(chain([out_char] * border_width, list(row), [out_char] * border_width))
    out_grid.append(new_row)
  for i in range(border_width):
    out_grid.append([out_char] * (width + border_width * 2))  
  return out_grid


def get_sq(coord, in_grid, inf="."):
  x, y = coord
  height = len(in_grid)
  width = len(in_grid[0])
  def get_pt(x2, y2, in_grid):
    if any([x2 < 0, y2 < 0, x2 >= width, y2 >= height]):
      return inf
    else:
      return in_grid[y2][x2]
  square = ""
  square += get_pt(x - 1, y - 1, in_grid)
  square += get_pt(x, y - 1, in_grid)
  square += get_pt(x + 1, y - 1, in_grid)
  square += get_pt(x - 1, y, in_grid)
  square += get_pt(x, y, in_grid)
  square += get_pt(x + 1, y, in_grid)
  square += get_pt(x - 1, y + 1, in_grid)
  square += get_pt(x, y + 1, in_grid)
  square += get_pt(x + 1, y + 1, in_grid)
  bin_square = "".join(list(map(lambda pixel: "1" if pixel == "#" else "0", list(square))))
  return int(bin_square, 2)

def enhance(in_grid, in_alg, step = 1):
  ref_grid = pad_grid(list(map(lambda x: list(map(str, list(x))), in_grid)), step)
  new_grid = pad_grid(list(map(lambda x: list(map(str, list(x))), in_grid)), step)

  height = len(new_grid)
  width = len(new_grid[0])
  # start processing at first layer of padding
  for y in range(height):
    for x in range(width):
      # determine new pixel value by looking at surrounding square
      alg_ind = get_sq((x, y), ref_grid, "." if step % 2 == 1 else "#")
      pixel_out = in_alg[alg_ind]
      new_grid[y][x] = pixel_out
  return new_grid    

#debug_grid(grid)
step1_grid = enhance(grid, alg, 1)
#debug_grid(step1_grid)
step2_grid = enhance(step1_grid, alg, 2)
#debug_grid(step2_grid)

new_grid = grid
for step in range(50):
  # note, step is 1-indexed
  new_grid = enhance(new_grid, alg, step + 1) 

print(count_hash(new_grid))

