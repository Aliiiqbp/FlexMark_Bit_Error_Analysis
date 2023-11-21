import pandas as pd
import re

file_name = 'dropout-256'

# Read the text file
file_path = file_name + '.txt'  # Replace with the actual path to your file
with open(file_path, 'r') as file:
    file_content = file.read()

# Define a function to extract information from the text
def extract_info(text):
    experiments = re.findall(r'message: tensor\(([^)]+)\)\nextracted: tensor\(([^)]+)\)', text)
    data = {
        'message': [],
        'extracted': [],
        'bit_flips_index': [],
        'num_bit_flips': []
    }
    for msg, ext in experiments:
        message_list = [int(bit) for bit in re.findall(r'\d+', msg)[:-2]]
        extracted_list = [int(bit) for bit in re.findall(r'\d+', ext)[:-2]]
        bit_flips = [i for i, (m, e) in enumerate(zip(message_list, extracted_list)) if m != e]
        num_bit_flips = len(bit_flips)

        data['message'].append(message_list)
        data['extracted'].append(extracted_list)
        data['bit_flips_index'].append(bit_flips)
        data['num_bit_flips'].append(num_bit_flips)

    return data

# Create a DataFrame
data = extract_info(file_content)
df = pd.DataFrame(data)

# Add an index column
df['Index'] = df.index

# Reorder columns
df = df[['Index', 'message', 'extracted', 'bit_flips_index', 'num_bit_flips']]

# Save to CSV
csv_path = file_name + '.csv'  # Replace with the desired output path
df.to_csv(csv_path, index=False)

# Display the DataFrame
print(df['message'])
print(df['extracted'])
print(df['bit_flips_index'])
print(df['num_bit_flips'].describe())
