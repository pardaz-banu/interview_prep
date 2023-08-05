#a Python Program to check if the two strings are anagram.

def anagram(st1, st2):
    if len(st1) != len(st2):
        return False
    if len(st1) == 1:
        return st1 == st2
    for i in range(len(st1)):
        if st1[i] in st2:
            chars = st2[:st2.index(st1[i])]+st2[st2.index(st1[i])+1:]
            if anagram(st1[:i]+st1[i+1:], chars):
                return True
    return False

st1 = input()
st2=input()
print(anagram(st1,st2))
