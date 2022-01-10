from statistics import multimode
from enum import Enum
import time

def current_milli_time():
    return round(time.time() * 1000)

# loading input
f = open("day3.dat", "r")

contents = f.read()
# split into lines
contents_split = contents.splitlines()

number_bits = 12

# gets the largest, most common bit from a list
# invert = True: gets the smallest, least common bit from a list
def find_most_common_bit(list, invert = False):
  # disambiguates multiple modes, take biggest
  mode_bit = max(multimode(list))
  # this does the ~ flip, if invert
  return ("0" if mode_bit == "1" else "1") if invert else mode_bit


# extracts a list of bits at position (pos)
def list_from_pos(input_list, pos):
  return list(map(lambda item: (item[pos]), input_list))

start_time = current_milli_time()

gamma_rate_bin = "".join(list(map(lambda x: find_most_common_bit(list_from_pos(contents_split, x)), range(number_bits))))
epsilon_rate_bin = "".join(list(map(lambda x: find_most_common_bit(list_from_pos(contents_split, x), True), range(number_bits))))

end_time_1 = current_milli_time()

print('Part 1', 'Power consumption', int(gamma_rate_bin, 2) * int(epsilon_rate_bin, 2), "in", end_time_1 - start_time, "ms")

## Part Deux
class LifeSupportMode(Enum):
  OXYGEN_GENERATOR_RATING = 0
  CO2_SCRUBBER_RATING = 1

# Returns a reduced list
def reduce_list(list_input, pos, is_least_common):
  most_common_bit = find_most_common_bit(list_from_pos(list_input, pos), is_least_common)
  # print("most common bit at pos", pos, "is", most_common_bit)
  return list(filter(lambda x: x[pos] == most_common_bit, list_input))

def find_life_support_rating(list_input, life_support_mode):
  working_list = list(list_input)
  for ind in range(number_bits):
    working_list = reduce_list(working_list, ind, life_support_mode is LifeSupportMode.CO2_SCRUBBER_RATING)
    if(len(working_list) == 1):
      # return last remaining number
      return working_list.pop(0)

#print(find_oxy_gen_rat(contents_split))
oxy_gen_rat = int(find_life_support_rating(contents_split, LifeSupportMode.OXYGEN_GENERATOR_RATING),2)
co2_scrub_rat = int(find_life_support_rating(contents_split, LifeSupportMode.CO2_SCRUBBER_RATING),2)

end_time_2 = current_milli_time()

print('Part 2', 'Life support rating', oxy_gen_rat * co2_scrub_rat, "in", end_time_2 - end_time_1, "ms")

# Immutable data
# Pure functions 
# Functions as "first-class" citizens
# Declarative - map, filter, stats