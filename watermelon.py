# You have a water melon.
# You have to print YES if:
#        1. The weight of water melon is divisible by 2.
#        2. The half of the weight of the water melon is also divisible by 2.
# Other wise print NO

water_melon_weight = int(input())  # Getting the weight of the water melon
 
if water_melon_weight > 2 and  water_melon_weight % 2 == 0: # Checking if it is divisible by 2 and only is the number which's half is odd.
    print("Yes")  # Printing YES for situation
else:
    print("No") # Printing NO for this situation.


# Find the full problem here
# https://www.codeforces.com/problemset/problem/4/A
