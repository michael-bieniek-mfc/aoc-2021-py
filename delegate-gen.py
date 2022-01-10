from typing import Iterable
from itertools import filterfalse

def flatten(items, ignore_types=(bytes, str )):
  for x in items:
    if isinstance(x, Iterable) and not isinstance(x, ignore_types):
      yield from flatten(x)
    else:
      yield x


print(list(flatten(["Pluralsight", "is", ["a", ["great", "platform", "to"]], "learn"])))

