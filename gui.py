import tkinter as Tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
import tkinter.messagebox
from pkg import xls_VVT
from pkg import VVT_check, TOM_check, TODO_check, write_xls
import os, sys
fileDir = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(fileDir)

root=Tk.Tk()
root.geometry('800x300')
root.configure(bg='#2bab8d')
fr_input=Tk.LabelFrame(root, text="Eingabe der VVT Vorlage", padx=5, pady=5)
fr_input.grid(column=0, row=0, padx=10, pady=10)
fr_output=Tk.LabelFrame(root, text="Ausgabe", padx=5, pady=5)
fr_output.grid(column=0, row=1, padx=10, pady=10)

# Eingabe
def xls_input(v):
    if v ==1:
        global oldXLS_str
        oldXLS_str=filedialog.askopenfilename(initialdir=fileDir, title="Auswahl der alten VVT")
        label_old=Tk.Label(fr_output, text=oldXLS_str)
        label_old.grid(column=0, row=0)
    elif v==2:
        global newXLS_str
        newXLS_str=filedialog.askopenfilename(initialdir=fileDir, title="Auswahl der neuen VVT")
        label_new=Tk.Label(fr_output, text=newXLS_str)
        label_new.grid(column=0, row=1)

def check_vvt():
    xls_old=xls_VVT.readxls_main(oldXLS_str)
    xls_new=xls_VVT.readxls_main(newXLS_str)
    vvt_return=VVT_check.main(xls_old, xls_new)
    tom_return=TOM_check.main(xls_old, xls_new)
    ToDo_return=TODO_check.main(xls_old, xls_new)
    str_datei=entry_name.get()
    write_xls.print_xls(vvt_return, tom_return, ToDo_return, str_datei)
    if len(str_datei) > 0 :
        Tk.messagebox.showinfo(title='Success', message=f"Die Datei {str_datei} wurde erstellt")
    else: 
        Tk.messagebox.showinfo(title='Success', message=f"Die Datei wurde erstellt")

cmd_input=Tk.Button(fr_input, text="VVT ALT",width=20, bg='#7dcae8' , command=lambda: xls_input(1))
cmd_input.grid(column=0, row=0)
label_free=Tk.Label(fr_input, text="", width=20)
label_free.grid(column=1, row=0)
cmd_input=Tk.Button(fr_input, text="Neue VVT Version (xls)", bg='#2bab47', width=20, command=lambda: xls_input(2))
cmd_input.grid(column=2, row=0)
cmd_check=Tk.Button(fr_input, text="Überprüfung der VVTs", command=check_vvt)
cmd_check.grid(column=1, row=1)
label_entry=Tk.Label(fr_input, text="")
label_entry.grid(column=0, row=2)
label_entry=Tk.Label(fr_input, text="Dateiname XLS Output")
label_entry.grid(column=0, row=3)
entry_name=Tk.Entry(fr_input, text="Dateiname", width=40)
entry_name.grid(column=1, row=3, columnspan=2)


# Ausgabe


root.mainloop()