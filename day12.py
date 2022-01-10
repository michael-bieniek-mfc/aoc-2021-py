import sys
f = open("day12.dat", "r")

contents = f.read()
# split into lines
rows = contents.splitlines()

def build_cave_vectors(rows):
  cave_vectors_set = { row.split("-")[0] for row in rows }.union({ row.split("-")[1] for row in rows })
  cave_vectors = {cave: [] for cave in cave_vectors_set }
  for row in rows:
    (source_cave, dest_cave) = row.split("-")
    # two-way!
    cave_vectors[source_cave].append(dest_cave)
    if dest_cave != "end" and source_cave != "start":
      cave_vectors[dest_cave].append(source_cave)
  return cave_vectors

def build_traversals(cave_vectors):
  all_paths = []
  
  def traverse_cave(cave, cave_vectors, path):
    new_path = path + cave
    if cave == "end":
        all_paths.append(new_path)
    else:
      dests = cave_vectors[cave]
      
      is_small_cave = lambda x: x.lower() == x and x != "start"
      visisted_small_caves = list(filter(is_small_cave, new_path.split(",")))
      can_we_visit = lambda x: any([
        x == "end", # at the end
        not is_small_cave(x) and x != "start", # can visit big ones any number of times
        is_small_cave(x) and not x in visisted_small_caves, # a new small cave
        is_small_cave(x) and x in visisted_small_caves and len(visisted_small_caves) == len(set(visisted_small_caves)) # a small cave being visited twice, first time
      ])


      for dest in dests:
        if can_we_visit(dest):
          traverse_cave(dest, cave_vectors, new_path + ",")

  traverse_cave("start", cave_vectors, "")

  return all_paths   

caves = build_cave_vectors(rows)

traversals = build_traversals(caves)

print(len(traversals))

