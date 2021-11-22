"""
https://leetcode.com/problems/the-skyline-problem/
"""

from itertools import chain
from collections import deque

class Solution:
  def getSkyline(self, buildings):
    height_points = [*chain.from_iterable(
      [
        [left, height, [id_]],
        [right, 0, [id_]],
      ]
      for id_, (left, right, height) in enumerate(buildings))
    ]

    height_points.sort(key=lambda item: (item[0], -item[1]))
    print(height_points)

    # Cleanup height_points
    i = 1
    idxs = []
    while i < len(height_points):
      if height_points[i - 1][0] == height_points[i][0]:
        idxs += height_points[i][2]
        del height_points[i]
      elif idxs:
        idxs += height_points[i - 1][2]
        height_points[i - 1][2] = idxs
        idxs = []
        i += 1
      else:
        i += 1

    if idxs:
      idxs += height_points[i - 1][2]
      height_points[i - 1][2] = idxs

    print(height_points)

    res = []
    dq = deque()  # monotonically increasing deque
    withinRange = dict()
    for x, height, id_ in height_points:
      for id in id_:
        if not id in withinRange:
          withinRange[id] = height

          while dq and not dq[0] in withinRange:
            dq.popleft()

          while dq and not withinRange[dq[-1]] > height:
            dq.pop() 
          
          dq.append(id)
        else:
          del withinRange[id]

          if dq and not dq[0] in withinRange:
            dq.popleft()

      if dq and withinRange:
        res.append([x, withinRange[dq[0]]])
      else:
        res.append([x, height])
        
    # Cleanup solution
    i = 1
    while i < len(res):
      if res[i][1] == res[i - 1][1]:
        del res[i]
      else:
        i += 1

    return res

res = Solution().getSkyline([[1,2,1],[1,2,2],[1,2,3]])
print(res)
