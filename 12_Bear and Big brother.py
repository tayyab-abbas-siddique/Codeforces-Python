a, b = list(map(int, input().split()))

if __name__ == "__main__":
    count = 0
    
    while a <= b:
        a = a * 3
        b = b * 2
        count += 1
    
    
    print(count)

# https://www.codeforces.com/problemset/problem/791/A
