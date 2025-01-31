# rule of pdt

from itertools import product
for p in product(['a', 'b', 'c'], ['x', 'y']):
  print("".join(p))

# tuple
from itertools import product
for p in product("ab", repeat=3):
  print("".join(p))

# Permutations
from itertools import permutations
for p in permutations("abcd", 2):
  print("".join(p))
  
