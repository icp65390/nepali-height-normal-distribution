import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load dataset
data = pd.read_csv("data/nepali_height_data.csv")
heights = data["height_cm"]

# Calculate mean and standard deviation
mean_height = heights.mean()
std_height = heights.std()

# Generate x values
x = np.linspace(heights.min(), heights.max(), 100)

# Normal distribution curve
y = norm.pdf(x, mean_height, std_height)

# Plot
plt.figure(figsize=(8, 5))
plt.hist(heights, bins=10, density=True, alpha=0.6)
plt.plot(x, y)

plt.title("Normal Distribution of Height of Nepali People")
plt.xlabel("Height (cm)")
plt.ylabel("Density")

plt.show()

