import pyautogui
import time
import random
import traceback

try:

    acciones = [
        "Qué eesee", "Cómoooo funnnnciona", "Por qué", "Cuándo salió", "Cuánto valee",
        "Cuántos aaños tieene", "Cuáal ees eel oreigen dee", "Paara qué sirve",
        "Cómoo aaprender", "Cóomo se usa", "Qué significa", "Cuál es el mejor",
        "Qué taan cierto ees", "Cómo hacer", "Qué pasó con", "Qué opinan de"
    ]

    objetos = [
        "la inteligencia artificial", "el Big Bang", "la selección Colombia",
        "Python", "los agujeros negros", "Elon Musk", "la cultura japonesa",
        "los teléfonos Samsung", "Apple", "Shakira", "Bad Bunny",
        "las criptomonedas", "las redes sociales", "Marvel",
        "los volcanes", "el océano", "los OVNIs", "ChatGPT"
    ]

    def generar_busqueda():
        return f"{random.choice(acciones)} {random.choice(objetos)}"

    def abrir_nueva_pestaña():
        pyautogui.hotkey("ctrl", "t")
        time.sleep(1)

    def cerrar_pestaña():
        pyautogui.hotkey("ctrl", "w")
        time.sleep(0.8)

    def escribir_busqueda(texto):
        pyautogui.write(texto, interval=0.05)
        pyautogui.press("enter")

    repeticiones = 1000

    print("Listo. Abre Edge, ponlo delante y NO cambies de ventana.\n")
    time.sleep(2)

    for i in range(repeticiones):
        print(f"Búsqueda {i+1}/{repeticiones}")

        abrir_nueva_pestaña()

        consulta = generar_busqueda()
        escribir_busqueda(consulta)

        time.sleep(random.randint(2, 3))

        cerrar_pestaña()

except Exception:
    traceback.print_exc()
    input("ERROR — Presiona ENTER para cerrar...")
