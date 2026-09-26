import sys 

water_melon_weight = int(input("Enter your number:"))

if __name__ == "__main__":
    if water_melon_weight % 2 == 0 and water_melon_weight > 2:
        sys.stdout.write("Yes")
    else:
        sys.stdout.write("No") 


# https://codeforces.com/problemset/problem/4/A
