from functools import cache

scores = {
  "player1": 0,
  "player2": 0
}

position = {
  "player1": 4,
  "player2": 1
}

die_val = 0
rolls = 0
win_score = 21

def roll_det_die():
  global die_val, rolls
  rolls+= 1
  die_val+= 1
  if die_val > 100:
    die_val = 1
  return die_val

def roll_quant_die():
  # return all roll possibilities
  # dice rolls 1, 2, 3 in every universe
  # outcome can be 3 -> 9
  return [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]


def get_new_pos(curr_val, roll_val):
  new_val = (curr_val + roll_val) % 10
  if new_val == 0:
    new_val = 10
  return new_val

for x in range(10000):
  try:
    # player 1
    p1_pos = position["player1"]
    roll_val = 0
    for a in range(3):
      roll_val += roll_det_die()
    position["player1"] = get_new_pos(p1_pos, roll_val)
    scores["player1"] = scores["player1"] + position["player1"]
    if scores["player1"] >= 1000:
      print("Player 1 wins with", scores["player1"])
      break

    # player 2
    p2_pos = position["player2"]
    roll_val = 0
    for a in range(3):
      roll_val += roll_det_die()
    position["player2"] = get_new_pos(p2_pos, roll_val)
    scores["player2"] = scores["player2"] + position["player2"]
    if scores["player2"] >= 1000:
      print("Player 2 wins with", scores["player2"])
      break
  except KeyError as e:
    print("player not found", e)

print("position",position)
print("scores",scores)
print("Rolls", rolls)


wins = {
  "player1": 0,
  "player2": 0
}

memory = {(x, y): 0 for x in range(1,11) for y in range(0,21)}

for key, value in memory.items():
  (pos, score) = key
  tot_wins = 0
  rolls_that_dont_win = []
  for roll in [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]:
    if score + get_new_pos(pos, roll) >= 21:
      tot_wins += 1
    else:
      rolls_that_dont_win.append(roll)
  memory[key] = (tot_wins, rolls_that_dont_win)

tot_rolls = 0

@cache
def spawn_game(state):
  p1_scr, p2_scr, p1_pos, p2_pos, next_player = state
  states = []
  if next_player == 1:
    num_wins, not_wins = memory[(p1_pos, p1_scr)]
    for roll in not_wins:
      new_p1_pos = get_new_pos(p1_pos, roll)
      new_p1_scr = p1_scr + new_p1_pos
      states.append((new_p1_scr, p2_scr, new_p1_pos, p2_pos, 2))
  elif next_player == 2:
    num_wins, not_wins = memory[(p2_pos, p2_scr)]
    for roll in not_wins:
      new_p2_pos = get_new_pos(p2_pos, roll)
      new_p2_scr = p2_scr + new_p2_pos
      states.append((p1_scr, new_p2_scr, p1_pos, new_p2_pos, 1))
  return (num_wins, states)

iterations = 0
def play_quantum_game(state, multiplier = 1):
  global iterations
  iterations += 1
  if iterations % 100000000 == 0:
    print(wins)
  nums_wins, states = spawn_game(state)
  if(state[4] == 1):
    wins["player1"] += (multiplier * nums_wins)
  elif(state[4] == 2):
    wins["player2"] += (multiplier * nums_wins)
  seen = set()
  for new_state in states:
    if new_state in seen:
      continue
    seen.add(new_state)
    play_quantum_game(new_state, states.count(new_state) * multiplier)

print("Part 1", 920*993)

# oh my goodness, we really need to use memoization and recursion to solve this (see @cache) 
play_quantum_game((0, 0, 4, 1, 1))

print("Part 2", wins)