import math
f = open("day18.dat", "r")
contents = f.read().splitlines()

def parse_into_tuple(partsgen):
  lhs = None
  rhs = None

  while True:
    part = next(partsgen)
    if part == "[":
      lhs = parse_into_tuple(partsgen)
    elif part == "]":      
      return (lhs, rhs)
    elif part == ",":
      rhs = parse_into_tuple(partsgen)
    else:
      # number, just return
      return int(part)

def check_for_ten(sfnum_in):
  num_ptr = sfnum_in
  lhs, rhs = num_ptr

  if type(lhs) is tuple:    
    lhs = check_for_ten(lhs)

  if type(rhs) is tuple:
    rhs = check_for_ten(rhs)

  if type(lhs) is int and lhs >= 10:
    lhs = (math.floor(lhs/2), math.ceil(lhs/2))
  elif type(rhs) is int and rhs >= 10:
    rhs = (math.floor(rhs/2), math.ceil(rhs/2))

  return (lhs, rhs)

already_exploded = False

def check_for_nested_pair(sfnum_in, level):
  global already_exploded
  num_ptr = sfnum_in
  lhs, rhs = num_ptr
  explode_out = None

  if level == 4 and not already_exploded:
    # explode lhs
    explode_lhs = lhs
    explode_rhs = rhs
    already_exploded = True
    return (0, (explode_lhs, explode_rhs))

  if type(lhs) is tuple:    
    lhs, explode_out = check_for_nested_pair(lhs, level+1)

  if type(rhs) is tuple:
    rhs, explode_out = check_for_nested_pair(rhs, level+1)

  if explode_out is not None and level < 4:
    expleft, expright = explode_out
    print("Explode check", level, lhs, rhs)
    if type(lhs) is int:
      lhs += expleft
      explode_out = (0, expright)
    if type(rhs) is int:
      rhs += expright
      explode_out = (expleft, 0)
  if level == 0:
    already_exploded = False
  return ((lhs, rhs), explode_out)


test_num1 = (7,(6,(5,(4,(3,2)))))
test_num2 = (((((9,8),1),2),3),4)
test_num3 = ((6,(5,(4,(3,2)))),1)
test_num4 = ((((0, 7), 4), ((7, 8), (0, (6, 7)))), (1, 1))
result = check_for_nested_pair(test_num4, 0)

print(result)

print(check_for_ten([1, 11]))


def reduce_sfnumber(sfnum_in):

  sfnum_out = sfnum_in.copy()
  # apply 1 action
  # explore
  # split 
  return sfnum_out


def process_adds(in_contents):
  loop = iter(in_contents)
  first_num = next(loop)
  # load first number
  accum = parse_into_tuple((part for part in list(first_num)))
  # now we loop the rest and sum up
  for number in loop:
    rhs = parse_into_tuple((part for part in list(number)))
    accum = (accum, rhs)
    print("After addition", accum)
    # now reduce
    has_reduces = True
    while has_reduces:
      print(accum)
      new_num = check_for_nested_pair(accum, 0)[0]
      if new_num != accum:
        accum = new_num
        continue
      new_num = check_for_ten(new_num)
      if new_num == accum:
        # Nothing's changed
        has_reduces = False
      accum = new_num
    

  print(accum)


   


#process_adds(contents)
