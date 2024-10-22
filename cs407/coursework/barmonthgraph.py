import pandas as pd
import matplotlib.pyplot as plt
from verispy import VERIS

data_dir = "/Users/kiranmahn/GitHub/VCDB/data/json/validated"  # replace with your own address for data
v = VERIS(json_dir=data_dir)

print(v.schema_url)

# Convert JSON to DataFrame and address fragmentation issue
veris_df = v.json_to_df(verbose=True)

# Optionally de-fragment the DataFrame if needed
veris_df = veris_df.copy()

# Use 'plus.timeline.notification.month' to get the month
veris_df['month'] = veris_df['timeline.incident.month']

# Find all columns that start with 'action.error.variety.'
error_variety_columns = [col for col in veris_df.columns if col.startswith('action.variety.')]

# Define month names
month_names = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Define a list of colors to use for the bars (cyclically)
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
    "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

# Determine the maximum y value across all months to set a common y-axis limit
max_y_value = 0
for month in range(1, 13):
    monthly_data = veris_df[veris_df['month'] == month]
    error_variety_counts = monthly_data[error_variety_columns].sum()
    if error_variety_counts.max() > max_y_value:
        max_y_value = error_variety_counts.max()

# Set up a figure with 3 rows and 4 columns to fit 12 graphs
fig, axes = plt.subplots(3, 4, figsize=(20, 15))

# Loop through each month and create a bar graph
for month in range(1, 13):
    # Filter data for the current month
    monthly_data = veris_df[veris_df['month'] == month]

    # Sum across the 'action.error.variety.' columns for the current month
    error_variety_counts = monthly_data[error_variety_columns].sum()

    # Extract the last word after the last dot for x-axis labels
    labels = [col.split('.')[-1] for col in error_variety_columns]

    # Select the appropriate subplot (axes) based on the month index
    ax = axes[(month - 1) // 4, (month - 1) % 4]

    # Create a bar graph if there's data for that month
    if not error_variety_counts.empty:
        # Use the color list cyclically to color bars
        bar_colors = [colors[i % len(colors)] for i in range(len(labels))]
        
        ax.bar(labels, error_variety_counts, color=bar_colors)
        ax.set_title(month_names[month - 1])  # Set title using month name
        ax.set_xlabel("Action Error Variety")
        ax.set_ylabel("Count")
        ax.set_xticklabels(labels, rotation=45, ha='right')
        ax.set_ylim(0, max_y_value)  # Set y-axis range to the determined maximum
    else:
        # If no data, show a blank subplot with title
        ax.set_title(month_names[month - 1])
        ax.axis('off')

# Adjust layout and spacing
plt.tight_layout()
plt.show()
