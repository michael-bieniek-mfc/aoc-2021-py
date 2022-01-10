# loading input
f = open("day7.dat", "r")

from functools import reduce

contents = f.read()

hoz_pos = [int(x) for x in contents.split(",")]

max_pos = max(hoz_pos)
min_pos = min(hoz_pos)

def cost_of_moving_pt1(subs, pos):
  # move every sub to a given position, pos, and get its total cost
  return reduce(lambda x, y: x + (abs(pos - y)), subs, 0)

# do the test for every position, then get the smallest one
results1 = min(list(map(lambda x: cost_of_moving_pt1(hoz_pos, x), range(max_pos))))

print("Part 1 - Minimum fuel is", results1)

def cost_of_moving_pt2(subs, pos):
  return reduce(lambda x, y: x + sum(range(abs(pos - y) + 1)), subs, 0)

results2 = min(list(map(lambda x: cost_of_moving_pt2(hoz_pos, x), range(max_pos))))
print("Part 2 - Minimum fuel is", results2)

# optimization, pre-sum ranges
presums = list(map(lambda x: sum(range(abs(x) + 1)), range(max_pos+1)))

def cost_of_moving_pt2_faster(subs, pos):
  return reduce(lambda x, y: x + presums[abs(pos - y)], subs, 0)

results3 = list(map(lambda x: cost_of_moving_pt2_faster(hoz_pos, x), range(max_pos)))
min_fuel3 = min(results3)

print("Part 2 (optimized) - Minimum fuel is", min_fuel3)