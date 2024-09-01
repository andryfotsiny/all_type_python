from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import keyboard

def create_folder(drive, folder_name, parent_id=None):
    # Crée un dossier dans Google Drive
    folder_metadata = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        folder_metadata['parents'] = [{'id': parent_id}]
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    return folder['id']

def upload_folder_to_drive(folder_path, drive_folder_id):
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile('client_secrets.json')  # Spécifiez le chemin complet si nécessaire
    gauth.LocalWebserverAuth()  # Authentification locale
    drive = GoogleDrive(gauth)

    # Créer le dossier `dossierenv` s'il n'existe pas déjà
    folder_list = drive.ListFile({'q': f"title='{drive_folder_id}' and mimeType='application/vnd.google-apps.folder'"}).GetList()
    if not folder_list:
        print("Dossier 'dossierenv' non trouvé. Création du dossier...")
        drive_folder_id = create_folder(drive, 'dossierenv')
        print(f"Dossier 'dossierenv' créé avec l'ID: {drive_folder_id}")
    else:
        drive_folder_id = folder_list[0]['id']

    # Upload des fichiers dans le dossier
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            gfile = drive.CreateFile({'parents': [{'id': drive_folder_id}]})
            gfile['title'] = file_name
            gfile.SetContentFile(file_path)
            gfile.Upload()
            print(f'Uploaded: {file_name}')

def on_ctrl_6():
    folder_path = 'D:\\capture'
    upload_folder_to_drive(folder_path, 'dossierenv')
    print("Upload complete!")

# Définir le raccourci clavier Ctrl+6 pour exécuter la fonction
keyboard.add_hotkey('ctrl+6', on_ctrl_6)

keyboard.wait('esc')  # Vous pouvez appuyer sur 'esc' pour terminer le script
