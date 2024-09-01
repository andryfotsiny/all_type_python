import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la commande : {e}\n{e.stderr}")
        return None

def create_hotspot(ssid, password):
    # Configurez le point d'accès
    command = [
        'netsh', 'wlan', 'set', 'hostednetwork',
        f'mode=allow', f'ssid={ssid}', f'key={password}'
    ]
    output = run_command(command)
    if output:
        print("Configuration terminée.")

    # Démarrez le point d'accès
    command = ['netsh', 'wlan', 'start', 'hostednetwork']
    output = run_command(command)
    if output:
        messagebox.showinfo("Info", "Point d'accès démarré.")

def stop_hotspot():
    # Arrêtez le point d'accès
    command = ['netsh', 'wlan', 'stop', 'hostednetwork']
    output = run_command(command)
    if output:
        messagebox.showinfo("Info", "Point d'accès arrêté.")

def start_hotspot():
    ssid = ssid_entry.get()
    password = password_entry.get()
    if ssid and password:
        create_hotspot(ssid, password)
    else:
        messagebox.showwarning("Avertissement", "Veuillez entrer un SSID et un mot de passe.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion du Point d'Accès")
root.geometry("400x250")
root.configure(bg="#f5f5f5")

# Style des widgets
style = ttk.Style()
style.configure("TLabel", background="#f5f5f5", font=("Helvetica", 12))
style.configure("TEntry", padding=5, relief="flat")
style.configure("TButton",
                padding=6,
                relief="flat",
                background="#4CAF50",  # Couleur de fond du bouton
                foreground="green",    # Couleur du texte du bouton
                font=("Helvetica", 12))

# Appliquer un style de bouton personnalisé
style.map("TButton",
          background=[("active", "#45a049")],  # Couleur de fond du bouton au survol
          relief=[("pressed", "sunken")],  # Effet d'enfoncement lorsqu'on clique
          foreground=[("pressed", "green")])  # Couleur du texte du bouton lorsqu'enfoncé

# Création des éléments de l'interface
ttk.Label(root, text="SSID:", anchor="w").grid(row=0, column=0, padx=20, pady=10, sticky="w")
ttk.Label(root, text="Mot de Passe:", anchor="w").grid(row=1, column=0, padx=20, pady=10, sticky="w")

ssid_entry = ttk.Entry(root)
ssid_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

start_button = ttk.Button(root, text="Démarrer le Point d'Accès", command=start_hotspot)
start_button.grid(row=2, column=0, columnspan=2, pady=20)

stop_button = ttk.Button(root, text="Arrêter le Point d'Accès", command=stop_hotspot)
stop_button.grid(row=3, column=0, columnspan=2, pady=20)

# Ajustement automatique des colonnes
root.columnconfigure(1, weight=1)

# Lancement de l'application Tkinter
root.mainloop()
