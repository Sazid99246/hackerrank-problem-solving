import numpy as np
a1 = [*map(int, input().split())] 
a1 = np.array(a1)
print(np.reshape(a1, (3, 3)))
