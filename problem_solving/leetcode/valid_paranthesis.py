
class Solution(object):
    def isValid(self, s):
        d = dict(('()','{}','[]'))
        st = []
        for i in range(len(s)):
            if s[i] in '[({':
                st.append(s[i])
                #print(st)
            elif len(st) == 0 or s[i] != d[st.pop()]:
                return False
        return len(st) == 0
