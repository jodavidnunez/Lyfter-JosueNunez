"""1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`"""
hotel_data = {
    "Hotel_1":{
        "nombre":"RIU Guanacaste",
        "numero_de_estrellas":4,
        "habitaciones":[
            {
                "numero":1,
                "piso":1,
                "precio_por_noche":120
            },
            {
                "numero":2,
                "piso":2,
                "precio_por_noche":140
            }
        ]
    },
    "Hotel_2":{
        "nombre":"Fiesta",
        "numero_de_estrellas":3,
        "habitaciones":[
            {
                "numero":1,
                "piso":1,
                "precio_por_noche":80
            },
            {
                "numero":2,
                "piso":2,
                "precio_por_noche":100
            }
        ]
    }
}

import pprint
pprint.pprint(hotel_data)