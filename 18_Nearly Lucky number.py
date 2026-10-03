a = int(input())
b = [int(c) for c in str(a)]

if __name__ == "__main__":
    c4 = b.count(4)
    c7 = b.count(7)
    
    if c4 + c7 == 4 or c4 + c7 == 7:
        print("YES")
    else:
        print("NO")

      
# https://www.codeforces.com/problemset/problem/110/A
