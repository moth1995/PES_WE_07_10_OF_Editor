from tkinter import Button, Entry, Frame, Label, messagebox, LabelFrame
from editor import common_functions, OptionFile

BLOCK_NAMES = [
    "Block 0", 
    "Block 1", 
    "Stadiums Names + Leagues Names",
    "Edited Players",
    "Players",
    "Boots | Shirt # | Teams Player Registration | Teams Formations",
    "Clubs",
    "Kits | Logos",
    "Emblems",
    "Block 9",
    "Block 10",
]

class ImportTab(Frame):
    def __init__(self, master, option_file:OptionFile, of2:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.of2 = of2
        self.appname = appname
        
        self.labelframe = LabelFrame(self, text="Import from OF2")
                
    def import_block_from_of2(self, block_index):
        
        self.of.of_block[block_index] = self.of2.of_block[block_index]
        
        self.of.load_of_data()
        
        self.event_generate("<<ReloadRequest>>")
        
    def publish(self):
        
        if self.of2 is None:
            Label(self.labelframe, text="First you need to open your second option file from File -> Open OF2").pack()
        else:
            for i in range(len(self.of.of_block)):
                btn = Button(
                    self.labelframe, 
                    text = f"Import {BLOCK_NAMES[i]}", 
                    command = lambda block_index = i : self.import_block_from_of2(block_index = block_index)
                )
                btn.pack(fill = "x", padx = "100", pady=2)

        self.labelframe.pack(padx=100, pady=20, ipady=20, fill="both")

