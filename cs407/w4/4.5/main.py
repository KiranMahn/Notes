import pandas as pd
from verispy import VERIS

data_dir = "/Users/kiranmahn/GitHub/VCDB/data/json/validated"  # replace with your own address for data
v = VERIS(json_dir=data_dir)

print(v.schema_url)

# Convert JSON to DataFrame and address fragmentation issue
veris_df = v.json_to_df(verbose=True)

# Optionally de-fragment the DataFrame if needed
veris_df = pd.concat([veris_df], axis=1)


# ransomwarecount=veris_df['action.malware.variety.Ransomware'].value_counts()

# Extract and print the action error varieties
types = veris_df['action.error.variety.Misdelivery'].value_counts()
print(types)

