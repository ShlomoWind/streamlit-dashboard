import numpy as np
#1
matrix1 = np.random.randint(0, 100, size=(5, 5))
print(matrix1)
print(np.argmax(matrix1, axis=1))

#2
matrix2 = np.random.randint(0,100,size=(5,5))
print(matrix2)
print(np.argmin(matrix2,axis=1))

#3
matrix3 = np.random.randint(0,100,size=(4,4))
print(matrix3)
temp = matrix3[0].copy()
matrix3[0] = matrix3[3]
matrix3[3] = temp
print(matrix3)

#4
matrix4 = np.random.randint(0,100,size=(4,4))
print(matrix4)
print("==")
print(np.rot90(matrix4))

#5
matrix5 = np.random.randint(0,100,size=(4,4))
print(matrix5)
shift_arr = np.array([np.roll(row,1)for row in matrix5])
print("====")
print(shift_arr)

#6
matrix6 = np.random.randint(0,100,size=(4,4))
print(matrix6)
sh_arr = np.array([np.roll(matrix6,shift=1,axis=0)])
print("==")
print(sh_arr)