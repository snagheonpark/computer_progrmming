import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='temperature')

plt.title('Daily temperature trend')
plt.xlabel('Time (hour)')  # Added a missing parenthesis
plt.ylabel('Temperature (°C)')  # Corrected the degree symbol

plt.legend()
plt.grid(True)
plt.show()
