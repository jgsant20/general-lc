""" Regex Search Algorithm

2. Function wildcard_match(text, query) adds the wildcard metacharacter '.' to query, matching any character in text
- I can only think of one way to approach this solution.

"""
from test_helper import run_bulk_tests

def wildcard_match_straightforward(text, query):
  def check_matching_at_idx(start_idx):
    for idx in range(start_idx, start_idx + len(query)):
      if text[idx] != query[idx - start_idx] and query[idx - start_idx] != '*':
        return False
    return True

  for i in range(len(text) - len(query) + 1):
    if check_matching_at_idx(i):
      return True
  return False

if __name__ == '__main__':
  run_bulk_tests([wildcard_match_straightforward], [
    [("aDcdefg", "a*c"), True],
    [("defgadc", "a*c"), True],
  ])
