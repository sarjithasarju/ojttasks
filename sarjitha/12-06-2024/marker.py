import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[2,3,4,5,6,11,12,13]

plt.plot(x,y,marker='o',linestyle='-',color='g',markersize=6,markerfacecolor='r')

plt.title("line plot wit markers")
plt.xlabel("x=axis")
plt.ylabel("y=axis")

plt.show()

