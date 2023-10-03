import tkinter as tk
import requests
from tkinter import END, Toplevel, Listbox, messagebox
import socket

def se_connecter():
    ip = entry_ip.get()
    port = entry_port.get()
    
    if not ip or not port:
        resultat_label.config(text="Veuillez remplir tous les champs.")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))

        resultat_label.config(text="Connexion réussie.")
        
        afficher_menu_telechargement(client_socket)

    except ConnectionRefusedError:
        resultat_label.config(text="Erreur de connexion : Connexion refusée.")
    except Exception as e:
        resultat_label.config(text=f"Erreur de connexion : {str(e)}")

def afficher_menu_telechargement(client_socket):
    fenetre_menu_telechargement = Toplevel(fenetre)
    fenetre_menu_telechargement.title("Menu de téléchargement")
    fenetre_menu_telechargement.geometry("400x300")
    client_socket.send('LIST'.encode())
    files = client_socket.recv(1024).decode("utf-8")
    
    def on_selection(event):
        selection = liste_fichiers.get(liste_fichiers.curselection())
        
        extension = selection.split(".")
        if len(extension) > 1:
            bouton_telecharger.config(text="Download")
        else:
            bouton_telecharger.config(text="Open")
        
    def telecharger_fichier():
        fichier_selectionne = liste_fichiers.get(liste_fichiers.curselection())
        print(fichier_selectionne)
        fichier_selectionne=requests.get()
        client_socket.send(f'GET {fichier_selectionne}'.encode())
        data = client_socket.recv(1024)
        if data == b'File not found':
              messagebox.showerror("Erreur", "Fichier non trouvé sur le serveur.")
        else:
            with open(fichier_selectionne, 'wb') as file:
                 while data:
                    file.write(data)
                    data = client_socket.recv(1024)
        print(f"{fichier_selectionne} downloaded successfully.")
        messagebox.showinfo("Succès", f"{fichier_selectionne} téléchargé avec succès.")

    list_button = tk.Button(fenetre_menu_telechargement, text="Lister les fichiers sur le serveur", bg="green", width=40)
    list_button.pack()

    liste_fichiers = Listbox(fenetre_menu_telechargement, width=48)
    
    fichiers_disponibles = []  
    for fichier in files.split("=>"):
        nom_fichier = fichier.strip()
        liste_fichiers.insert(END, nom_fichier)

    liste_fichiers.pack()
    liste_fichiers.bind('<<ListboxSelect>>', on_selection)

    bouton_telecharger = tk.Button(fenetre_menu_telechargement, text="Télécharger", command=telecharger_fichier, bg="green", width=40)
    bouton_telecharger.pack()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Connexion page")

container = tk.Frame(fenetre, width=200, bg="gray")
container.pack(pady=20)

label_ip = tk.Label(container, text="Adresse IP :", width=30, height=2, bg="gray")
label_ip.pack()

entry_ip = tk.Entry(container)
entry_ip.pack()

label_port = tk.Label(container, text="Port :", width=30, height=2, bg="gray")
label_port.pack()

entry_port = tk.Entry(container)
entry_port.pack()

resultat_label = tk.Label(fenetre, text="")
resultat_label.pack()

bouton_connexion = tk.Button(container, text="Connexion", command=se_connecter, bg="gray", width=30, height=2)
bouton_connexion.pack()

fenetre.mainloop()
