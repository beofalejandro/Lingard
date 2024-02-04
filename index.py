from flask import Flask as fk, render_template as rt, request as rq
from pytube import YouTube # Soon proyect

# Method to pytube library dowloader
# def downloader:

# Start Flask
app = fk(__name__)

# Create a route for create url - its important to create more pages
@app.route('/')
# Insert content to index
def index():
    return rt('index.html')

@app.route('/calcular', methods=['POST'])
def calculate():
    number1 = float(rq.form['number1'])
    number2 = float(rq.form['number2'])
    operation = rq.form['operation']

    if operation == 'suma':
        result = number1 + number2
    if operation == 'resta':
        result = number1 - number2
    else:
        result = 'operacion no valida'

    return rt('index.html', result=result)

# Start the app
if __name__ == '__main__':
    app.run(debug=True)