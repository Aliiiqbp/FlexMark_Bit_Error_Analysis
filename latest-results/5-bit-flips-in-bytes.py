import pandas as pd
import ast
import seaborn as sns
import matplotlib.pyplot as plt
from ast import literal_eval



file_name_list = ['compression-16', "compression-64", "compression-256",
                  "gaussian-16", "gaussian-64", "gaussian-256",
                  "gaussian-blur-16", "gaussian-blur-64", "gaussian-blur-256"]


def create_count_columns(df, source_column):
    # Extract unique values from the source column
    # Convert string representations of lists to actual lists
    df[source_column] = df[source_column].apply(literal_eval)
    unique_values = set(value for sublist in df[source_column] for value in sublist)

    # Create new columns based on unique values
    for value in unique_values:
        new_column_name = f"{source_column}_count_byte_{value}"
        df[new_column_name] = df[source_column].apply(lambda x: x.count(value) if value in x else 0)

    return df

# Example usage:
# Assuming you have a pandas DataFrame named 'df' and a column 'bit_flips_index_8'
# Replace this with your actual DataFrame and column name

for file_name in file_name_list:
    # Read the CSV file
    csv_path = file_name + '-chunk-8.csv'  # Replace with the actual path to your CSV file
    df = pd.read_csv(csv_path, converters={'bit_flips_index': ast.literal_eval})

    df_expanded = create_count_columns(df, 'bit_flips_index_8')
    df_expanded.to_csv(file_name + "bit-errors-in-bytes.csv")


    byte_columns = [col for col in df_expanded.columns if 'byte' in col]

    # Concatenate values from selected columns into a single series
    combined_series = pd.concat([df_expanded[col] for col in byte_columns], ignore_index=True)

    # Count unique values in the combined series
    unique_values_counts = combined_series.value_counts()

    # Plot the result in a histogram
    unique_values_counts.plot(kind='bar', alpha=0.9)
    plt.xlabel('Unique Values')
    plt.ylabel('Count')
    plt.title(file_name)
    plt.savefig(file_name + "-count-bit-errors-in-bytes.png")
    plt.show()









