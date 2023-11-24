import pandas as pd
import matplotlib.pyplot as plt
import ast

file_name = 'compression-256'

# Replace 'your_file.csv' with the actual path to your CSV file
df = pd.read_csv(file_name + '.csv')

# Replace 'bit_flips_index' with your actual column name
bit_flips_column = df['bit_flips_index']

# Convert string representations to actual lists
bit_flips_column = bit_flips_column.apply(ast.literal_eval)

# Calculate the number of errors in each row
num_errors = bit_flips_column.apply(len)

# Plot the distribution with mean and std indicators
plt.figure(figsize=(10, 6))

plt.hist(num_errors, bins=range(0, max(num_errors) + 1), edgecolor='black', alpha=0.7)
plt.axvline(num_errors.mean(), color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(num_errors.std(), color='green', linestyle='dashed', linewidth=2, label='Std Dev')

plt.xlabel('Number of Errors')
plt.ylabel('Frequency')
plt.title('Distribution of Number of Errors per sample for compression')
plt.legend()

# Save the figure
plt.savefig(file_name + 'number_of_errors_distribution.png')

plt.show()
