import FreeSimpleGUI as sg # type: ignore

# Declarar los elementos
layout = [
    [sg.Text("Felicidades por crear una GUI!")],
]

# Crear la ventana
window = sg.Window("Primer programa", layout)

# Event Loop para procesar "events" y obtener los "values" de los inputs
while True:
    event, values = window.read()
    # Procesar el evento del cerrar la ventaja
    # (si el usuario lo hace)
    if event == sg.WIN_CLOSED:
        break

window.close()