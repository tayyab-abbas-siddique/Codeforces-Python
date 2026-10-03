n = int(input())

if __name__ == "__main__":
    count = 1
    lst = []
    for i in range(n):
        a = int(input())
        lst.append(a)
    
    for j in range(1, len(lst)):
        if lst[j] != lst[j - 1]:
            count += 1
        else:
            count += 0
        
    print(count)
# https://codeforces.com/problemset/problem/344/A
