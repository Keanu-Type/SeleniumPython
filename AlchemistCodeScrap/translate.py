from googletrans import Translator

Translate = Translator()

hello=Translate.translate('"Fierce Little Wolf, All Grown Up"',dst='en')
print(hello.text)