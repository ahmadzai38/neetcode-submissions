class Solution:
    def isPalindrome(self, s: str) -> bool:
        hset = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"}
        result = [] 

        for i in range(len(s)):
            if s[i] not in hset:
                continue
            #if s[i] != " " and s[i] != "?":
            result.append(s[i].lower())

        res = []

        for n in range(len(s) - 1, -1, -1):
            if s[n] not in hset:
                continue 
            #if s[n] != " " and s[n] != "?":
            res.append(s[n].lower()) 

        return result == res