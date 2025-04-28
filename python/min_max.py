import numpy

n = list(map(int, input().split()))
list1 = []
for _ in range(n[0]):
    list1.append(list(map(int, input().split())))
my_array = numpy.array(list1)
print(numpy.max(numpy.array(numpy.min(my_array, axis=1))))
