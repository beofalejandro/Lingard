from flask import Flask as fk, render_template as rt, request as rq
from pytube import YouTube
import os
import laboratory as lab

# Start Flask
app = fk(__name__)

# Create a route for create url - its important to create more pages
# All the methods behind here
@app.route('/')
# Insert content to index
def index():
    return rt('index.html')

@app.route('/about')
def about():
    return rt('about.html')


# Methods for index page
# DOWNLOADER
@app.route('/download', methods=['POST'])
def dowloader():
    # get the video link and the quality for this 
    url_link = str(rq.form['url_link'])
    video_quality = str(rq.form['video_quality'])

    try:
        # Set connection with youtube with get a video link
        yt = YouTube(url_link)
        stream = yt.streams.filter(res = video_quality).first()

        # Download in especific directory
        os.path.join('Downloads', f'{yt.title}.mp4')
        stream.download(output_path='Downloads')

        # return in the document
        return rt('index.html', result_download = 'Descargado Satisfactoriamente')
    except Exception as e:
        return rt('index.html', result_download = 'Hubo un error en la descarga del video')

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
    elif operation == 'multiplicacion':
        result = number1 * number2
    elif operation == 'division':
        result = number1 / number2
    else:
        result = 'operacion no valida'

    return rt('index.html', result_equal = result)

# My Laboratory 
@app.route('/laboratory', methods=['POST'] )
def laboratory():
    output = lab.laboratory_console()

    return rt('index.html',
            output_laboratory = output)

@app.route('/laboratory2', methods=['POST'])
def laboratory2():
    number1 = float(rq.form['number1'])
    number2 = float(rq.form['number2'])
    operation = rq.form['operation']

    if operation == 'suma':
        result = lab.suma(number1, number2)
    elif operation == 'resta':
        result = lab.resta(number1, number2)
    elif operation == 'multiplicacion':
        result = lab.multiplicacion(number1, number2)
    elif operation == 'division':
        result = lab.division(number1, number2)
    else:
        result = 'operacion no valida'

    return rt('index.html', result_equal = result)

# Start the app
if __name__ == '__main__':
    app.run(debug=True)