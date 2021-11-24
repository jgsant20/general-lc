""" Regex Search Algorithm

1. Function exact_match(text, query) returns true if query is an exact substring of text.
  - Multiple ways to approach this, but just write the most straightforward solution
  - You could also learn the KMP algorithm to make this super fast, but honestly, I don't think the interviewer would expect it.

"""
from test_helper import run_bulk_tests
from collections import Counter


def exact_match_straightforward(text, query):
  """
  Straight forward solution, you'd think is really slow, but it's actually the second fastest
  """
  for i in range(len(text) - len(query) + 1):
    if text[i:i + len(query)] == query:
      return True
  return False

def exact_match_super_slow_lmao(text, query):
  """
  This is a terribly slow solution. Don't use it LOL
  """
  left = 0
  queryCounter = Counter(query)
  matchedLetters = 0

  for right in range(len(text)):
    rightChar = text[right]

    # Add to matchedLetters!
    if rightChar in queryCounter:
      queryCounter[rightChar] -= 1
      if queryCounter[rightChar] == 0:
        matchedLetters += 1

    if right >= len(query) - 1:
      if matchedLetters == len(queryCounter) and text[left:left + len(query)] == query:
        return True

      leftChar = text[left]
      # Subtract from matchedLetters!
      if leftChar in queryCounter:
        if queryCounter[leftChar] == 0:
          matchedLetters -= 1
        queryCounter[leftChar] += 1

      left += 1
  
  return False

def exact_match_probably_what_they_want(text: str, query: str) -> int:
  for i in range(len(text) - len(query) + 1):
    if text[i] == query[0] and text[i:i + len(query)] == query:
      return True
  return False

def exact_match_slight_improvement_maybe(text: str, query: str) -> int:
  def check_if_match_at_idx(idx):
    for i in range(idx, idx + len(query)):
      if text[i] != query[i - idx]:
        return False
    return True

  for i in range(len(text) - len(query) + 1):
    if text[i] == query[0] and check_if_match_at_idx(i):
      return True
  return False

def exact_match_easiest_and_fastest(text: str, query: str) -> int:
  """
  Literally the fastest.
  """
  try:
    text.index(query)
    return True  
  except Exception:
    return False

if __name__ == '__main__':
  run_bulk_tests([exact_match_straightforward, exact_match_super_slow_lmao, exact_match_probably_what_they_want, exact_match_easiest_and_fastest, exact_match_slight_improvement_maybe], [
    [("abcdefg", "abc"), True],
    [("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab","ab"), True]
  ])
