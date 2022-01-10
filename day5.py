import collections

# loading input
f = open("day5.dat", "r")

# read and split into lines
contents = f.read().splitlines()

def traverse_line(line):
  line_pts = line.split(" -> ")
  print(line_pts)
  start_coord = line_pts[0].split(",")
  end_coord = line_pts[1].split(",")
  
  x1 = int(start_coord[0])
  y1 = int(start_coord[1])
  x2 = int(end_coord[0])
  y2 = int(end_coord[1])

  line_dir = None
  if x2 == x1:
    # x stays the same, vertical
    line_dir = "up" if y2 > y1 else "down"
  elif y2 == y1:
    # y stays the same, horizontal
    line_dir = "right" if x2 > x1 else "left"
  elif x2 > x1 and y2 > y1:
    # up & right
    line_dir = "upright"
  elif x1 > x2 and y2 > y1:
    # up & left
    line_dir = "upleft"
  elif x1 > x2 and y1 > y2:
    # down & left
    line_dir = "downleft"
  elif x2 > x1 and y1 > y2:
    # down & left
    line_dir = "downright"


  print("Line direction", line_dir)

  pts_traversed = []

  if line_dir == "up" or line_dir == "down":
    for step in range(abs(y2 - y1) + 1):
      pts_traversed.append(
        "{0}:{1}".format(x1,y1 + step if line_dir == "up" else y1 - step)
      )
  if line_dir == "right" or line_dir == "left":
    for step in range(abs(x2 - x1) + 1):
      pts_traversed.append(
        "{0}:{1}".format(x1 + step if line_dir == "right" else x1 - step,y1)
      )
  if line_dir == "upright":
    for step in range(abs(x2 - x1) + 1):
      pts_traversed.append(
        "{0}:{1}".format(x1 + step, y1 + step)
      )
  if line_dir == "upleft":
    for step in range(abs(x2 - x1) + 1):
      pts_traversed.append(
        "{0}:{1}".format(x1 - step, y1 + step)
      )
  if line_dir == "downleft":
    for step in range(abs(x2 - x1) + 1):
      pts_traversed.append(
        "{0}:{1}".format(x1 - step, y1 - step)
      )
  if line_dir == "downright":
    for step in range(abs(x2 - x1) + 1):
      pts_traversed.append(
        "{0}:{1}".format(x1 + step, y1 - step)
      )

  return pts_traversed

tot_pts_traversed = []

for line in contents:
  tot_pts_traversed.extend(traverse_line(line))

dups = [item for item, count in collections.Counter(tot_pts_traversed).items() if count > 1]

print(len(dups))

