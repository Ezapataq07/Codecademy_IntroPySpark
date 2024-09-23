import re

pattern = '$**+*{2}'

pattern = pattern.replace('$', ' $ ')
pattern = pattern.replace('+', ' + ')
pattern = pattern.replace('*{', ' *{')
pattern = pattern.replace('}', '} ')
pattern = pattern.replace('**', ' * * ')

print(pattern.split())
