""" Regex Search Algorithm

3. Function question_wildcard_match(text, query) adds quantifier metacharacter + to query character set.
    x? in query matches either zero or one occurrence of x in text.

"""

from collections import deque
from test_helper import run_bulk_tests


def question_wildcard_match(text, query):
    class QueryCharacter:
        def __init__(self, character, type=''):
            self.character = character
            self.type = type

    class PossibleSolutionsItem:
        def __init__(self, textIdx, queryIdx):
            """We wanna check if query character at queryIdx matches text character at textIdx"""
            self.textIdx = textIdx
            self.queryIdx = queryIdx

    possibleSolutions = deque()
    seen = set()
    def addToPossibleSolutions(textIdx, queryIdx):
        if not (textIdx, queryIdx) in seen:
            possibleSolutions.append(PossibleSolutionsItem(textIdx, queryIdx))
        seen.add((textIdx, queryIdx))

    # Simplify query by merging items together so we can simply for loop through it
    # 'ab?c' --> ['a', 'b?', 'c']
    simplifyQuery = []
    for i in range(len(query) - 1):
        if query[i + 1] == '?':
            simplifyQuery.append(QueryCharacter(query[i], '?'))
        elif query[i] != '?':
            simplifyQuery.append(QueryCharacter(query[i]))

    if query[-1] != '?':
        simplifyQuery.append(QueryCharacter(query[-1]))

    for i in range(len(text)):
        if simplifyQuery[0].type == '?':
            addToPossibleSolutions(i + 1, 0)
            addToPossibleSolutions(i + 1, 1)
        elif simplifyQuery[0].character == text[i]:
            addToPossibleSolutions(i + 1, 1)

        while possibleSolutions:
            leftPossibleSolution = possibleSolutions.popleft()

            nextTextIdx = leftPossibleSolution.textIdx
            nextQueryIdx = leftPossibleSolution.queryIdx
            while nextTextIdx < len(text) and nextQueryIdx < len(simplifyQuery):
                if simplifyQuery[nextQueryIdx].type == '?':
                    addToPossibleSolutions(nextTextIdx, nextQueryIdx + 1)
                
                if simplifyQuery[nextQueryIdx].character == text[nextTextIdx]:
                    nextTextIdx += 1
                    nextQueryIdx += 1
                else:
                    break

            if nextQueryIdx == len(simplifyQuery) or nextTextIdx == len(text):
                return True
    print(seen)
    return False 

if __name__ == '__main__':
  run_bulk_tests([question_wildcard_match], [
    [("aDcdefg", "ab?c"), False],
    [("defgac", "ab?c"), True],
    [("acasdfadsfwersfgwseg", "ab?c"), True],
    [("asdasdfoefhweqifhabc", "ab?c"), True],
    [("a", "ab?c?"), True],
    [("abc", "ab?c?"), True],
  ])
