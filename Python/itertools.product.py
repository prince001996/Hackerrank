#link - https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

cart_prod = list(product(a,b))

for each in cart_prod:
    print(each, end=' ')
