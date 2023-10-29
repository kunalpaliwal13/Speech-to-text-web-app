from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'D:\\uni\\web\\STT\\static'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'flac', 'ogg', 'aac', 'wma', 'aiff', 'm4a', 'amr', 'ac3'}

 
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    import assemblyai as aai
    aai.settings.api_key = "d16f4183716949e3ab2e4f6b0db99f0f"
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    text = transcript.text

    text_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'transcript.txt')
    with open(text_file_path, 'w') as text_file:
        text_file.write(text)
    #return send_file(file_path, as_attachment=True)
    return send_file(text_file_path, as_attachment=True, download_name='transcript.txt')
    #return text

@app.route('/')
def hello_world():
    return render_template('prototype.html')

@app.route('/file/<file>')
def file(file):
    return file
 
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":
        if 'myFile' not in request.files:
            return "No file part"
        uploaded_file = request.files['myFile']

        if uploaded_file.filename == '':
            return "No selected file"

        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download', filename=filename))
    return render_template('prototype.html')
    


   
if __name__ =='__main__':
    app.run(debug= True)