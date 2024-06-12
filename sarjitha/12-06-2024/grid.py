import matplotlib.pylab as plt
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,3,4,5,7]
plt.plot(x,y1,linestyle='-',color='b',linewidth=3,marker='o',markerfacecolor='1')
plt.plot(x,y2,linestyle='--',color='r',linewidth=3,marker='x',markerfacecolor='1')
plt.title("line plot wit grid")
plt.xlabel("x=axis")
plt.ylabel("y=axis")
plt.legend()

plt.grid(True)
plt.grid(color='grey',linestyle='--',linewidth='1')
plt.show()
