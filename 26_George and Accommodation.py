n = int(input())
count = 0
if __name__ == "__main__":
    for i in range(n):
        p, q = list(map(int,input().split()))
        if q - p >= 2:
            count += 1
        else:
            count += 0
        
    print(count)
# https://codeforces.com/problemset/problem/467/A
