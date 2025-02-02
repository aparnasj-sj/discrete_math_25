# What is the number of PINs with sum of digits equal to 9

from itertools import product

pins = product(range(10), repeat=4)
print(len([pin for pin in pins if sum(pin) == 9]))

# What is the number of PINs with sum of digits equal to 10 
from itertools import product

pins = product(range(10), repeat=4)
print(len([pin for pin in pins if sum(pin) == 10]))
"""
^^ prints 286 , and is off by 4 , bcos of 4 illegal pins (10,0,0,0) (0,10,0,0)...
correct ans = 286-4 = 282
"""
# What is the number of PINs with non-increasing digits?
from itertools import product

pins = product(range(10), repeat=4)
print(len([pin for pin in pins
           if all(pin[i] <= pin[i + 1] for i in range(3))]))
# 
