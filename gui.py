import tkinter as Tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
import tkinter.messagebox
from pkg import xls_VVT
import os, sys
fileDir = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(fileDir)

root=Tk.Tk()
root.geometry('700x800')
root.configure(bg='#2bab8d')
fr_input=Tk.LabelFrame(root, text="Eingabe der VVT Vorlage", padx=5, pady=5)
fr_input.grid(column=0, row=0, padx=10, pady=10)
fr_output=Tk.LabelFrame(root, text="Ausgabe", padx=5, pady=5)
fr_output.grid(column=0, row=1, padx=10, pady=10)

# Eingabe
def xls_input(v):
    if v ==1:
        global input_str
        input_str=filedialog.askopenfilename(initialdir=fileDir, title="Auswahl der alten VVT")
        label_old=Tk.Label(fr_output, text=input_str)
        label_old.grid(column=0, row=0)
    elif v==2:
        global output_str
        output_str=filedialog.askopenfilename(initialdir=fileDir, title="Auswahl der alten VVT")
        label_new=Tk.Label(fr_output, text=output_str)
        label_new.grid(column=0, row=1)

def check_vvt():
    entry=xls_VVT.readxls_main(input_str)

cmd_input=Tk.Button(fr_input, text="VVT ALT",width=20, bg='#7dcae8' , command=lambda: xls_input(1))
cmd_input.grid(column=0, row=0)
label_free=Tk.Label(fr_input, text="", width=20)
label_free.grid(column=1, row=0)
cmd_input=Tk.Button(fr_input, text="Neue VVT Version (xls)", bg='#2bab47', width=20, command=lambda: xls_input(2))
cmd_input.grid(column=2, row=0)
cmd_check=Tk.Button(fr_input, text="Überprüfung der VVTs", command=check_vvt)
cmd_check.grid(column=1, row=1)

# Ausgabe


root.mainloop()