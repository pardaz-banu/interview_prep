def palindrome(st):
    if len(st) < 1:
        return True
    if st[0] == st[-1]:
        return palindrome(st[1:-1])
    return False
    
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
for i in range(lower_limit, upper_limit):
    if i%2 == 1:
        if palindrome(str(i)):
            print(i)

        
