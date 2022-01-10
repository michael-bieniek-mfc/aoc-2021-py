"""
Perf notes: This is O(2^n) problem, with n being the number of iterations. Although this might
be manageable to do with lists for small n, it quickly becomes impossible with larger values of n.
Instead of using lists, we need to use a dict with block counts since each rule consumes 1 block, e.g.: AB
and produces two new blocks, e.g.: AC, CB if rule is AB => C

"""

from collections import Counter

f = open("day14.dat", "r")

contents = f.read()
lines = contents.splitlines()

lineiter = iter(lines)
polymer_template = next(lineiter)
next(lineiter) # gobble up blank line

# build a list of tuples for insertion rules
insert_rules = list(map(lambda line: (line.split(" -> ")[0], line.split(" -> ")[-1]), lineiter))

def apply_rule(blocks, rules):
  added_letter_counter = {y: 0 for y in set(map(lambda x: x[-1], rules))}
  resultant_dict = dict(blocks)

  for block in blocks.keys():
    # find matching rule
    matching_rule = list(filter(lambda rule: rule[0] == block, rules))
    if len(matching_rule) >= 1:
      rule = matching_rule.pop(0)
      # apply rule
      block_count = blocks[block]
      spawn1 = rule[0][0] + rule[-1]
      spawn2 = rule[-1] + rule[0][1]
      resultant_dict[block] = resultant_dict[block] - block_count
      resultant_dict[spawn1] = block_count if spawn1 not in resultant_dict else resultant_dict[spawn1] + block_count
      resultant_dict[spawn2] = block_count if spawn2 not in resultant_dict else resultant_dict[spawn2] + block_count

      added_letter_counter[rule[-1]] = added_letter_counter[rule[-1]] + block_count

  return (resultant_dict, added_letter_counter)

def polymerization(template, rules, steps = 1):
  letter_counter = Counter(list(template))
  result_coll = [ template[x:x+2] for x in range(0, len(template) -1 ) ]
  result = dict(Counter(result_coll))
  # imperative approach for now
  for step in range(steps):
    (result, added_letter_counter) = apply_rule(result, rules)
    letter_counter += Counter(added_letter_counter)
  print(max(letter_counter.values()) - min(letter_counter.values()))
  return result

def find_min_max_char(output):
  by_letter = {}

  # find the highest occurrence of a character as well as lowest
  for block in output.keys():
    if output[block] != 0:
      first_letter = block[0]
      second_letter = block[1]
      by_letter[first_letter] = output[block] if first_letter not in by_letter else by_letter[first_letter] + output[block]
      by_letter[second_letter] = output[block] if second_letter not in by_letter else by_letter[second_letter] + output[block]

  return by_letter

# Step 1, 10 steps
output = polymerization(polymer_template, insert_rules, 40)
output_counts = find_min_max_char(output)
