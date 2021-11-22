""" Regex Search Algorithm

1. Function exact_match(text, query) returns true if query is an exact substring of text.
  - Multiple ways to approach this, but just write the most straightforward solution
  - You could also learn the KMP algorithm to make this super fast, but honestly, I don't think the interviewer would expect it.
2. Function wildcard_match(text, query) adds the wildcard metacharacter '.' to query, matching any character in text

"""
import time
from collections import Counter

def time_to_ns(time):
  return time * 1000000

def run_tests(func, tests):
  print(f'Running tests for {func.__name__}():')
  total_times = []
  for i, (inputs, expected_res) in enumerate(tests):
    start_time = time.time()
    res = func(*inputs)
    time_ran = time_to_ns(time.time() - start_time)
    total_times.append(time_ran)

    if res == expected_res:
      print(f'  Test #{i + 1} ran for{time_ran : .3f}ns with inputs {inputs} and expected result {expected_res} successful!')
    else:
      print(f'  Test #{i + 1} ran for{time_ran : .3f}ns with inputs {inputs} mismatch {res} != expected result {expected_res}')

  print(f'  function ran on average:{sum(total_times) / len(total_times) : .3f}ns')
  print()

def run_bulk_tests(funcs, tests):
  for func in funcs:
    run_tests(func, tests)

def exact_match_slow(text, query):
  """
  Straight forward solution, you'f think is really slow, but it's actually the second fastest
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

def exact_match_easiest_and_fastest(text: str, query: str) -> int:
  """
  Literally the fastest.
  """
  try:
    return text.index(query)
  except Exception:
    return -1

run_bulk_tests([exact_match_slow, exact_match_super_slow_lmao, exact_match_probably_what_they_want, exact_match_easiest_and_fastest], [
  [("abcdefg", "abc"), True],
  [("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab","ab"), True]
])

def 