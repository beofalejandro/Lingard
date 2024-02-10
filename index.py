from flask import Flask as fk, render_template as rt, request as rq
from pytube import YouTube
import os

# Start Flask
app = fk(__name__)

# Create a route for create url - its important to create more pages
@app.route('/')
# Insert content to index
def index():
    return rt('index.html')

# DOWNLOADER
@app.route('/download', methods=['POST'])
def dowloader():
    url_link = str(rq.form['url_link'])
    video_quality = str(rq.form['video_quality'])

    try:
        # Set connection with youtube with get a video link
        yt = YouTube(url_link)
        stream = yt.streams.filter(res = video_quality).first()

        # Download in especific directory
        os.path.join('Downloads', f'{yt.title}.mp4')
        stream.download(output_path='Downloads')

        return rt('index.html')
    except Exception as e:
        return rt('index.html')

# CALCULATOR
@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = float(rq.form['number1'])
    number2 = float(rq.form['number2'])
    operation = rq.form['operation']

    if operation == 'suma':
        result = number1 + number2
    elif operation == 'resta':
        result = number1 - number2
    else:
        result = 'operacion no valida'

    return rt('index.html', result=result)

# Start the app
if __name__ == '__main__':
    app.run(debug=True)