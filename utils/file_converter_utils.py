from flask import send_file
import io
from fpdf import FPDF
import docx
import json

def convert_image_to_pdf(image_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_file, x=10, y=8, w=190)
    
    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    
    return send_file(buffer, mimetype='application/pdf', download_name='converted.pdf')

def convert_docx_to_txt(docx_file):
    doc = docx.Document(docx_file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    
    buffer = io.BytesIO()
    buffer.write(text.encode('utf-8'))
    buffer.seek(0)
    
    return send_file(buffer, mimetype='text/plain', download_name='converted.txt')

def convert_json_to_txt(json_file):
    data = json.load(json_file)
    text = json.dumps(data, indent=4)
    
    buffer = io.BytesIO()
    buffer.write(text.encode('utf-8'))
    buffer.seek(0)
    
    return send_file(buffer, mimetype='text/plain', download_name='converted.txt')
