# Ejercicio - Callback para JSON
# Voy a darle un JSON (archivo) y quiero poder hacerle la operacion (funcion) que me de la gana
# por ejemplo buscar ERROR, o transformarlo todo a mayusculas, o etc...
import json

def json_callback(data, operation):
    return operation(data)

def test_json_callback():
    with open("test.json", 'r') as file:
        json_data = json.load(file)
        
    expected = {k: v.upper() for k, v in json_data.items()}
    callback = json_callback(json_data, lambda data: {k: v.upper() for k,v in data.items()})
    assert callback == expected
    