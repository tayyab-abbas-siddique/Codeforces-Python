n = int(input())
 
if __name__ == "__main__":
    lst1 = []
    lst2 = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        lst1.append(a)
        lst2.append(b)
    
    temp = 0
    ans = []
    
    for i in range(len(lst1)):
        temp -= lst1[i]
        temp += lst2[i]
        ans.append(temp)
    
    
    print(max(ans))
# https://codeforces.com/problemset/problem/116/A
