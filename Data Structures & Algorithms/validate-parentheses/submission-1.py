class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        matching = {'(':')','{':'}','[':']'}
        for c in s :
            if c in matching:
                temp.append(c)
            else:
                if not temp or matching[temp.pop()] != c:
                    return False
        return len(temp) == 0


        
        
       