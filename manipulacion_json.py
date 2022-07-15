import json
from typing_extensions import Self

with open('ejemplos_json\eventos_black.json') as file:
    data = json.load(file)

    x = data["direccion"]["calle"]
