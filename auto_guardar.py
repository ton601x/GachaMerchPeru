import os
import time
from PIL import ImageGrab

# Guarda todo en una carpeta unica 'img/general' dentro del proyecto
CARPETA_DESTINO = os.path.join(os.getcwd(), "img", "general")
os.makedirs(CARPETA_DESTINO, exist_ok=True)

print("=" * 60)
print("SCRIPT ACTIVO - MODO CARPETA GENERAL")
print(f"Ruta de destino: {CARPETA_DESTINO}")
print("Copia cualquier imagen (clic derecho -> Copiar imagen) para guardarla.")
print("=" * 60)

ultima_data = None

while True:
    try:
        captura = ImageGrab.grabclipboard()
        if captura is not None and hasattr(captura, "save"):
            bytes_actuales = captura.tobytes()
            if bytes_actuales != ultima_data:
                nombre_archivo = f"img_{int(time.time())}.png"
                ruta_final = os.path.join(CARPETA_DESTINO, nombre_archivo)
                captura.save(ruta_final, "PNG")
                print(f"[GUARDADO] -> {nombre_archivo}")
                ultima_data = bytes_actuales
        time.sleep(1)
    except Exception:
        time.sleep(1)
        