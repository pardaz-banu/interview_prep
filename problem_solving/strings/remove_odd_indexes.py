#The program takes a string and removes the characters of odd index values in the string.
st = input()
result = ""
for i in range(len(st)):
    if i%2 == 0:
        result += st[i]
print("The string after removing odd index characters is ", result)
