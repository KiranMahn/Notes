import pandas as pd
import matplotlib.pyplot as plt
from verispy import VERIS

# Creates a graph showing the total number of attacks in June for each year

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

# Filter data to only include incidents from June
june_data = veris_df[veris_df['month'] == 5]

# Group by year and count the total number of attacks for each year
june_attacks_per_year = june_data['year'].value_counts().sort_index()

# Create a bar graph to show the total number of attacks in June for each year
plt.figure(figsize=(10, 6))
plt.bar(june_attacks_per_year.index, june_attacks_per_year.values, color='#1f77b4')
plt.title("Total Number of Attacks in May Each Year")
plt.xlabel("Year")
plt.ylabel("Number of Attacks")
plt.xticks(june_attacks_per_year.index, rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()
