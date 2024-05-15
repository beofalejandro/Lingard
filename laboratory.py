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
