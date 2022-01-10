f = open("day1.dat", "r")

contents = f.read()
contents_split = contents.splitlines()


prev_line = -1

inc_dec_counts = {
  "Increased": 0,
  "Decreased": 0
}

for line in contents_split:
  if prev_line == -1:
    print("Doing nothing, first value")
  elif int(line) > prev_line:    
    inc_dec_counts["Increased"] = inc_dec_counts["Increased"] + 1
  else:
    inc_dec_counts["Decreased"] = inc_dec_counts["Decreased"] + 1

  prev_line = int(line)

print(inc_dec_counts)

prev_window_sum = -1;
window = []

sum_inc_dec_counts = {
  "Increased": 0,
  "Decreased": 0
}

for line in contents_split:
  window.append(int(line))
  if len(window) > 3:
    window.pop(0) ## remove first item
  if len(window) == 3:
    window_sum = sum(window)
    if window_sum > prev_window_sum and prev_window_sum != -1:
      sum_inc_dec_counts["Increased"] = sum_inc_dec_counts["Increased"] + 1
    prev_window_sum = window_sum
print(sum_inc_dec_counts)


