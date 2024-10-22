import pandas as pd
import matplotlib.pyplot as plt
from verispy import VERIS

# Creates a bar graph for each year, focusing only on incidents from June

data_dir = "/Users/kiranmahn/GitHub/VCDB/data/json/validated"  # replace with your own address for data
v = VERIS(json_dir=data_dir)

print(v.schema_url)

# Convert JSON to DataFrame and address fragmentation issue
veris_df = v.json_to_df(verbose=True)

# Optionally de-fragment the DataFrame if needed
veris_df = veris_df.copy()

# Use 'plus.timeline.notification.month' and 'plus.timeline.notification.year' to get month and year
veris_df['month'] = veris_df['timeline.incident.month']
veris_df['year'] = veris_df['timeline.incident.year']

# Find all columns that start with 'action.'
action_columns = [col for col in veris_df.columns if col.startswith('action.') and '.variety' not in col]

# Convert relevant action columns to numeric, ignoring non-numeric values
for col in action_columns:
    veris_df[col] = pd.to_numeric(veris_df[col], errors='coerce')

# Define colors to be used for the bars
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
    "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

# Filter data to only include incidents from June
june_data = veris_df[veris_df['month'] == 6]

# Get unique years from the filtered data
years = june_data['year'].dropna().unique()

# Loop through each year and create separate bar graphs
for year in sorted(years):
    # Filter data for the current year
    yearly_data = june_data[june_data['year'] == year]

    # Sum across the 'action.' columns for the current year
    action_counts = yearly_data[action_columns].sum()

    # Filter out actions with a count of 20 or less
    action_counts = action_counts[action_counts > 20]

    # Extract the last word after the last dot for x-axis labels
    labels = [col.split('.')[-1] for col in action_counts.index]

    # Create a new figure for each year
    plt.figure(figsize=(10, 6))

    # Create a bar graph if there's data for that year
    if not action_counts.empty:
        # Use the color list cyclically to color bars
        bar_colors = [colors[i % len(colors)] for i in range(len(labels))]

        plt.bar(labels, action_counts, color=bar_colors)
        plt.title(f"June Incidents - {year}")  # Set title using year
        plt.xlabel("Attack Type")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
    else:
        plt.title(f"June Incidents - {year}")
        plt.text(0.5, 0.5, 'No Data Available', ha='center', va='center', fontsize=15)

    # Set y-axis limit based on max action counts if needed
    plt.ylim(0, action_counts.max() + 1)  # Adjust y-limit to max count

    # Show the plot
    plt.tight_layout()
    plt.show()
