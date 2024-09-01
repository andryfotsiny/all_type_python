import pyautogui
import keyboard
import os
from datetime import datetime

# Dossier de sauvegarde des captures d'écran
save_path = "D:\\capture"

# Fonction pour capturer l'écran et sauvegarder l'image
def capture_screen():
    # Vérifie si le dossier existe, sinon le créer
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Nom du fichier avec horodatage
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"capture_{timestamp}.png"
    full_path = os.path.join(save_path, file_name)

    # Capture d'écran
    screenshot = pyautogui.screenshot()

    # Sauvegarde de l'image
    screenshot.save(full_path)
    print(f"Capture enregistrée sous {full_path}")

# Assignation du raccourci Ctrl+5 pour capturer l'écran
keyboard.add_hotkey('ctrl+5', capture_screen)

# Rester en attente des touches
print("Appuyez sur Ctrl+5 pour capturer l'écran.")
keyboard.wait('esc')