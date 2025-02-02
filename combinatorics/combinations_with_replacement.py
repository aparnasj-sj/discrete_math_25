# selection with replacement
"""
We have anunlimited supply of tomatoes, bell peppers and lettuce. 
We want to make a salad out of 4 units among these three ingredients (we do not have to use all ingredients). 
The order in which we use the ingredients does not matter. How many different salads we can make? 
We do not have the formula to answer this question yet, so try to list all the salads first or create a program that will do that for you.
Then you can count the number of salads by hand (note the answer to the problem should be the number).
"""

from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBL", 4):
    print("".join(c))
