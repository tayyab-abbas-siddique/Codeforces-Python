word = input("Enter your string: ")

if __name__ == "__main__":
    if len(word) > 10:
        print(word[0] + str(len(word - 2)) + word[-1])
    else:
        print(word)



# https://codeforces.com/problemset/problem/71/A
