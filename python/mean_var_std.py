import numpy

n = list(map(int, input().split()))
list1 = []
for _ in range(n[0]):
    list1.append(list(map(int, input().split())))
my_array = numpy.array(list1)
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(round(numpy.std(my_array, axis=None), 11))
