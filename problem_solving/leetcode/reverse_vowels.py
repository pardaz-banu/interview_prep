class Solution:
    def reverseVowels(self, s: str) -> str:
        st = ""
        #s = s.lower()
        s = list(s)
        for i in range(len(s)):
            if s[i] in 'aeiou' or s[i] in 'AEIOU':
                st+=s[i]
        st = st[::-1]
        k = 0
        #print(s)
        for i in range(len(s)):
            if s[i] in 'aeiou' or s[i] in 'AEIOU':
                s[i] = st[k]
                k += 1
        result = ""
        for i in range(len(s)):
            result+= s[i]
        return result
