''' Problem statement: 
Implement a method to perform a basic string compression by counting the repeated characters. And if the compressed string is not less than the 
original string then return original string otherwise return compressed string
Input: "aabcccaad"
Output: "aabcccaad"
Input: "aabbbbbcccddd"
Output: "a2b6c3d3"

Time complexity for the code I implemented is O(n)
Space complexity is O(1)
'''
def stringCompressed(s):
    res = ""
    c = 0
    for i in range(len(s)):
        c += 1
        if i+1 >= len(s) or s[i+1] != s[i]:
            res += s[i]+str(c)
            c = 0
    if len(res) < len(s):
        return res
    return s
    

s = input("Enter the string: ")
print(stringCompressed(s))
