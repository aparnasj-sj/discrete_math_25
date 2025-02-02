from itertools import product

for t in product('abc', repeat=2):
    print(*t, sep='', end=' ')


# Permutations are ordered selections without repetitions. The number of permutations is 
from itertools import permutations

for t in permutations('abc', 2):
    print(*t, sep='', end=' ')

# Combinations are unordered selections without repetitions. Also known as sets
from itertools import combinations

for t in combinations('abc', 2):
    print(*t, sep='', end=' ')

#Combinations with repetitions are unordered selections with repetitions. Also known as multisets. B
from itertools import combinations_with_replacement

for t in combinations_with_replacement('abc', 2):
    print(*t, sep='', end=' ')
# aa ab ac bb bc cc 
