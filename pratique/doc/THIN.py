
from ctypes import sizeof
import tkinter as tk
from tkinter import Canvas, messagebox
import tkinter
from turtle import width
import tkinter.font as font
from tkinter import PhotoImage
from PIL import Image, ImageTk


def telecharger_fichier():
    fichier_selectionne = liste_fichiers.get(liste_fichiers.curselection())
    






    messagebox.showinfo("Téléchargement", f"Le fichier '{fichier_selectionne}' a été téléchargé avec succès.")


fenetre = tk.Tk()

fenetre.title("Menu de téléchargement")
container=tk.Frame(fenetre, width=40)
container.pack()
list= tk.Button(container,text="List files on server",bg="green",width=40)
list.pack()
liste_fichiers = tk.Listbox(container, width= 48)
fichiers_disponibles = ["fichier1.txt", "Dama.jpg", "picture.jpg", "fichier4.zip","video/"]
for fichier in fichiers_disponibles:
    liste_fichiers.insert(tk.END, fichier)
liste_fichiers.pack()

bouton_telecharger = tk.Button(container, text="Download a file", command=telecharger_fichier,bg="green",width=40)
bouton_quite = tk.Button(container, text="quitter", command=fenetre.quit,bg="red",width=40)

bouton_telecharger.pack()
bouton_quite.pack()



def ouvrir_dossier():
    dossier_selectionne = liste_fichiers.get(liste_fichiers.curselection())
    if dossier_selectionne.endswith('/'):
        messagebox.showinfo("Ouverture de dossier", f"Le dossier '{dossier_selectionne}' a été ouvert.")
    else:
        messagebox.showerror("Erreur", "Veuillez sélectionner un dossier pour l'ouvrir.")
bouton_open = tk.Button(container, text="Open", command=ouvrir_dossier, bg="green", width=40)
bouton_open.pack()
bouton_open.config(state=tk.DISABLED)

def on_listbox_select(event):
    dossier_selectionne = liste_fichiers.get(liste_fichiers.curselection())
    if dossier_selectionne.endswith('/'):
        bouton_open.config(state=tk.NORMAL)
    else:
        bouton_open.config(state=tk.DISABLED)

liste_fichiers.bind("<<ListboxSelect>>", on_listbox_select)






# bouton_telecharger.grid(row=0,column=0)
# bouton_quite.grid(row=0,column=1)

fenetre.mainloop()

    
# fig= tkinter.Tk()

# # fig.title("my first programme is very good")
# # #fig.geometry("1000x600")
# # fig.minsize(400,600)
# # fig.maxsize(400,600)
# # fig.resizable(width=True,height=True)

# # figu= tkinter.Label(fig, text="bonjour tout le monde")

# # Entry_page=tkinter.Entry(fig,width=100)
# # Entry_page.pack()
# button_quit=tkinter.Button(fig,text="Ok")
# button_quit.pack()
# check_button=tkinter.Checkbutton(fig,text="pubier")
# human_check=tkinter.Radiobutton(fig,text="Homme",value=1)
# woman_check=tkinter.Radiobutton(fig,text="Femme",value=0)
# check_button.pack()
# human_check.pack()
# woman_check.pack()
# fig.mainloop()