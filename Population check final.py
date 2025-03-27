import pandas as pd

input_file = r
output_file_valid = r
output_file_invalid = r

df = pd.read_excel(input_file)

valid_entries = df[
    (df['Work Phone'].notna() | df['Mobile Phone Number'].notna()) &
    df['First Name'].notna() &
    df['Company Name'].notna()
]

invalid_entries = df[
    ~((df['Work Phone'].notna() | df['Mobile Phone Number'].notna()) &
      df['First Name'].notna() &
      df['Company Name'].notna())
]

valid_entries.to_excel(output_file_valid, index=False)
invalid_entries.to_excel(output_file_invalid, index=False)
