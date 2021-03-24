#Work on progress!
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


class Menubar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 14)

        #File
        menubar = tk.Menu(parent.root, font = font_specs,tearoff=0)
        parent.root.config(menu=menubar)

        file_dropdown = tk.Menu(menubar)
        file_dropdown.add_command(label="New file")
        file_dropdown.add_command(label="Open file")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save", command=parent.save)
        file_dropdown.add_command(label="Save as", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit")

        menubar.add_cascade(label="File",menu=file_dropdown)

        #Help
        parent.root.config(menu=menubar)

        about_dropdown = tk.Menu(menubar)
        about_dropdown.add_command(label="about")


        menubar.add_cascade(label="Help",menu=about_dropdown)





class PyText:
    def __init__(self, root):
        root.title("Untitled - PyText")
        root.geometry('1200x700')

        font_specs = ("ubuntu", 18)

        self.root = root

        self.textarea = tk.Text(root, font=font_specs)
        self.scroll = tk.Scrollbar(root, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)

    def save_as(self):
        data = self.textarea.get(1.0, tk.END)
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css")])

            with open(new_file, "w") as f:
                f.write(data)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)

        except:
            pass

    def save(self):
        try:
            if self.filename != '':
                data = self.textarea.get(1.0, tk.END)
                with open(self.filename, 'w'):
                    f.write(data)


        except:
            self.save_as()




if __name__ == '__main__':
    root = tk.Tk()
    pt = PyText(root)
    root.mainloop()