import os.path
import shutil
import sys
import tkinter as tk
import supportFile

_script = sys.argv[0]
_location = os.path.dirname(_script)


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'


class Toplevel1:

    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""

        top.geometry("962x603+448+175")
        top.minsize(120, 1)
        top.maxsize(5764, 1249)
        top.resizable(1, 1)
        top.title("2020 Catalog Remover")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Listbox1 = tk.Listbox(self.top)
        self.Listbox1.place(relx=0.333, rely=0.033, relheight=0.915
                            , relwidth=0.638)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(selectmode="extended")

        self.V11Button = tk.Button(self.top)
        self.V11Button.place(relx=0.114, rely=0.299, height=24, width=97)
        self.V11Button.configure(activebackground="beige")
        self.V11Button.configure(activeforeground="black")
        self.V11Button.configure(background="#d9d9d9")
        self.V11Button.configure(compound='left')
        self.V11Button.configure(disabledforeground="#a3a3a3")
        self.V11Button.configure(foreground="#000000")
        self.V11Button.configure(highlightbackground="#d9d9d9")
        self.V11Button.configure(highlightcolor="black")
        self.V11Button.configure(pady="0")
        self.V11Button.configure(text='''Version 11 Scan''')
        self.V11Button.configure(command=lambda: scanfiles(self, 11))

        self.V12Button = tk.Button(self.top)
        self.V12Button.place(relx=0.114, rely=0.348, height=24, width=97)
        self.V12Button.configure(activebackground="beige")
        self.V12Button.configure(activeforeground="black")
        self.V12Button.configure(background="#d9d9d9")
        self.V12Button.configure(compound='left')
        self.V12Button.configure(disabledforeground="#a3a3a3")
        self.V12Button.configure(foreground="#000000")
        self.V12Button.configure(highlightbackground="#d9d9d9")
        self.V12Button.configure(highlightcolor="black")
        self.V12Button.configure(pady="0")
        self.V12Button.configure(text='''Version 12 Scan''')
        self.V12Button.configure(command=lambda: scanfiles(self, 12))

        self.V13Button = tk.Button(self.top)
        self.V13Button.place(relx=0.114, rely=0.398, height=24, width=97)
        self.V13Button.configure(activebackground="beige")
        self.V13Button.configure(activeforeground="black")
        self.V13Button.configure(background="#d9d9d9")
        self.V13Button.configure(compound='left')
        self.V13Button.configure(disabledforeground="#a3a3a3")
        self.V13Button.configure(foreground="#000000")
        self.V13Button.configure(highlightbackground="#d9d9d9")
        self.V13Button.configure(highlightcolor="black")
        self.V13Button.configure(pady="0")
        self.V13Button.configure(text='''Version 13 Scan''')
        self.V13Button.configure(command=lambda: scanfiles(self, 13))

        self.DeleteButton = tk.Button(self.top)
        self.DeleteButton.place(relx=0.062, rely=0.846, height=24, width=207)
        self.DeleteButton.configure(activebackground="#ff040b")
        self.DeleteButton.configure(activeforeground="black")
        self.DeleteButton.configure(background="#ff040b")
        self.DeleteButton.configure(compound='left')
        self.DeleteButton.configure(disabledforeground="#a3a3a3")
        self.DeleteButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.DeleteButton.configure(foreground="#000000")
        self.DeleteButton.configure(highlightbackground="#d9d9d9")
        self.DeleteButton.configure(highlightcolor="black")
        self.DeleteButton.configure(pady="0")
        self.DeleteButton.configure(text='''DELETE''')
        self.DeleteButton.configure(command=lambda: deletefolders(self))

        self.InstructionMessage = tk.Message(self.top)
        self.InstructionMessage.place(relx=0.052, rely=0.066, relheight=0.164
                                      , relwidth=0.239)
        self.InstructionMessage.configure(background="#d9d9d9")
        self.InstructionMessage.configure(foreground="#000000")
        self.InstructionMessage.configure(highlightbackground="#d9d9d9")
        self.InstructionMessage.configure(highlightcolor="black")
        self.InstructionMessage.configure(padx="1")
        self.InstructionMessage.configure(pady="1")
        self.InstructionMessage.configure(
            text='''Please click your installed version of 2020, then once the folders to the left are shown, select all 
            that you want to delete, then click DELETE.''')
        self.InstructionMessage.configure(width=230)

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


def scanfiles(self, version):
    self.Listbox1.delete('0', 'end')
    if version == 11:
        dirName = 'C:\\ProgramData\\20-20 Technologies\\Cat\\Common'
    if version == 12:
        dirName = 'C:\\ProgramData\\2020\\Design\\12\\Cat\\Common'
    if version == 13:
        dirName = 'C:\\ProgramData\\2020\\Design\\13\\Cat\\Common'

    try:
        listOfFile = os.listdir(dirName)
    except:
        self.InstructionMessage.configure(text='You do not have this version installed')
    all_files = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        full_path = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path) and '-' in entry:
            all_files.append(full_path)

    for i in range(len(all_files)):
        self.Listbox1.insert(i, all_files[i])


def deletefolders(self):
    for i in reversed(self.Listbox1.curselection()):
        shutil.rmtree(self.Listbox1.get(i))
        self.Listbox1.delete(i)
        self.Listbox1.update()


def start_up():
    supportFile.main()


if __name__ == '__main__':
    supportFile.main()
