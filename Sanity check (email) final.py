import pandas as pd
import re

input_file = r"D:\Hubspot contact\DB (Second cons)\14-10\wf\2.San em\pop_valid.xlsx"
output_file_valid = r"D:\Hubspot contact\DB (Second cons)\14-10\wf\2.San em\san_em_valid.xlsx"
output_file_invalid = r"D:\Hubspot contact\DB (Second cons)\14-10\wf\2.San em\san_em_invalid.xlsx"

df = pd.read_excel(input_file)

email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email(email):
    if pd.isna(email):
        return False 
    email = email.strip()
    return re.match(email_pattern, email) is not None

df['Valid Email'] = df['Work Email'].apply(lambda x: is_valid_email(x))

valid_email_entries = df[df['Valid Email'] | df['Work Email'].isna()]
invalid_email_entries = df[~(df['Valid Email'] | df['Work Email'].isna())]

valid_email_entries = valid_email_entries.drop(columns=['Valid Email'])
invalid_email_entries = invalid_email_entries.drop(columns=['Valid Email'])

valid_email_entries.to_excel(output_file_valid, index=False)

invalid_email_entries.to_excel(output_file_invalid, index=False)
