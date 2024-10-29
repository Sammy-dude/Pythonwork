import matplotlib.pyplot as plt

# X and Y data
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 8, 27, 64]
y3 = [0, 2, 4, 6, 8]
# plt.figure(figsize=(4, 4))
# Plot with named color
plt.plot(x, y1, color='red', label='Named color')

# Plot with hexadecimal color
plt.plot(x, y2, color='#00FF00', label='Hex color')

# Plot with RGB tuple
plt.plot(x, y3, color=(0, 0, 1), label='RGB tuple')

# plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Different Color Types in Matplotlib')

# Show the plot
plt.show()
