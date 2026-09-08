n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
 
num = a[k-1]
count = 0
a_use = []
 
for i in a:
    if i >= num and i != 0:
        count += 1
   
print(count)

# https://codeforces.com/problemset/problem/158/A
