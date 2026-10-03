a = int(input())
b = input()

if __name__ == "__main__":
 
    ca = b.count("A")
    cd = b.count("D")
    
    if ca > cd:
        print("Anton")
    elif cd > ca:
        print("Danik")
    else:
        print("Friendship")
# https://codeforces.com/problemset/problem/734/A
