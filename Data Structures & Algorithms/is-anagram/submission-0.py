class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        contador = {}
        
        for i in range(len(s)):
            contador[s[i]] = contador.get(s[i], 0) + 1
            contador[t[i]] = contador.get(t[i], 0) - 1
            
        for cantidad in contador.values():
            if cantidad != 0:
                return False
                
        return True