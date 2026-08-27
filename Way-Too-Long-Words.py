# You will given a string in input.
# If the length of the string is greater than 10, you have to print it's first letter then length of the input minus 2 then last letter of word (without spaces).
# Else print the input exactly.

word = input()

if len(word) > 10:
    print(word[0]+str(len(word)-2)+word[-1])
else:
    print(word)
