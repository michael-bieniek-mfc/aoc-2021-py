from functools import reduce

# loading input
f = open("day6.dat", "r")

contents = f.read()

init_pop_fish = [int(x) for x in contents.split(",")]

part1_fishies = init_pop_fish.copy()
part2_fishies = init_pop_fish.copy()

def day_cycle(fishies):
  new_day = list(map(lambda x: x-1, fishies))
  # count new fish spawned
  new_fish_spawned = len(list(filter(lambda x: x < 0, new_day)))

  # update old fish who had baby fihs
  new_day = list(map(lambda x: 6 if x < 0 else x, new_day))

  # add new fish
  new_day.extend([8] * new_fish_spawned)
  return new_day



init_counts = [0] * 9 # ages 0 thru 8
for age in part2_fishies:
  init_counts[age] = init_counts[age] + 1

for day in range(256):
  # how many fish birthing?
  births = init_counts.pop(0)
  init_counts.append(births)
  init_counts[6] = init_counts[6] + births

print("Part 2", reduce(lambda x, y: x + y, init_counts, 0))
  



## recursive, efficient
def calc_children(age, days):
  curr_age = age
  fish_count = 1
  for day in range(days):
    curr_age = curr_age - 1
    if curr_age < 0:
      curr_age = 6
      # spawn child
      fish_count = fish_count + calc_children(8, days-day - 1)
  return fish_count
  
for x in range(80):
  part1_fishies = day_cycle(part1_fishies)


print("Part 1", len(part1_fishies))


accum = 0
for x in init_pop_fish:
  accum = accum + calc_children(x, 80)

print("Part 1 faster", accum)


#accum = 0
#for x in init_pop_fish:
 # accum = accum + calc_children(x, 256)

#print("Part 2 faster", accum)


