
"""
Un utilitaire Tkinter pour des phrases répétitives
"""
import tkinter as tk
import sys
from tkinter import filedialog


# J'utilise une classe qui ne dérive pas d'une classe de tkinter, comme préconisé par :
# https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly
class MapApp():  # Ne dérive pas de Tkinter

    text = None
    def __init__(self, master, files):
        if files:
            self.files = files
            print(f"Les fichiers à traiter sont : ")
            for file in files:
                print(file)
        else:
            self.files = ["fichier 1", "fichier 2"]

        self.master = master
        self.master.title("Mon application graphique.")
        self.tkframe = tk.Frame(self.master)  # Premier objet tk.Frame.

        self.frame_top = tk.Frame(self.tkframe)
        self.frame_top.pack(side="top")
        self.frame_bottom = tk.Frame(self.tkframe)
        self.frame_bottom.pack(side="top")

        # Créer un bouton quitter
        self.button_quit = tk.Button(self.frame_bottom, text="Quitter", command=master.quit)
        self.button_quit.pack()

        # Créer un bouton Ouvrir
        self.button_open = tk.Button(self.frame_bottom, text="Ouvrir...", command=self.ouvrir_fichier)
        self.button_open.pack()

        # Une entrée en haut
        self.files_entry = tk.Entry(self.frame_top)
        self.files_entry.pack(side='left')

        if self.files :
            for line in self.files:
                self.files_entry.insert(tk.END, str(line) + "\n\n")

        # Créer une barre pour menu déroulant et y insérer des menus.
        menu_bar = tk.Menu(master)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Ouvrir un fichier...", command=self.ouvrir_fichier)
        file_menu.add_command(label="Fermer le fichier")
        file_menu.add_command(label="Quitter l'application", command=root.quit)

        menu_bar.add_cascade(label="Fichier", menu=file_menu)

        # Configurer la fenêtre principale pour utiliser la barre de menus
        self.master.config(menu=menu_bar)

        self.tkframe.pack()

    def ouvrir_fichier(self):
        # Insérer ici la fonction que vous souhaitez exécuter lorsque l'option "Ouvrir" est sélectionnée
        path = filedialog.askopenfilename()
        with open(path, "r") as f:
            text = f.read()
        print(text)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        all_files = sys.argv[1:]
    except:
        filename = None
        all_files = None
    # faire quelque chose avec le nom de fichier
    if filename:
        print(f"Lancement du programme avec le fichier {filename}")
        print(f"commande transmise : f{all_files}")
    else:
        print("Pas de fichier")

    root = tk.Tk()
    root.geometry("400x200")
    app = MapApp(root, files=all_files )
    root.mainloop()
