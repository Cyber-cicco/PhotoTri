import tkinter as tk
import Fonctions
import os
import time


app_main = tk.Tk()
app_main.title("PhotoTri")
app_main.geometry("1350x610+" + str((app_main.winfo_screenwidth() - 800)//2) + "+" + str((app_main.winfo_screenheight() - 600)//2))

supprimer = tk.PhotoImage(file="Images/supprimer.png")
vider = tk.PhotoImage(file="Images/vider.png")

current_directory = Fonctions.state_of_tk()
current_directory.str_txt1 = str_txt_renamed = tk.StringVar()

frame_main = tk.Frame(app_main, padx="10", pady="10")

btn_browse = tk.Button(frame_main, text="Ouvrir", command=lambda : current_directory.ouvrir(app_main, lst_present))
btn_select = tk.Button(frame_main, text="v", command=lambda : Fonctions.select(lst_present, lst_rename), width=4, height=2)
btn_selectall = tk.Button(frame_main, text="vv", command=lambda : Fonctions.selectall(lst_present, lst_rename), width=4, height=2)
btn_delete = tk.Button(frame_main, image=supprimer, command=lambda : Fonctions.delete_1(lst_rename), height=45, width=50)
btn_deleteall = tk.Button(frame_main, image=vider, command=lambda : lst_rename.delete(0, lst_rename.size()-1), height=45, width=50)
btn_rename = tk.Button(frame_main, text="OK", command=lambda : current_directory.rename(txt_rename.get(), lst_present, lst_rename, txt_rename), width=3, height=2)
lbl_rename = tk.Label(frame_main, text="vvvvvvvvv")
lbl_image = tk.Label(app_main)
lst_present = tk.Listbox(frame_main, width=25)
lst_rename = tk.Listbox(frame_main, width=25)
txt_renamed = tk.Entry(frame_main, state='readonly', textvariable=str_txt_renamed, width=25)
txt_rename = tk.Entry(frame_main, width=25)

current_directory.start_list_index_changed_listener(lst_rename, lbl_image)
txt_rename.bind('<Return>', lambda e: current_directory.rename(txt_rename.get(), lst_present, lst_rename, txt_rename))

frame_main.grid(row=0, column=0, sticky='nw')
btn_browse.grid(row=0, sticky='w')
btn_select.grid(row=3, column=0)
btn_selectall.grid(row=3, column=2)
btn_delete.grid(row=9, column=0)
btn_deleteall.grid(row=9, column=1)
btn_rename.grid(row=9, column=2)
lbl_rename.grid(row=7, column=1)
lbl_image.grid(row=0, column=1)
lst_present.grid(row=1, rowspan=2, column=0, columnspan=3)
lst_rename.grid(row=4, rowspan=2, column=0, columnspan=3)
txt_renamed.grid(row=6, column=0, columnspan=3)
txt_rename.grid(row=8, column=0, columnspan=3)

app_main.mainloop()
current_directory.isTrue = False
time.sleep(1)
current_directory.isTrue = False
