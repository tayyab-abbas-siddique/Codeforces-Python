a, b = list(map(int, input().split()))

if __name__ == "__main__":
    for i in range(b):
        if a % 10 == 0:
            a //= 10
        else:
            a -= 1
        
    print(a)
# https://codeforces.com/problemset/problem/977/A
