import pandas as pd
import json

# File path to the uploaded Excel file
file_path = 'x_680833_csa_exam_csa_prep_content (19).xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Rename the columns: 'Front(HTML)' to 'qsn' and 'Back(HTML)' to 'ans'
df = df.rename(columns={'Front (html)': 'qsn', 'Back (HTML)': 'ans'})

# Convert the DataFrame to a dictionary
qna_dict = df[['qsn', 'ans']].to_dict(orient='records')

# Convert the dictionary to a JSON string
qna_json = json.dumps(qna_dict, indent=4)

# Save the JSON string to a file
output_file_path = 'qna_content.json'
with open(output_file_path, 'w') as f:
    f.write(qna_json)

print(f"JSON file created: {output_file_path}")
