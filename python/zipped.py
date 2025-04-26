n, x = map(int, input().split())
data = [list(map(float, input().split())) for _ in range(x)]
students = zip(*data)
for student in students:
    print(sum(student) / x)
