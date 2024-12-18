import matplotlib.pyplot as plt

# Your data
list1 = [1 - i * 0.03 for i in range(30)]  # Decreasing from 1 towards 0
list2 = [1 + i * 0.03 for i in range(30)]  # Increasing from 1 upwards

# Create an array with the positions of each bar along the x-axis
x = range(len(list1))

# Plot bars
plt.bar(x, list1, width=0.4, align='center', color='blue', label='ti+')
plt.bar(x, list2, width=0.4, align='edge', color='red', label='tj-')

plt.xlabel('Position')
plt.ylabel('Bias')

# Adding grid
plt.grid(True, linestyle='--', alpha=0.6)

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To layout the graph properly
plt.tight_layout()

# Show the plot
plt.show()
