#This is a Python Program to determine how many times a given letter occurs in a string recursively.
def count_char(st, ch):
    if not st:
        return 0
    if st[0] == ch:
        return 1 + count_char(st[1:],ch)
    else:
        return count_char(st[1:],ch)

st = input()
character = input()
print(character + " occourred " + str(count_char(st, character)) +" times.")
