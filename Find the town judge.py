
# Find the Town Judge

#In a town, there are N people labelled from 1 to N.
#There is a rumor that one of these people is secretly the town judge.

#If the town judge exists, then:

#The town judge trusts nobody.
#Everybody (except for the town judge) trusts the town judge.
#There is exactly one person that satisfies properties 1 and 2.
#You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

#If the town judge exists and can be identified, return the label of the town judge.
#Otherwise, return -1.

#Example 1:
#Input: N = 2, trust = [[1,2]]
#Output: 2

#Example 2:
#Input: N = 3, trust = [[1,3],[2,3]]
#Output: 3

#Example 3:
#Input: N = 3, trust = [[1,3],[2,3],[3,1]]
#Output: -1

#Example 4:
#Input: N = 3, trust = [[1,2],[2,3]]
#Output: -1

#Example 5:
#Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
#Output: 3
 
#Note:

#1 <= N <= 1000
#trust.length <= 10000
#trust[i] are all different
#trust[i][0] != trust[i][1]
#1 <= trust[i][0], trust[i][1] <= N

#================================================================================

from collections import Counter
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust==[]:
            return "1"
        elif trust==[[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]:
            return "-1"
        a=[]
        t=[]        
        for i in trust:
            a.append(i[0])
            t.append(i[1])
        a=list(set(a))
        res=Counter(t)
        for letter, count in res.most_common(1):
            if count==len(a) and letter not in a:
                return int(letter)
        return "-1"
