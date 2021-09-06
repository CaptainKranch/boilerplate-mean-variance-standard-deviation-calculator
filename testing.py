import numpy as np
list = np.array([0,1,2,3,4,5,6,7,8])

# print(list[3:6])

var2 = []
var2 = np.array(var2)


var = np.append(var2, list[:3])
var3 = np.insert(var, list[3:6], axis = 2)
print(var3)



# var = np.array([1,2,3],[4,4,4])
# print(var)
