#link - https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

from collections import Counter

n, m = [int(x) for x in input().split()]
arr = Counter([int(x) for x in input().split()])
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

score = 0
for each in arr:
    if each in A:
        score += arr[each]
    elif each in B:
        score -= arr[each]

print(score)
