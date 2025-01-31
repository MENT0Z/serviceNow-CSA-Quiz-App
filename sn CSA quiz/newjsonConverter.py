import pandas as pd
import json
import re

# Function to strip HTML tags and format options
def strip_html(html):
    if isinstance(html, str):  # Ensure input is a string
        # Find the position of the first <li> tag
        li_match = re.search(r'<li>', html)
        if li_match:
            question_part = html[:li_match.start()]  # Take the text before the first <li>
        else:
            question_part = html  # If no <li> found, take the whole html

        # Extract options
        options = re.findall(r'<li>(.*?)</li>', html)  # Extract list items
        numbered_options = [f"{i + 1}. {option.strip()}" for i, option in enumerate(options)]
        options_string = '\n'.join(numbered_options)  # Join options with newline

        # Clean the question part
        cleaned_question = re.sub(r'<p>(.*?)</p>', r'\1', question_part)  # Keep paragraph content
        cleaned_question = re.sub(re.compile('<.*?>'), '', cleaned_question).strip()  # Remove any remaining HTML

        return options_string, cleaned_question.strip()  # Return options and cleaned question
    return '', ''  # Return empty strings if input is not a string

# Function to extract and format the answer
def format_answer(html):
    if isinstance(html, str):
        # Replace <br /> with newlines
        html = re.sub(r'<br\s*/?>', '\n', html)  # Replace <br /> with newline
        
        # Clean any remaining HTML tags
        formatted_answer = re.sub(r'<.*?>', '', html).strip()  # Remove remaining HTML
        return formatted_answer
    return ''  # Return empty string if input is not a string

# Load the Excel file
df = pd.read_excel('x_680833_csa_exam_csa_prep_content (19).xlsx')  # Ensure this is the correct file path

# Process the DataFrame
data = []
for _, row in df.iterrows():
    options, qsn = strip_html(row['Front (html)'])  # Remove HTML from the 'Front (html)' column and get options
    ans = format_answer(row['Back (HTML)'])  # Format the answer with newlines for <br />
    data.append({'qsn': qsn, 'ans': ans, 'options': options})

# Convert to JSON
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Save to JSON file
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("JSON file created successfully.")
