from translate import Translator

#using 2 letter ISO or RFC306 to translate, can be switched out for other languages
translator = Translator(to_lang="fr")

try:
    with open('./text.txt', mode='r') as english_text:
        text = english_text.read()
        translation = translator.translate(text)

        #prints out what it is going to write into new translation file
        print(translation)
        #writes to new file
        with open('./text_French.txt', mode='w') as french_text:
            french_text.write(translation)
#file must be called text otherwise it will error letting you know it cannot find it            
except FileNotFoundError as e:
    print("cannot locate the 'text' file")