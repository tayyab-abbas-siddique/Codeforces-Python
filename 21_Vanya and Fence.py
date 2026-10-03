n, h = list(map(int,input().split()))
a = list(map(int,input().split()))

if __name__ == "__main__":
 
    count = 0
    
    for i in a:
        if i <= h:
            count += 1
        else:
            count += 2
        
    print(count)
# https://codeforces.com/problemset/problem/677/A
