k, n, w = list(map(int,input().split()))
lst = []

if __name__ == "__main__":
 
    for i in range(1, w + 1):
        a = i * k 
        lst.append(a)
    
    b = sum(lst[0:w + 1])
    c = b - n
    if c < 0:
        print(0)
    else:
        print(c)   

# https://codeforces.com/problemset/problem/546/A
