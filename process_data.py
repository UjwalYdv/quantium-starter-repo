import pandas as pd

# List of input files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

processed_dfs = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels (lowercase in CSV)
    df = df[df["product"] == "pink morsel"]

    # Convert price from string ($3.00) to float (3.00)
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Create sales column
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    processed_dfs.append(df)

# Combine all three CSVs into one
final_df = pd.concat(processed_dfs, ignore_index=True)

# Save output file
final_df.to_csv("output.csv", index=False)

print("Data processing complete. output.csv created.")
