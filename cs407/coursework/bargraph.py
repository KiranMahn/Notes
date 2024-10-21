import pandas as pd
import matplotlib.pyplot as plt
from verispy import VERIS

# Creates a bar graph of all the number of varieties of attack errors

data_dir = "/Users/kiranmahn/GitHub/VCDB/data/json/validated"  # replace with your own address for data
v = VERIS(json_dir=data_dir)

print(v.schema_url)

# Convert JSON to DataFrame and address fragmentation issue
veris_df = v.json_to_df(verbose=True)

# Optionally de-fragment the DataFrame if needed
veris_df = veris_df.copy()

# Find all columns that start with 'action.error.variety.'
error_variety_columns = [col for col in veris_df.columns if col.startswith('action.error.variety.')]

# Sum across these columns to get the total count of each variety
error_variety_counts = veris_df[error_variety_columns].sum()

# Extract the last word after the last dot for x-axis labels
labels = [col.split('.')[-1] for col in error_variety_columns]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(labels, error_variety_counts, color='skyblue')

# Set title and labels
plt.title("Counts of Action Error Varieties")
plt.xlabel("Action Error Variety")
plt.ylabel("Count")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the graph
plt.tight_layout()
plt.show()
