import pandas as pd

def expand_list_column(df, list_column):
    # Create dummy variables for each unique value in the lists
    dummy_df = pd.get_dummies(df[list_column].apply(pd.Series).stack(), prefix=list_column, prefix_sep='-').sum(level=0)

    # Concatenate the dummy variables with the original DataFrame
    df_expanded = pd.concat([df, dummy_df], axis=1)

    # Fill NaN values with 0
    df_expanded = df_expanded.fillna(0)

    # Convert columns to integers
    df_expanded = df_expanded.astype(int)

    return df_expanded

# Example usage:
# Assuming you have a pandas DataFrame named 'df' and a column 'bit_flips_index_8'
# Replace this with your actual DataFrame and column name
# df_expanded = expand_list_column(df, 'bit_flips_index_8')