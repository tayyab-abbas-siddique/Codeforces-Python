def has_distinct_digits(number):
    digits = str(abs(number))
    return len(digits) == len(set(digits))
 
if __name__ == "__main__":
    a = int(input())
    for i in range(a + 1, 9015):
        if has_distinct_digits(i) == True:
            c = has_distinct_digits(i)
            break 
        
        
        
        
    print(i)
# https://codeforces.com/problemset/problem/271/A
