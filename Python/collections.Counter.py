#link - https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

n = int(input())

shoes = Counter(input().split())

count_Cust = int(input())
amount = 0
for i in range(count_Cust):
    size, price = [int(x) for x in input().split()]
    if shoes[str(size)] > 0:
        shoes[str(size)] -=1
        amount += price

print(amount)