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
veris_df['month'] = veris_df['plus.timeline.notification.month']

# Find all columns that start with 'action.'
action_columns = [col for col in veris_df.columns if col.startswith('action.') and '.variety' not in col]

# Define month names
month_names = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Determine the maximum y value across all months to set a common y-axis limit
max_y_value = 0
for month in range(1, 13):
    monthly_data = veris_df[veris_df['month'] == month]
    action_counts = monthly_data[action_columns].sum()
    if action_counts.max() > max_y_value:
        max_y_value = action_counts.max()

# Set up a figure with 3 rows and 4 columns to fit 12 graphs
fig, axes = plt.subplots(3, 4, figsize=(20, 15))

# Loop through each month and create a bar graph
for month in range(1, 13):
    # Filter data for the current month
    monthly_data = veris_df[veris_df['month'] == month]

    # Sum across the 'action.' columns for the current month
    action_counts = monthly_data[action_columns].sum()

    # Extract the last word after the last dot for x-axis labels
    labels = [col.split('.')[-1] for col in action_columns]

    # Select the appropriate subplot (axes) based on the month index
    ax = axes[(month - 1) // 4, (month - 1) % 4]

    # Create a bar graph if there's data for that month
    if not action_counts.empty:
        ax.bar(labels, action_counts, color='skyblue')
        ax.set_title(month_names[month - 1])  # Set title using month name
        ax.set_xlabel("Attack Type")
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
