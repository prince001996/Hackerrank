#link - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

def takeSecond(elem):
    return elem[1]
if __name__ == '__main__':
    report = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in report:
            report[score].append(name)
        else:
            report[score]=[name]

    mark = sorted(report)[1]

    students = report[mark]

    for each in sorted(students):
        print(each)