n = int(input())
s = input()

if __name__ == "__main__":
    count = 0
    
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            count += 1
        
    print(count)    

# https://codeforces.com/problemset/problem/266/A
