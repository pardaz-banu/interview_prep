#This is a Python Program to display which letters are in the two strings but not in both.
s1 = input()
s2 = input()
not_common = set(s1) ^ set(s2)
print("letters that are in two strings but not in both are: \n",list(not_common))
