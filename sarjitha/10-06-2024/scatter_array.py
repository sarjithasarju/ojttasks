#3. Use the scatter() method to draw a scatter plot diagramimport matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Example data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
