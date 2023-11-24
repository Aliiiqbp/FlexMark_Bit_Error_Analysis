import pandas as pd
import matplotlib.pyplot as plt
import ast

from scipy.interpolate import make_interp_spline, BSpline

file_name = 'compression-16'

# Replace 'your_file.csv' with the actual path to your CSV file
df = pd.read_csv(file_name + '.csv')

# Replace 'bit_flips_index' with your actual column name
bit_flips_column = df['bit_flips_index']

# Convert string representations to actual lists
bit_flips_column = bit_flips_column.apply(ast.literal_eval)

# Combine all error indexes into a single list
all_indexes = [index for sublist in bit_flips_column for index in sublist]

# Create a pandas Series from the combined list
index_series = pd.Series(all_indexes)

# Calculate frequencies
index_frequencies = index_series.value_counts(normalize=True).sort_index()

# Increase the size of the figure
plt.figure(figsize=(15, 6))

# Plot the distribution
index_frequencies.plot(kind='bar', xlabel='Index', ylabel='Frequency', title='Error Distribution by Index')
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Save the output image

plt.savefig(file_name + '.png')

plt.show()





# # Smooth the line plot
# x_smooth = pd.Series(index_frequencies.index).sort_values()
# y_smooth = make_interp_spline(index_frequencies.index, index_frequencies.values)(x_smooth)
#
# # Plot the smoothed line
# plt.plot(x_smooth, y_smooth, marker='o')
# plt.xlabel('Index')
# plt.ylabel('Frequency')
# plt.title('Smoothed Error Distribution by Index')
# plt.show()