from tkinter import Frame,  ttk, LabelFrame, Label, IntVar, Spinbox, Button, StringVar, colorchooser
from tkinter.ttk import Combobox
from editor import Team
from editor.utils.constants import *
class KitTab(Frame):

    def __init__(self, master, team:Team, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.team = team
        self.appname = appname

        self.frame1 = ttk.Frame(self)
        self.frame1.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        self.kit_combox = Combobox(self.frame1, state="readonly", values=KIT_TYPES, )
        self.kit_combox.bind("<<ComboboxSelected>>", lambda _ : self.get_kit_info())
        self.kit_combox.set(KIT_TYPES[PA])
        self.kit_combox.grid(row=0, column=0, sticky="NWE")  
        frame_01 = LabelFrame(self, text="Menu")
        frame_01.grid(column=1, row=0, padx=5, pady=5, sticky="NWE")

        Label(frame_01, text="Option").grid(column=1, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="Type").grid(column=2, row=0, padx=5, pady=5, sticky="N")

        Label(frame_01, text="Shirt Font").grid(column=0, row=1, padx=5, pady=5,  sticky="WE")
        
        self.font_curve_cmb = ttk.Combobox(frame_01, values=FONT_CURVE,width=7,state="readonly")
        self.font_curve_cmb.grid(column=2, row=1, padx=10, pady=5, sticky="W")

        Label(frame_01, text="Short Number").grid(column=0, row=4, padx=5, pady=5, sticky="WE")

        self.short_number_pos_cmb = ttk.Combobox(frame_01, values=OFF_LEFT_RIGHT,width=5,state="readonly")
        self.short_number_pos_cmb.grid(column=1, row=4, padx=10, pady=5, sticky="W")
        
        Label(frame_01, text="Model").grid(column=0, row=6, padx=5, pady=5, sticky="WE")

        self.model_spb_var = IntVar(self, 0)

        model_spb = Spinbox(frame_01, textvariable=self.model_spb_var, from_=0, to=255, width=5)
        model_spb.grid(column=1, row=6, padx=10, pady=5, sticky="W")

        Label(frame_01, text="License").grid(column=0, row=7, padx=5, pady=5, sticky="WE")
    
        self.license_cmb = ttk.Combobox(frame_01, values=KIT_LICENSE,width=12,state="readonly")
        self.license_cmb.grid(column=1, row=7, padx=10, pady=5, sticky="W")

        Label(frame_01, text="Radar Color").grid(column=0, row=8, padx=5, pady=5, sticky="WE")
        
        self.colors_rgb_var = StringVar(self, "")

        self.btn_radar_color = Button(
            frame_01,
            width=7, 
            textvariable=self.colors_rgb_var,
            command=self.select_color
        )
        self.btn_radar_color.grid(column=1, row=8, padx=10, pady=5, sticky="W")

        frame_02 = Frame(self, )
        frame_02.grid(column=1, row=1, padx=5, pady=5, sticky="W")

        apply_btn = ttk.Button(frame_02, text="Apply", command=lambda : self.set_kit_data())
        apply_btn.grid(column=0, row=0, padx=10, pady=5)

        cancel_btn = ttk.Button(frame_02, text="Close", command=lambda : self.master.master.stop_window())
        cancel_btn.grid(column=1, row=0, padx=10, pady=5)
        
        self.kit_combox.event_generate("<<ComboboxSelected>>")

    def select_color(self):
        colors = colorchooser.askcolor(parent = self, title="Select a radar color", initialcolor=self.colors_rgb_var.get())
        if colors[0] is None :
            return 0
        self.colors_rgb_var.set(colors[1])
        self.btn_radar_color.configure(bg=colors[1])

    def get_kit_info(self):
        
        kit_list = self.team.kits.kits

        kit_type = self.kit_combox.current()
        if kit_type == 0:
            kit = kit_list[kit_type]
        elif kit_type == 1:
            kit = kit_list[kit_type]
        elif kit_type == 2:
            kit = kit_list[kit_type]
        elif kit_type == 3:
            kit = kit_list[kit_type]

        self.license_cmb.set(kit.license)
        self.model_spb_var.set(kit.model)
        self.short_number_pos_cmb.set(kit.short_number)
        self.font_curve_cmb.set(kit.font_curve)
        self.btn_radar_color.configure(bg=kit.color_radar)
        self.colors_rgb_var.set(kit.color_radar)


    def set_kit_data(self):
        
        kit_list = self.team.kits.kits

        kit_type = self.kit_combox.current()
        if kit_type == GA:
            kit = kit_list[kit_type]
        elif kit_type == PA:
            kit = kit_list[kit_type]
        elif kit_type == GB:
            kit = kit_list[kit_type]
        elif kit_type == PB:
            kit = kit_list[kit_type]

        kit.model = self.model_spb_var.get()
        kit.short_number = self.short_number_pos_cmb.get()
        kit.font_curve = self.font_curve_cmb.get()
        kit.color_radar = self.colors_rgb_var.get()

        # license has to be updated on the four set of kits
        for kit in kit_list:
            kit.license = self.license_cmb.get()

        self.team.kits.update_data()
