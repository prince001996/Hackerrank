#link - https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

n = int(input())
arr = [x for x in input().split()]
k = int(input())

combi = list(combinations(arr, k))

total = len(combi)

count = [1 for each in combi if 'a' in each]
print(len(count)/total)