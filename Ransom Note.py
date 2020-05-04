
#Given an arbitrary ransom note string and another string containing letters from all the magazines,
#write a function that will return true if the ransom note can be constructed from the magazines ;
#otherwise, it will return false.

#Each letter in the magazine string can only be used once in your ransom note.

#Note:
#You may assume that both strings contain only lowercase letters.

#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true

#===============================================================================


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote=="":
            return True
        
        d=[]
        flag=0
        magazine=list(magazine)
        ransomNote=list(ransomNote)
        r=list(set(ransomNote))
        for i in range(len(r)):
            c=ransomNote.count(r[i])
            d.append(c)
        for i in range(len(d)):
            if d[i]<=magazine.count(r[i]):
                flag=1
            else:
                flag=0
                break
        if flag==1:     
            return True
        else:
            return False
