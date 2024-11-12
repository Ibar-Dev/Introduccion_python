import json

def parse_json(json_str):
    return json.loads(json_str)

# Ejemplo de uso:
json_str = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'
objeto_python = parse_json(json_str)
print(objeto_python)
