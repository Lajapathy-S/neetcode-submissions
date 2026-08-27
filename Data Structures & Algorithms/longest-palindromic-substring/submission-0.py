class Solution:
    def longestPalindrome(self, s: str) -> str:
        resindex = 0
        reslen = 0

        
        for i in range(len(s)):
            #foroddlength
            l,r = i,i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    resindex = l
                    reslen = r-l+1

                l = l -1 
                r = r+1
            #foroddlength
            l,r = i,i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    resindex = l
                    reslen = r-l+1

                l = l -1 
                r = r+1
        return s[resindex:reslen+resindex]

            

                