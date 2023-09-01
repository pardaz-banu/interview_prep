#python program to find if the string is unique or not without using data structure
def check(s):
    res = ""
    for i in range(len(s)):
        if s[i] not in res:
            res += s[i]
        else:
            return False
    return True

s = input("Enter the string: ")
print(check(s))
