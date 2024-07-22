def laboratory_console(): 
    text_string = 'hi everyone, lets start to work'
    whitespaceword = '   hola mundo   '
    letter_seached = 's'

    for x in 'so':
        print(text_string)

    if letter_seached in text_string:
        print(f'already have a {letter_seached} in the text {text_string}')

    if letter_seached not in 'hola mundo':
        print(f'the letter {letter_seached} not have in {text_string}')

    print('first' not in text_string)
    print(f'you cut the text in this from {text_string[0:7]}')

    print(f'i change succesfully the text: {text_string.upper()}')
    print(f'i change succesfully the text: {text_string.lower()}')
    print(f'i remove succesfully whithespaces from: {whitespaceword.strip()}')
    print(f'remplace succesfully letters in: {text_string.split(",")}')
    concatenate_text = whitespaceword + text_string
    print(concatenate_text)

    def text_console ():
        head = '\n------------------- beofalejandro code × The 0.2.3 Happy Bite Edition -------------------\n'
        task_message = (f'{head}Task Failed Sucesfully XD')
        # original_sentence = 'Saint Mount founded this school in 1993'
        # verb, adjetive, time, complement = ['founded', 'school', 'was', 'by Saint Mount']
        # original_sentence = print(f'OriginaL form: {original_sentence}')
        # passive_form = print(f'Passiive form: {adjetive} {time} {verb} {complement}')

        # original_sentence2 = 'they re painting my bedroom tomorrow'
        # verb2, subject2, adjetive2, complement2 = ['painting', 'they re', 'my bedroom', 'tomorrow']
        # if subject2 == 'they re':
            # subject2 = 'I m'
            # if verb2 == 'painting':
                # verb2, time2 = ['painted', 'having']
                # original_form2 = print(f'This is the base form sentence: {original_sentence2}')
                # passive_form2 = print(f'This is a passive form to the sentence: {subject2} {time2} {verb2} {adjetive2} {complement2}', f'\n{task_message.upper()}\n')
            # else:
                # print('check this code, have a error')
        # else:
            # print('i have a wrong, please debug one more time :D')

        return task_message
    return text_console()

def cifrar_cesar(mensaje, desplazamiento):
  """
  Cifra un mensaje usando el cifrado César.

  Args:
      mensaje: El mensaje a cifrar (cadena de texto).
      desplazamiento: El desplazamiento numérico para el cifrado (entero).

  Returns:
      Mensaje cifrado (cadena de texto).
  """
  
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
  """
  Descifra un mensaje cifrado con el cifrado César.

  Args:
      mensaje_cifrado: El mensaje cifrado a descifrar (cadena de texto).
      desplazamiento: El desplazamiento numérico utilizado para el cifrado (entero).

  Returns:
      Mensaje original descifrado (cadena de texto).
  """
  
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

# Ejemplo de uso
mensaje = "Hola mundo"
desplazamiento = 3

mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")

mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
print(f"Mensaje descifrado: {mensaje_descifrado}")
