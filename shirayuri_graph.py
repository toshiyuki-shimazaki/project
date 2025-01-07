import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    "Japanese Literature", 
    "French Literature", 
    "English Literature", 
    "Children's Culture", 
    "Developmental Psychology", 
    "Elementary Education"
]
years = ["2020", "2021", "2022", "2023", "2024"]
data = [
    [109, 88, 80, 55, 49],  # Japanese Literature
    [103, 79, 52, 53, 34],  # French Literature
    [100, 106, 50, 55, 52], # English Literature
    [53, 62, 67, 63, 50],   # Children's Culture
    [49, 70, 56, 70, 64],   # Developmental Psychology
    [74, 72, 59, 69, 46],   # Elementary Education
]

# Create bar graph
x = np.arange(len(years))  # Index for years
width = 0.15  # Width of each bar
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each category as bars
for i, category in enumerate(categories):
    ax.bar(x + i * width, data[i], width, label=category)

# Configure the graph
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Students", fontsize=12)
ax.set_title("Enrollment Trends", fontsize=14)
ax.set_xticks(x + width * (len(categories) - 1) / 2)
ax.set_xticklabels(years)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Display the graph
plt.tight_layout()
plt.show()
