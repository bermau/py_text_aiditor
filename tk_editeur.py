"""
Un utilitaire Tkinter pour des phrases répétitives
"""
import tkinter as tk
import sys
from tkinter import filedialog


def fonction_trt(txt: str):
    return txt.upper()


# J'utilise une classe qui ne dérive pas d'une classe de tkinter, comme préconisé par :
# https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly
def ouvrir_fichier():
    # Insérer ici la fonction que vous souhaitez exécuter lorsque l'option "Ouvrir" est sélectionnée
    path = filedialog.askopenfilename()
    with open(path, "r") as f:
        text = f.read()
    print(text)


class MapApp():  # Ne dérive pas de Tkinter

    def __init__(self, tk_master, files):

        if files:
            self.files = files
            print(f"Les fichiers à traiter sont : ")
            for file in files:
                print(file)
        else:
            self.files = ["fichier 1", "fichier 2"]

        self.text = ["Ceci est un texte ", "d'initialisation et quelques lignes un peu longues pour prendre de la "
                                           "place. "]

        self.tkmaster = tk_master
        self.tkmaster.title("Mon éditeur spécialisé")

        self.tkframe = tk.Frame(self.tkmaster)  # Premier objet tk.Frame.

        self.frame_top = tk.Frame(self.tkframe)
        self.frame_top.pack(side="top")

        self.frame_bottom = tk.Frame(self.tkframe)
        self.frame_bottom.pack(side="left")

        self.frame_right = tk.Frame(self.tkframe)
        self.frame_right.pack(side="right")

        # Une entrée en haut
        self.text_area = tk.Text(self.frame_top, height=20, width=30)
        # self.text_entry.place(height=20, width=30)
        self.text_area.pack(side='left')

        # Créer un bouton d'action
        self.button_action_1 = tk.Button(self.frame_right, text="Traitement1", command=self.traitement1)
        self.button_action_1.pack()

        # Créer un bouton Ouvrir
        self.button_open = tk.Button(self.frame_bottom, text="Ouvrir...", command=ouvrir_fichier)
        self.button_open.pack()

        # Créer un bouton quitter
        self.button_quit = tk.Button(self.frame_bottom, text="Quitter", command=tk_master.quit)
        self.button_quit.pack()

        # if self.files :
        #     for line in self.files:
        #         self.files_entry.insert(tk.END, str(line) + "\n\n")

        for line in self.text:
            self.text_area.insert(tk.END, str(line) + "\n\n")

        # Créer une barre pour menu déroulant et y insérer des menus.
        menu_bar = tk.Menu(tk_master)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Ouvrir un fichier...", command=ouvrir_fichier)
        file_menu.add_command(label="Fermer le fichier")
        file_menu.add_command(label="Quitter l'application", command=root.quit)

        menu_bar.add_cascade(label="Fichier", menu=file_menu)

        # Configurer la fenêtre principale pour utiliser la barre de menus
        self.tkmaster.config(menu=menu_bar)
        self.tkframe.pack()

    def traitement1(self):
        txt_in = self.text_area.selection_get()

        print("Entrée : ", txt_in)
        txt_out = fonction_trt(txt_in)
        print("Sortie : ", txt_out)

        first_index = self.text_area.index("sel.first")
        last_index = self.text_area.index("sel.last")

        # Remplacer la sélection par le texte en majuscules
        self.text_area.delete(first_index, last_index)
        self.text_area.insert(first_index, txt_out)


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
    root.geometry("400x400")
    app = MapApp(root, files=all_files)
    root.mainloop()
