import numpy as np
matrix=np.array([[19,26,3,4],
                     [5,66,7,8],
                     [9,80,11,12],
                     [13,19,15,6]])
diagnoal=np.diag(matrix)
sum_diagnoal=np.sum(diagnoal)

print ("sum of the diagnoal elements 4*4 is ",sum_diagnoal)