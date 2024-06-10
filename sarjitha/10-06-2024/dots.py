#4. A scatter plot with 1000 dots
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random data points for x and y
x = np.random.rand(1000)
y = np.random.rand(1000)

# Create a scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot with 1000 Dots')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
