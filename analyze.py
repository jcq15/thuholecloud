import json

holes = []

with open('data.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
    while s:
        holes.append(json.loads(s))
        s = f.readline()

with open('puretxt.txt', 'w', encoding='utf-8') as f:
    for hole in holes:
        if 'data' in hole:
            f.write(hole['data']['text']+'\n')
