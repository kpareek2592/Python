from datetime import date
import datetime

letter = '''Dear <|NAME|>
Greetings from ABC. I am delighted to tell you that you have been selected.

Date: <|DATE|>'''

name = input('Enter your name ')
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", str(date.today()))
print(letter)