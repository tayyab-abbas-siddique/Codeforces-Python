a = input()
b = input()

if __name__ == "__main__":
    a = a.lower()
    b = b.lower()

    if a < b:
        print("-1")
    elif a > b:
        print("1")
    else:
        print("0")

# https://www.codeforces/problemset/problem/112A/
