import re
f = open("day13.dat", "r")

contents = f.read()

# split into lines
rows = contents.splitlines()

pred_is_dot_instr = lambda x: re.match(r'\d+,\d+', x)
pred_is_fold_instr = lambda x: re.match(r'fold along', x)

# our dot instructions, as (x,y) tuples
dot_instrs = list(map(lambda instr: (int(instr.split(",")[0]), int(instr.split(",")[-1])), list(filter(pred_is_dot_instr, rows))))

def map_to_fold(raw):
  substrind = len('fold along ')
  trimmed = raw[substrind:]
  return (trimmed.split("=")[0], int(trimmed.split('=')[-1]))

# fold instructions
fold_instrs = list(map(map_to_fold,list(filter(pred_is_fold_instr, rows))))

def print_grid(dots):
  max_x = max(list(map(lambda dot: dot[0], dots)))
  max_y = max(list(map(lambda dot: dot[-1], dots)))
  print(max_x)
  for y in range (max_y+1):
    set_x_on_line = set(map(lambda pt: pt[0],list(filter(lambda point: point[-1] == y, dots))))
    print("".join(["#" if x in set_x_on_line else "." for x in range(max_x + 1)]))

# now, let's start folding
def fold(dot_instrs, fold_instr):
  direction = fold_instr[0]
  line = fold_instr[-1]
  if direction == "y":
    # fold up, along horizontal line at y
    # all coords with y > # will be mirrored on line
    def map_fold(point):
      ( x, y ) = point
      if y > line:
        return ( x, line - abs(y - line) )
      else:
        return (x, y)
    return list(map(map_fold, dot_instrs))
  elif direction =="x":
    # fold up, along vertical line at x
     # all coords with x > # will be mirrored on line
    def map_fold(point):
      ( x, y ) = point
      if x > line:
        return ( line - abs(x - line), y )
      else:
        return (x, y)
    return list(map(map_fold, dot_instrs))

firstFold = fold(dot_instrs, fold_instrs[0])

fold_iter = iter(fold_instrs)
firstFold = fold(dot_instrs, next(fold_iter))


print(len(set(firstFold)))
folded_paper = firstFold

# now let's fold the remaining times
for fold_instr in fold_iter:
  folded_paper = fold(folded_paper, fold_instr)

print_grid(folded_paper)