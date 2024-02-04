from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Editor de texto")

def nuevoArchivo():
    text.delete("1.0", END)
def abrirArchivo():
    url = filedialog.askopenfilename(initialdir=".", filetypes=(("Archivos de texto", "*.txt"),), title="Abrir archivo")
    if (url != ""):
        file = open(url, "r")
        content = file.read()
        text.delete("1.0", END)
        text.insert("1.0", content)
        file.close()

def guardarArchivo():
    ubicacion = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")], title="Seleccione ubicacion")
    if (ubicacion != ""):
        content = text.get("1.0", END)
        file = open(ubicacion, "w")
        file.write(content)
        file.close()

bar = Menu(root)

file_menu = Menu(bar, tearoff=0)
file_menu.add_command(label="Nuevo", command=nuevoArchivo)
file_menu.add_separator()
file_menu.add_command(label= "Abrir", command=abrirArchivo)
file_menu.add_separator()
file_menu.add_command(label= "Guardar", command=guardarArchivo)
file_menu.add_separator()
file_menu.add_command(label= "Salir", command=root.quit)

bar.add_cascade(menu=file_menu, label="Archivo")

text = Text(root)
text.pack(fill=BOTH, expand=1)
text.config(bd=0, padx=6, pady=5, font=("Helvetica"))


root.config(menu=bar)
root.mainloop()