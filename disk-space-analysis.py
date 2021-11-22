""" Question: Find the minima of all subsets of size n.

Example:
space = [8, 2, 4, 6]
x = 2


Approach:
- Use a deque

"""

from collections import deque

def diskSpaceAnalysis(space, x):
  res = []
  dq = deque()
  l, r = 0, 0

  while r < len(space):

    while dq and space[dq[-1]] > space[r]:
      dq.pop()
    dq.append(r)

    if l > dq[0]:
      dq.popleft()

    if (r + 1) >= x:
      res.append(space[dq[0]])
      l += 1
    r += 1

  return res

res = diskSpaceAnalysis([8, 2, 4, 6], 2)
print(res)
