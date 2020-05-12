import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import threading
from PIL import Image, ImageTk


class state_of_tk :
    
    isTrue = True
    img_format_list = ["jpeg", "JPEG", "png", "PNG", "gif", "GIF", 'JFIF', 'BMP', 'BAT', "jpg", "JPG"]

    def __init__(self):
        True


    def ouvrir(self, app, liste1):
        app.directory = filedialog.askdirectory()
        self.current_directory = app.directory
        self.list_of_files([], liste1)

    def rename(self, new_name, liste1, liste2, txt_2):
        try :
            oldname = self.str_txt1.get()
            os.rename(self.current_directory +'/'+ oldname, self.current_directory + '/' + new_name + '.png')
            self.list_of_files([], liste1)
            self.str_txt1.set("")
            txt_2.delete(0, len(txt_2.get()))
            liste2.delete(self.selected_index)
            liste2.select_set(self.selected_index)
        except :
            messagebox.showerror("Erreur", "Une erreur est survenue. Avez vou sélectionné un fichier?") 


    def change_img(self, liste2, img):
        image_notk = Image.open(self.current_directory + '/' + liste2.get(self.selected_index))
        image_notk = image_notk.copy()
        if image_notk.width > 1000:
            ratio = image_notk.width/1000
            image_notk = image_notk.resize((int(image_notk.width//ratio), int(image_notk.height//ratio)))
        if image_notk.height > 600:
            ratio = image_notk.height/600
            image_notk = image_notk.resize((int(image_notk.width//ratio), int(image_notk.height//ratio)))
        img2 = ImageTk.PhotoImage(image_notk)
        img.configure(image=img2)
        img.image = img2

    def list_of_files(self, rep, liste1):
        try:
            liste1.delete(0, liste1.size() - 1)
            i = 0
            del rep[:]
            for filename in os.listdir(self.current_directory):
                if '.' in filename:
                    f = filename.split('.')[1]
                    if f in self.img_format_list:
                        rep.append(filename)

            rep.sort()
            for filename in rep:
                liste1.insert(i, rep[i])
                i+=1
        except:
            True


    def start_list_index_changed_listener(self, liste2, img):
            thread1 = threading.Thread(target=lambda : self.list_index_changed_listener(liste2, img))
            thread1.start()


    def list_index_changed_listener(self, liste2, img):
        previous = -1
        while self.isTrue:
            try:
                self.selected_index = liste2.curselection()
                current_selection = liste2.get(liste2.curselection())
                if current_selection != previous:                   
                    self.change_txt_renamed(liste2)
                    self.change_img(liste2, img)
                previous = current_selection
            except:
                True
            time.sleep(0.1) 


    def change_txt_renamed(self, liste2):
        self.str_txt1.set(liste2.get(liste2.curselection()))



def select(liste1, liste2):
    try :
        selecteditem = liste1.get(liste1.curselection())
        if selecteditem not in liste2.get(0, liste2.size() - 1):
            liste2.insert(liste2.size(), selecteditem)
        else:
            messagebox.showwarning("Avertissement", "L'élément sélectionné se trouve déjà dans la seconde liste.")
    except:
        messagebox.showerror("Erreur", "Veuillez sélectionner un élément de la première liste.")


def selectall(liste1, liste2):
    i = 0
    j = liste1.size()
    liste2.delete(0, liste2.size()-1)
    while i<j:
        liste2.insert(i, liste1.get(i))
        i+=1


def delete_1(liste2):
    try:
        liste2.delete(liste2.curselection())
    except:
        messagebox.showerror("Erreur", "Veuillez saisir un élément de la seconde liste.")


