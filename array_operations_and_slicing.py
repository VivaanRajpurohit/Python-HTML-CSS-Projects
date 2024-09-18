import numpy as np

# Initial temperatures array
temperatures = np.array([18, 19, 20, 21, 22, 23, 24])

# Increase each temperature by 5 degrees
temperatures += 5
print("Temperatures increased by 5 degrees:")
print(temperatures)

# Extract mid-week temperatures
mid_week_temps = temperatures[1:4]
print("Mid-week temperatures:")
print(mid_week_temps)

# Calculate the average of mid-week temperatures
average_temp = np.mean(mid_week_temps)
print("Average mid-week temperature:")
print(average_temp)
