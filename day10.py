from functools import reduce
from statistics import median

# loading input
f = open("day10.dat", "r")

contents = f.read()
# split into lines
rows = contents.splitlines()

open_tags = ["(", "[", "{", "<"]
close_tags = [")", "]", "}", ">"]

tags = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">",
}

pts = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

scores = []

incomplete_lines = []
incomplete_lines_stack = []
corrupted_lines = []

for row in rows:
  
  stack_counter = 0 # for detecting incompletes
  stack = []
  point_counter = 0
  first_corr = None

  items = list(row)
  for item in items:
    if item in open_tags:
      # put corresponing closing tag on stack (to be expected)
      stack.append(tags[item])
      stack_counter = stack_counter + 1
    if item in close_tags:
      # we better expect it
      expected = stack.pop(-1)
      stack_counter = stack_counter - 1
      if expected != item and first_corr == None:
        point_counter = point_counter + pts[item]
        first_corr = item
        corrupted_lines.append(row)
        break
  if(first_corr != None):
    # we have corruption!
    scores.append(point_counter)
  else:
    # it's incomplete
    incomplete_lines.append(row)
    # mutate in place - bad - but what to do?
    stack.reverse()
    incomplete_lines_stack.append(stack)

print("Part 1", sum(scores))

inc_cost = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

def cost_of_incompleteness(missing_closures):
  return reduce(lambda x,y: (5 * x) + inc_cost[y], missing_closures, 0)

incomplete_scores = list(map(lambda x: cost_of_incompleteness(x), incomplete_lines_stack))

print("Part 2", median(incomplete_scores))