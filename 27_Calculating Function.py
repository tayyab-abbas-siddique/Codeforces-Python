def alternating_sum(n):
    if n % 2 == 0:
        return n // 2
    return -(n + 1) // 2
 
if __name__ == "__main__":
    n = int(input())
    print(alternating_sum(n))
# https://codeforces.com/problemset/problem/486/A
