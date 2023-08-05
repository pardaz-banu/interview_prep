def palindrome(st):
    if len(st) < 1:
        return True
    if st[0] == st[-1]:
        return palindrome(st[1:-1])
    return False
    
st = input()
print(palindrome(st))
