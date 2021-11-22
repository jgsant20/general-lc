"""
Basically implement the .index() string method
"""

class Solution:
    def strStr(self, haystack, needle):
        freqDict = {}
        for n in needle:
            if not n in freqDict:
                freqDict[n] = 0
            freqDict[n] += 1
            
        matchingChars = 0    
        lptr = 0
        for rptr in range(len(haystack)):
            rptrChar = haystack[rptr]
            if rptrChar in freqDict:
                freqDict[rptrChar] -= 1
                if freqDict[rptrChar] == 0:
                    matchingChars += 1

            print(lptr, rptr, matchingChars, freqDict, rptrChar)
            
            if rptr >= len(needle) -1:
                if matchingChars == len(freqDict) and needle == haystack[lptr:rptr + 1]:
                    return lptr 
                
                lptrChar = haystack[lptr]
                if lptrChar in freqDict:
                    if freqDict[lptrChar] == 0:
                        matchingChars -= 1
                    freqDict[lptrChar] += 1
                
                lptr += 1
                
        return -1


res = Solution().strStr("mississippi", "issip")
print(res)
