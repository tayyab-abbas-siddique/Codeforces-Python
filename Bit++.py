cases = int(input())
 
x = 0
 
for i in range(cases):
    word = input()
    if "X++" in word or "++X" in word:
        x = x + 1
    if "X--" in word or "--X" in word:
        x -= 1    
        
print(x)

#  https://codeforces.com/problemset/problem/282/A
