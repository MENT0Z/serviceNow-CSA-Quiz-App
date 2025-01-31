from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# File path to the uploaded Excel file
file_path = 'x_680833_csa_exam_csa_prep_content (19).xlsx'

@app.route('/')
def display_qna():
    # Read the Excel file using pandas
    df = pd.read_excel(file_path)

    # Extract the "Front(HTML)" (Question) and "Back(HTML)" (Answer) columns
    questions = df['Front (html)'].tolist()
    answers = df['Back (HTML)'].tolist()

    # Generate the HTML for the questions and answers
    qna_html = ""
    for i, (q, a) in enumerate(zip(questions, answers)):
        qna_html += f"""
        <div class="card mt-3">
            <div class="card-header">
                <h4>Question {i + 1}</h4>
                <div onclick="toggleAnswer('answer-{i}')" style="cursor: pointer;">
                    {q} <!-- Render the question (HTML content) -->
                </div>
            </div>
            <div id="answer-{i}" class="card-body" style="display: none;">
                <h5>Answer:</h5>
                {a} <!-- Render the answer (HTML content) -->
            </div>
        </div>
        """

    # Render the HTML template with all Q&A pairs
    return render_template_string(f"""
    <html>
        <head>
            <title>Q&A Viewer</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script>
                // Function to toggle the answer visibility
                function toggleAnswer(id) {{
                    var element = document.getElementById(id);
                    if (element.style.display === "none") {{
                        element.style.display = "block";
                    }} else {{
                        element.style.display = "none";
                    }}
                }}
            </script>
        </head>
        <body>
            <div class="container">
                <h1>Question & Answer Viewer</h1>
                {qna_html}
            </div>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
