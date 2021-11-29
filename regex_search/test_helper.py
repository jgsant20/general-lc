import time

def time_to_ns(time):
  return time * 1000000

def run_tests(func, tests):
  print(f'Running tests for {func.__name__}():')
  total_times = []
  tests_passed = 0
  for i, (inputs, expected_res) in enumerate(tests):
    start_time = time.time()
    res = func(*inputs)
    time_ran = time_to_ns(time.time() - start_time)
    total_times.append(time_ran)

    if res == expected_res:
      print(f'  Test #{i + 1} ran for {time_ran}ns and expected result {expected_res} successful!')
      tests_passed += 1
    else:
      print(f'  Test #{i + 1} ran for {time_ran}ns mismatch {res} != expected result {expected_res}')

  print(f'  function ran on average: { sum(total_times) / len(total_times)}ns')
  print()
  if tests_passed != len(tests):
    print(f'  {tests_passed} / {len(tests)} tests passed')
  else:
    print(f'  all tests passed')
  print()

def run_bulk_tests(funcs, tests):
  for func in funcs:
    run_tests(func, tests)
