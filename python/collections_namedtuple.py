from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input())
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print(sum(marks)/len(marks))
