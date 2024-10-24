import pandas as pd
import matplotlib.pyplot as plt
from verispy import VERIS

# Creates a bar graph for each month of the type of action for each attack separately 

data_dir = "/Users/kiranmahn/GitHub/VCDB/data/json/validated"  # replace with your own address for data
v = VERIS(json_dir=data_dir)

print(v.schema_url)

# Convert JSON to DataFrame and address fragmentation issue
veris_df = v.json_to_df(verbose=True)

# Optionally de-fragment the DataFrame if needed
veris_df = veris_df.copy()

# Use 'plus.timeline.notification.month' to get the month
veris_df['month'] = veris_df['timeline.incident.month']

# Find all columns that start with 'action.'
action_columns = [col for col in veris_df.columns if col.startswith('action.') and '.variety' not in col]

# Convert relevant action columns to numeric, ignoring non-numeric values
for col in action_columns:
    veris_df[col] = pd.to_numeric(veris_df[col], errors='coerce')

# Define month names
month_names = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Define colors to be used for the bars
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
    "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

# Loop through each month and create separate bar graphs
for month in range(1, 13):
    # Filter data for the current month
    monthly_data = veris_df[veris_df['month'] == month]

    # Sum across the 'action.' columns for the current month
    action_counts = monthly_data[action_columns].sum()

    # Filter out actions with a count of 20 or less
    action_counts = action_counts[action_counts > 20]

    # Extract the last word after the last dot for x-axis labels
    labels = [col.split('.')[-1] for col in action_counts.index]

    # Create a new figure for each month
    plt.figure(figsize=(10, 6))

    # Create a bar graph if there's data for that month
    if not action_counts.empty:
        # Use the color list cyclically to color bars
        bar_colors = [colors[i % len(colors)] for i in range(len(labels))]

        plt.bar(labels, action_counts, color=bar_colors)
        plt.title(month_names[month - 1])  # Set title using month name
        plt.xlabel("Attack Type")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
    else:
        plt.title(month_names[month - 1])
        plt.text(0.5, 0.5, 'No Data Available', ha='center', va='center', fontsize=15)

    # Set y-axis limit based on max action counts if needed
    plt.ylim(0, action_counts.max() + 1)  # Adjust y-limit to max count

    # Show the plot
    plt.tight_layout()
    plt.show()
