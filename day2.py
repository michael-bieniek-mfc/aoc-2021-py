from functools import reduce

# loading input
f = open("day2.dat", "r")

contents = f.read()
# split into lines
contents_split = contents.splitlines()

def reducer_func_pt1(aggr, instr):
  direction, val = instr.split(" ")
  if direction == "forward":
    aggr["x"] = aggr["x"] + int(val)
  elif direction == "up":
    aggr["z"] = aggr["z"] - int(val)
  elif direction == "down":
    aggr["z"] = aggr["z"] + int(val)
  return aggr

result = reduce(reducer_func_pt1, contents_split, { "x": 0, "z": 0 })

print("Part 1", result["x"] * result["z"])

## Part 2

def reducer_func_pt2(aggr, instr):
  direction, val = instr.split(" ")
  if direction == "forward":
    # both moves forward, and deeper based on aim
    aggr["x"] = aggr["x"] + int(val)
    aggr["z"] = aggr["z"] + aggr["aim"] * int(val)
  elif direction == "up":
    aggr["aim"] = aggr["aim"] - int(val)
  elif direction == "down":
    aggr["aim"] = aggr["aim"] + int(val)
  return aggr

result = reduce(reducer_func_pt2, contents_split, { "x": 0, "z": 0, "aim": 0 })

print("Part 2", result["x"] * result["z"])


