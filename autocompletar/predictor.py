import json

f = open('base-de-datos.json')
data = f.read()

histograma = json.loads(data)
words = [w for w, c in histograma]

def predictor(typing):
    posibilities = [w for w in words if w.startswith(typing)]
    return posibilities


while True:
    typing = raw_input('>>')
    print predictor(typing)

