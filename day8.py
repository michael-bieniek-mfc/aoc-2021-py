# loading input
f = open("day8.dat", "r")

contents = f.read()
# split into lines
contents_split = contents.splitlines()

def test_uniques(signal):
  # is a 1, 4, 7, 8
  return len(signal) == 2 or len(signal) == 3 or len(signal) == 4 or len(signal) == 7

unique_count = 0

for entry in contents_split:
  seg_out = entry.split(" | ")
  segs = seg_out[0].split()
  sigs = seg_out[1].split()
  uniques = len(list(filter(test_uniques, sigs)))
  unique_count = unique_count + uniques

print("Part 1", unique_count)

def x_in_y(x,y):
  x_split = list(x)
  y_split = list(y)
  return all(elem in y_split for elem in x_split)


# 0, 6 and 9 are 6 segments
def find_9(segs, digit_to_sig):
  reduced = list(filter(lambda x: len(x) == 6, segs))
  # all[9 in 8, 1 in 9, 7 in 9, 4 in 9]  
  result = None
  for seg in reduced:
    # test for digit
    if all([x_in_y(seg, digit_to_sig[8]), x_in_y(digit_to_sig[1], seg), x_in_y(digit_to_sig[7], seg), x_in_y(digit_to_sig[4], seg)]):
      result = seg
      break
  return "".join(sorted(result))

def find_0(segs, digit_to_sig):
  reduced = list(filter(lambda x: len(x) == 6, segs))
  # all[0 in 8, 1 in 0, 7 in 0, and can't be 9]  
  result = None
  for seg in reduced:
    # test for digit
    if all([x_in_y(seg, digit_to_sig[8]), x_in_y(digit_to_sig[1], seg), x_in_y(digit_to_sig[7], seg), not x_in_y(digit_to_sig[4], seg)]):
      result = seg
      break
  return "".join(sorted(result))

def find_6(segs, digit_to_sig):
  reduced = list(filter(lambda x: len(x) == 6, segs))
  # all[6 in 8, and not 0!]
  result = None
  for seg in reduced:
    # test for digit
    if all([x_in_y(seg, digit_to_sig[8]), x_in_y(digit_to_sig[1], seg), x_in_y(digit_to_sig[7], seg), not x_in_y(digit_to_sig[4], seg)]):
      result = seg
      break
  return "".join(sorted(result))

# 2, 3, 5 are 5 segments
def find_2(segs, digit_to_sig):
  reduced = list(filter(lambda x: len(x) == 5, segs))
  # all[2 in 8, 2 nin 9, 1 nin 2]
  result = None
  for seg in reduced:
    # test for digit
    if all([x_in_y(seg, digit_to_sig[8]), not x_in_y(seg, digit_to_sig[9]), not x_in_y(digit_to_sig[1], seg)]):
      result = seg
      break
  return "".join(sorted(result))

def find_3(segs, digit_to_sig):
  reduced = list(filter(lambda x: len(x) == 5, segs))
  # all[3 in 8, 3 in 9, 1 in 3]
  result = None
  for seg in reduced:
    # test for digit
    if all([x_in_y(seg, digit_to_sig[8]), x_in_y(seg, digit_to_sig[9]), x_in_y(digit_to_sig[1], seg)]):
      result = seg
      break
  return "".join(sorted(result))

def find_5(segs, digit_to_sig):
  reduced = list(filter(lambda x: len(x) == 5, segs))
  # all[5 in 8, 5 in 9, 1 not in 5]
  result = None
  for seg in reduced:
    # test for digit
    if all([x_in_y(seg, digit_to_sig[8]), x_in_y(seg, digit_to_sig[9]), not x_in_y(digit_to_sig[1], seg)]):
      result = seg
      break
  return "".join(sorted(result))

def determine_mapping(segs, sigs):
  digit_to_sig = [None] * 10

  sorted_segs = list(map(lambda x: "".join(sorted(x)), segs))

  # disambiguate the easy ones: 1, 4, 7, 8
  digit_to_sig[1] = next((x for x in sorted_segs if len(x) == 2), None)
  digit_to_sig[4] = next((x for x in sorted_segs if len(x) == 4), None)
  digit_to_sig[7] = next((x for x in sorted_segs if len(x) == 3), None)
  digit_to_sig[8] = next((x for x in sorted_segs if len(x) == 7), None)

  # remove the knowns from segs
  reduced_list = list(filter(lambda x: not test_uniques(x), sorted_segs))
  digit_to_sig[9] = find_9(reduced_list, digit_to_sig)
  reduced_list.remove(digit_to_sig[9])
  digit_to_sig[0] = find_0(reduced_list, digit_to_sig)
  reduced_list.remove(digit_to_sig[0])
  digit_to_sig[2] = find_2(reduced_list, digit_to_sig)
  reduced_list.remove(digit_to_sig[2])
  digit_to_sig[3] = find_3(reduced_list, digit_to_sig)
  reduced_list.remove(digit_to_sig[3])
  digit_to_sig[5] = find_5(reduced_list, digit_to_sig)
  reduced_list.remove(digit_to_sig[5])
  digit_to_sig[6] = reduced_list[0] # last one!
  
  # let's go over the signals now
  digits_out = list(map(lambda x: str(digit_to_sig.index("".join(sorted(x)))), sigs))
  return int("".join(digits_out))

result = []

for entry in contents_split:
  seg_out = entry.split(" | ")
  segs = seg_out[0].split()
  sigs = seg_out[1].split()
  result.append(determine_mapping(segs, sigs))

print("Part 2", sum(result))