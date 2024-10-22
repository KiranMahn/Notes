import pandas as pd
from verispy import VERIS

# Load the VERIS data
data_dir = "/Users/kiranmahn/GitHub/VCDB/data/json/validated"  # replace with your own address for data
v = VERIS(json_dir=data_dir)

# Convert JSON to DataFrame and address fragmentation issue
veris_df = v.json_to_df(verbose=True)

# Optionally de-fragment the DataFrame if needed
veris_df = veris_df.copy()

# Use 'plus.timeline.notification.month' and 'plus.timeline.notification.year' to get month and year
veris_df['month'] = veris_df['timeline.incident.month']
veris_df['year'] = veris_df['timeline.incident.year']

# Filter data for June 2023
june_2023_data = veris_df[(veris_df['month'] == 6) & (veris_df['year'] == 2023)]

# Count summaries that contain "MOVEit"
count = 0
for index, row in june_2023_data.iterrows():
    summary = row.get('summary', 'No summary available')
    if "MOVEit" in summary:
        count += 1

# Print the count
print(f"Number of summaries in June 2023 containing 'MOVEit': {count}")
