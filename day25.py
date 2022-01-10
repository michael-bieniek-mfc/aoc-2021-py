"""
Notes:
Originally, I tried to solve this in a functional way with immutable data structures (i.e. functions returning changed copies of grid)
However, the memory footprint was too large for the puzzle input. Using a simple imperative approach with mutated data worked well
"""
contents = []

with open("day25.dat", "r") as f:
  contents = [list(row) for row in f.read().splitlines()]

# establish grid bounds
width = len(contents[0])
height = len(contents)

def print_grid(contents):
  print("\n")
  list(print("".join(row))for row in contents)

def move(ref_contents):
  something_moved = any([shift_rows(ref_contents), shift_cols(ref_contents)])
  return something_moved

def shift_rows(ref_contents):
  something_moved = False
  for row in ref_contents:
    row_copy = list(row)
    for n, member in enumerate(row_copy):
      if member == '>':
        # someone to the right?
        right_ind = (n+1) % width
        if row_copy[right_ind] == '.':
          # can move!
          something_moved = True
          row[n] = '.'
          row[right_ind] = ">"
  return something_moved

def shift_cols(ref_contents):
  something_moved = False
  for x in range(width):
    col_copy = [ref_contents[ind][x] for ind in range(height)]
    for y in range(height):
      member = col_copy[y]
      if member == 'v':
        south_ind = (y + 1) % height
        if col_copy[south_ind] == '.':
          # can move!
          something_moved = True
          ref_contents[y][x] = '.'
          ref_contents[south_ind][x] = 'v'
  return something_moved

more_moves = True
counter = 0

while more_moves:
  move_result = move(contents)
  counter += 1
  if move_result is False:
    break

print("Day 25 - Part A", counter)