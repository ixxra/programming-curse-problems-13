import json
import re
from sys import argv


f = open(argv[1])
texto = f.read()

palabras = re.findall(r'\w\w\w+', texto)
cuenta = dict.fromkeys(palabras, 0)

for w in palabras:
    cuenta[w] = texto.count(w)

data = cuenta.items()
ordered_data = sorted(data, key=lambda item : item[1], reverse=True)

jsonified = json.dumps(ordered_data)
datafile = open(argv[2], 'w')
datafile.write(jsonified)
