s = input()

if __name__ == "__main__":
 
    upper = 0
    lower = 0
    
    for i in s:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        
    if upper > lower:
        print(s.upper())
    elif upper < lower:
        print(s.lower())
    else:
        print(s.lower())
# https://codeforces.com/problemset/problem/59/A
