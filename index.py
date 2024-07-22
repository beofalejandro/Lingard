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

@app.route('/encription-calculator')
def encription_calculator():
    return rt('pages/encription-calc.html')


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

## CODE FOR ENCRYPTION CALCULATOR
def cifrar_cesar(mensaje, desplazamiento):
  alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"

  mensaje_cifrado = ""

  for caracter in mensaje:
    if caracter.isspace():
      mensaje_cifrado += caracter
      continue

    if caracter.isupper():
      indice_original = alfabeto_mayusculas.index(caracter)
      indice_cifrado = (indice_original + desplazamiento) % len(alfabeto_mayusculas)
      mensaje_cifrado += alfabeto_mayusculas[indice_cifrado]
    else:
      indice_original = alfabeto_minusculas.index(caracter)
      indice_cifrado = (indice_original + desplazamiento) % len(alfabeto_minusculas)
      mensaje_cifrado += alfabeto_minusculas[indice_cifrado]

  return mensaje_cifrado

def descifrar_cesar(mensaje_cifrado, desplazamiento):
  alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"

  mensaje_descifrado = ""

  for caracter in mensaje_cifrado:
    if caracter.isspace():
      mensaje_descifrado += caracter
      continue

    if caracter.isupper():
      indice_cifrado = alfabeto_mayusculas.index(caracter)
      indice_original = (indice_cifrado - desplazamiento) % len(alfabeto_mayusculas)
      mensaje_descifrado += alfabeto_mayusculas[indice_original]
    else:
      indice_cifrado = alfabeto_minusculas.index(caracter)
      indice_original = (indice_cifrado - desplazamiento) % len(alfabeto_minusculas)
      mensaje_descifrado += alfabeto_minusculas[indice_original]

  return mensaje_descifrado


# ENCRIPTION CODE
@app.route('/encrypt', methods=['POST'])
def encrypt():
    mensaje = str(rq.form['message'])
    desplazamiento = int(rq.form['despl'])

    mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
    original_message = str(f"      Mensaje original: {mensaje}")
    cifrated_mens = str(f"      Mensaje cifrado: {mensaje_cifrado}")

    mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
    desifated_mens = str(f"      Mensaje descifrado: {mensaje_descifrado}")

    concatenated_text = original_message + '\n' + cifrated_mens + '\n' + desifated_mens

    return rt('pages/encription-calc.html', cifrated_message = concatenated_text)
    # return rt('pages/encription-calc.html', original_message = original_text)
    # return rt('pages/encription-calc.html', cifrated_mens = cifrated_text)


# Start the app
if __name__ == '__main__':
    app.run(debug=True)