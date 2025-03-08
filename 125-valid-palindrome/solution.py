class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = 0
        e = len(s)-1
        #alphanumeric = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

        while b < e:
            #if s[b] not in alphanumeric:
            if not s[b].isalnum():
                b += 1
                continue
            #if s[e] not in alphanumeric:
            if not s[e].isalnum():
                e -= 1
                continue
            if s[b].lower() != s[e].lower():
                return False
            b += 1
            e -= 1
        return True
