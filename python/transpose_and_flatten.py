import numpy

n1, n2 = map(int, input().split())

l = []
for i in range(n1):
    l.append(list(map(int, input().split())))

myarr = numpy.array(l)

print(numpy.transpose(l))
print(myarr.flatten())
