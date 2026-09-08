t = int(input())
count = 0
for i in range(t):
    n = list(map(int, input().split()))
    if sum(n) >= 2:
        count += 1
    else:
        count += 0
        
print(count)

# https://codeforces.com/problemset/problem/231/A
