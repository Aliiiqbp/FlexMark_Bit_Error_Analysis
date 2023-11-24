import pandas as pd
import ast

file_name = 'compression-64'
chunk_size = 4

# Read the CSV file
csv_path = file_name + '.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_path, converters={'bit_flips_index': ast.literal_eval})

# Function to perform the required operations on "bit_flips_index"
def process_bit_flips_index(bit_flips_index):
    # Divide each value by 8 using integer division (//), convert to set, and calculate the length
    bit_flips_index_8 = set([i // chunk_size for i in bit_flips_index])
    # bit_flips_index_8 = [i // chunk_size for i in bit_flips_index]
    num_chunk_flips = len(bit_flips_index_8)
    return bit_flips_index_8, num_chunk_flips

# Apply the function to create new columns
df[['bit_flips_index_' + str(chunk_size), 'num_chunk_flips']] = df['bit_flips_index'].apply(process_bit_flips_index).apply(pd.Series)

# Save the updated DataFrame to a new CSV file
output_csv_path = file_name + '-chunk-' + str(chunk_size) + '.csv'  # Replace with the desired output path
df.to_csv(output_csv_path, index=False)

# Display the updated DataFrame
print(df['num_chunk_flips'].describe())
