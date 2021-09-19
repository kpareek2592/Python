string = 'This is  a string with spaces.'

doubleSpaces = string.find('  ')
print(doubleSpaces)

string = string.replace('  ', ' ')
doubleSpaces = string.find('  ')
print(doubleSpaces)
print(string)