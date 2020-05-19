#link - https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true


from itertools import permutations

str, r = input().split()
perm = (list(permutations(sorted(str), int(r))))

for each in perm:
    print("".join(each))