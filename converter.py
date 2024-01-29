import json

# Lee el contenido del archivo JSON
with open('parameters.json', 'r') as file:
    data = json.load(file)

# Crea la cadena de texto en formato bash
bash_array = " ".join([f"'{item['ParameterKey']}=\\\"{item['ParameterValue']}\\\"'" for item in data])

# Imprime la cadena de texto resultante
print(bash_array)