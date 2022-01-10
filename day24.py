import math

contents = []
with open("day24.dat", "r") as f:
  contents = f.read().splitlines()

def process_instr_cort(instrs):
  registers = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
  }
  for instr in instrs:
    print(instr)
    instr_list = instr.split(" ")
    op = instr_list[0]
    if op == "inp":
      in_val = yield      
      registers[instr_list[-1]] = int(in_val)
    else:
      # these are operations
      a = instr_list[1]
      b = instr_list[2]
      print(b, b.isnumeric())
      if op == "add":
        registers[a] = registers[a] + int(b) if b.replace('-','').isnumeric() else registers[b]
      elif op == "mul":
        registers[a] = registers[a] * int(b) if b.replace('-','').isnumeric() else registers[b]
      elif op == "div":
        b_val = int(b) if b.replace('-','').isnumeric() else registers[b]
        if b_val == 0:
          raise(StopIteration("Bad op"))
        registers[a] = math.floor(registers[a] / b_val)
      elif op == "mod":
        a_val = registers[a]
        b_val = int(b) if b.replace('-','').isnumeric() else registers[b]
        if b_val <= 0 or a_val < 0:
          raise(StopIteration("Bad op"))
        registers[a] = a_val % b_val 
      elif op == "eql":
        b_val = int(b) if b.replace('-','').isnumeric() else registers[b]          
        registers[a] = 1 if registers[a] == b_val else 0
    print(registers)
  return registers

gen = process_instr_cort(contents)

# prime
next(gen)

13579246899999

for item in list('13579246899999'):
  gen.send(item)