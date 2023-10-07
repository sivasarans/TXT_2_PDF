from flask import Flask, request, render_template, send_file
import tempfile
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    text = request.form['text']

    # Generate the PDF using FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text, border=0, align='L')

    # Save the PDF to a specific file path
    pdf_file_path = "output.pdf"
    pdf.output(pdf_file_path)

    # Send the PDF as a response for download
    return send_file(pdf_file_path, as_attachment=True, download_name='output.pdf')

if __name__ == '__main__':
    app.run(debug=True)
