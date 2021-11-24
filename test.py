

from collections import deque

class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    # Reduce p
    reducedP = []
    foundStar = False
    for pChar in p:
      if pChar == '*':
        foundStar = True
      else:
        if foundStar:
          reducedP.append('*')
          foundStar = False
        reducedP.append(pChar)
    if foundStar:
      reducedP.append('*')
    p = ''.join(reducedP)

    if len(p) == 1 and p[0] == '*':
      return True

    dq = deque()
    seen = set()
  
    if s[0] == p[0] or p[0] == '?':
      if not (1, 1) in seen:
        dq.append((1, 1))
      seen.add((1, 1))
    elif p[0] == '*':
      # for j in range(i, len(s)-len(p)+1):
      for j in range(len(s) + 1):
        spPair = (j, 1)
        if not spPair in seen:
          dq.append(spPair)
        seen.add(spPair)
    
    while dq:
      leftmost = dq.popleft()
      startSIdx, startPIdx = leftmost[0], leftmost[1]

      pIdx = startPIdx
      sIdx = startSIdx
      while pIdx < len(p) and sIdx < len(s):
        if p[pIdx] == '*':
          for sTempIdx in range(sIdx + 1, len(s) + 1):
            spPair = (sTempIdx, pIdx + 1)
            if not spPair in seen:
              dq.append(spPair)
            seen.add(spPair)
        elif (p[pIdx] != s[sIdx] and p[pIdx] != '?'):
          break

        pIdx += 1
        sIdx += 1

      if sIdx == len(s) and pIdx == len(p):
        return True
    return False
  
sol = Solution()

# x = sol.isMatch('ab', 'ab**')
# print(x)

x = sol.isMatch('aa', '*')
print(x)

# x = sol.isMatch('cb', '?a')
# print(x)

x = sol.isMatch('adceb', '*a*b')
print(x)

x = sol.isMatch('acdcb', 'a*c?b')
print(x)

x = sol.isMatch('aa', 'a')
print(x)

x = sol.isMatch('', '***********')
print(x)
