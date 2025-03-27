import pandas as pd
import re

input_file = #file_link
output_file_valid = #file_link
output_file_invalid = #file_link

df = pd.read_excel(input_file)

def is_valid_mobile(mobile):
    clean_mobile = re.sub(r'\D', '', str(mobile))
    if len(clean_mobile) < 10:
        return False
    if clean_mobile[-10] in '6789':
        return True
    return False

df['Work Phone'] = df['Work Phone'].astype(str).str.replace(' ', '', regex=False)

df['Valid Mobile'] = df['Work Phone'].apply(lambda x: is_valid_mobile(x) if pd.notna(x) else False)

valid_mobile_numbers = df[df['Valid Mobile']].drop(columns=['Valid Mobile'])
invalid_mobile_numbers = df[~df['Valid Mobile']].drop(columns=['Valid Mobile'])

valid_mobile_numbers.to_excel(output_file_valid, index=False)
invalid_mobile_numbers.to_excel(output_file_invalid, index=False)
