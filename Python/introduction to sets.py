#link - https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
#name - introduction to sets
def average(array):
    arr = set(array)
    size = len(arr)
    return (sum(arr)/size)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)