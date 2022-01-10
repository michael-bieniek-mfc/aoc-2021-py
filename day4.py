from functools import reduce

# loading input
f = open("day4.dat", "r")

contents = f.read()
# split into lines
contents_split = contents.splitlines()

draws = contents_split.pop(0).split(',')
contents_split.pop(0)
boards = []
board_content = []
for line in contents_split:
  if len(line) == 0:
    continue
  board_content.extend(line.split())
  
  if len(board_content) == 25:
    ## full board
    boards.append({
      "marked": [False] * 25,
      "board": board_content.copy(),
      "winner": False
    })
    ## restore buffer
    board_content = []

def is_winner(board_in):
  mk = board_in["marked"]
  return any([all(mk[slice(0, 5)]),
  all(mk[slice(5, 10)]),
  all(mk[slice(10, 15)]),
  all(mk[slice(15, 20)]),
  all(mk[slice(20, 25)]),
  all(mk[slice(0, 25, 5)]),
  all(mk[slice(1, 25, 5)]),
  all(mk[slice(2, 25, 5)]),
  all(mk[slice(3, 25, 5)]),
  all(mk[slice(4, 25, 5)])])

def calc_score(board_in):
  print(board_in["board"])
  return reduce(lambda x, y: int(x) + int(y), board_in["board"], 0)

winning_board = None
winners = 0

for draw in draws:
  print("Drawing", draw)
  # check all boards
  for board in filter(lambda x: not x["winner"], boards):
    ind = -1
    try:
        ind = board["board"].index(draw)
    except ValueError:
      a = None
    if ind >= 0:
        board["marked"][ind] = True
        board["board"][ind] = '0'
    if(is_winner(board)):
      winning_board = board
      print("We have a winner")
      print(winning_board)
      print("Score", calc_score(winning_board) * int(draw))
      winners = winners + 1
      board["winner"] = True

      if all(
        list(map(lambda x: x["winner"], boards))):
        break
    if all(map(lambda x: x["winner"], boards)):
      break








