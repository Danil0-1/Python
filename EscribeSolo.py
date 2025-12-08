import pyautogui
import time

# --- 1. AQUÍ PEGAS EL TEXTO DE LA IZQUIERDA ---
texto = """
Dear Helena,

Thank you for your prompt response and for providing the opportunity to test the system.
I’m looking forward to exploring its features and understanding how well it aligns with our needs.

Regarding collaboration and cost-sharing, I believe a demonstration will give us both a clearer picture of how the system could be implemented across multiple teams.
Once I have access to the demo, I'll be better positioned to assess the technical and practical aspects of the system for our use case.

If you could send me the link to access the demo and any required login details, that would be much appreciated.

Thanks again for your time and consideration. I look forward to hearing from EF Student soon.

Best regards,
Stef Shaw
"""

# --- 2. TIEMPO PARA QUE TE PASES A LA PÁGINA Y PONGAS EL CURSOR ---
print("Tienes 5 segundos para ir a la página y poner el cursor donde quieres que escriba...")
time.sleep(5)

# --- 3. ESCRIBIR EL TEXTO AUTOMÁTICAMENTE ---
pyautogui.write(texto, interval=0.01)
