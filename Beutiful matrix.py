row = 0
col = 0
 
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        if arr[j] == 1:
            row = i
            col = j
 
moves = abs(row - 2) + abs(col - 2)
 
print(moves)

# https://www.codeforces.com/problemset/problem/263/A
