x=10
learning_rate=0.1
num_iteration=100
for i in range(num_iteration):
    gradient=2 * x
    x=x-learning_rate*gradient
print(f"minimum value of the x:{x}")