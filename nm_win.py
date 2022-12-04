import tkinter as tk
import customtkinter as ck


class App(ck.CTk):

    WIDTH = 1300
    HEIGHT = 700

    WPM_MIN = 5
    WPM_MAX = 100
    WPM_INIT = 40

    TONE_MIN = 50
    TONE_MAX = 15000
    TONE_INIT = 400

    def __init__(self):
        super().__init__()

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.title("NATO Phonetics and Morse Code")
        self.iconbitmap("nm_gold_icon.ico")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ***   Create the menu bar   *** #
        menu = tk.Menu()
        self.config(menu=menu)

        # Create the File menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Text & Phonetics", font=("Sans Serif", 13), command=self.save_text_phonetics)
        file_menu.add_command(label="Save Morse", font=("Sans Serif", 13), command=self.save_morse)
        file_menu.add_command(label="Save Config", font=("Sans Serif", 13), command=self.save_config)
        file_menu.add_command(label="Load Config", font=("Sans Serif", 13), command=self.load_config)
        file_menu.add_command(label="Print", font=("Sans Serif", 13), command=self.print_nm)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", font=("Sans Serif", 13), command=self.exit_app)

        # Create the Edit menu
        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", font=("Sans Serif", 13), menu=edit_menu)
        edit_menu.add_command(label="Cut", font=("Sans Serif", 13), command=self.cut)
        edit_menu.add_command(label="Copy", font=("Sans Serif", 13), command=self.copy)
        edit_menu.add_command(label="Paste", font=("Sans Serif", 13), command=self.paste)
        edit_menu.add_command(label="Delete", font=("Sans Serif", 13), command=self.delete)
        edit_menu.add_separator()
        edit_menu.add_command(label="Copy Input Text", font=("Sans Serif", 13), command=self.copy_input)
        edit_menu.add_command(label="Copy NATO Phonetics", font=("Sans Serif", 13), command=self.copy_nato)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear Input Text", font=("Sans Serif", 13), command=self.clear_input)
        edit_menu.add_command(label="Clear NATO Phonetics", font=("Sans Serif", 13), command=self.clear_nato)
        edit_menu.add_command(label="Clear All", font=("Sans Serif", 13), command=self.clear_all)

        # Create the Convert menu
        convert_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Convert", menu=convert_menu)
        convert_menu.add_command(label="to NATO Phonetics", font=("Sans Serif", 13), command=self.nato_conversion)
        convert_menu.add_command(label="to Morse Code", font=("Sans Serif", 13), command=self.morse_conversion)

        # Create the Config menu
        config_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Config", menu=config_menu)
        config_menu.add_command(label="Appearance", font=("Sans Serif", 13), command=self.appearance)
        config_menu.add_command(label="Color Theme", font=("Sans Serif", 13), command=self.color_theme)
        config_menu.add_separator()
        config_menu.add_command(label="NATO Audio", font=("Sans Serif", 13), command=self.naudio)
        config_menu.add_command(label="NATO Voice", font=("Sans Serif", 13), command=self.voice_change)
        config_menu.add_command(label="NATO Speech Tempo", font=("Sans Serif", 13), command=self.speed_change)
        config_menu.add_command(label="Show NATO Phonetics", font=("Sans Serif", 13), command=self.visual_change)
        config_menu.add_separator()
        config_menu.add_command(label="Morse Audio", font=("Sans Serif", 13), command=self.maudio_change)
        config_menu.add_command(label="Morse Visual", font=("Sans Serif", 13), command=self.mvisual_change)
        config_menu.add_command(label="Morse Speed", font=("Sans Serif", 13), command=self.morse_speed)
        config_menu.add_command(label="Morse Tone", font=("Sans Serif", 13), command=self.morse_tone)
        config_menu.add_separator()
        config_menu.add_command(label="Advanced Settings", font=("Sans Serif", 13), command=self.advanced)
        config_menu.add_separator()
        config_menu.add_command(label="Reset Settings", font=("Sans Serif", 13), command=self.reset_settings)
        config_menu.add_command(label="Reset Settings & Clear UI", font=("Sans Serif", 13), command=self.reset_all)
        config_menu.add_command(label="Factory Reset", font=("Sans Serif", 13), command=self.factory_reset)

        # Create the Help menu
        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help", font=("Sans Serif", 13), command=self.nm_help)
        help_menu.add_separator()
        help_menu.add_command(label="About", font=("Sans Serif", 13), command=self.nm_about)

        # ***** -----     CREATE THE GUI     ----- ***** #
        # Create the grid system
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=2)

        # ***   Input Text Area   *** #
        # Input Text Label
        self.input_text_label = ck.CTkLabel(master=self, text="Input Text:", font=("Arial Bold", 16))
        self.input_text_label.grid(row=1, column=0, sticky="sw", padx=25, pady=(10, 0))

        # Input Textbox
        self.text = ck.StringVar(value="Hello")
        self.input_text = ck.CTkTextbox(master=self, font=("Arial", 16))
        self.input_text.grid(row=2, column=0, columnspan=5, padx=20, pady=(5, 10), sticky="nsew")

        # ***   Output Text Area   *** #
        # Output Label
        self.output_text_label = ck.CTkLabel(master=self, text="NATO Phonetics:", font=("Arial Bold", 16))
        self.output_text_label.grid(row=3, column=0, sticky="sw", padx=25, pady=(10, 0))

        # Output Area
        self.output_frame = ck.CTkFrame(master=self)
        self.output_frame.grid(row=4, column=0, columnspan=5, padx=20, pady=(5, 0), sticky="nsew")

        self.nato_text = ck.StringVar(value="")
        self.nato_output = ck.CTkLabel(master=self.output_frame, text="", text_color="red",
                                       font=("Arial Bold", 16), textvariable=self.nato_text)
        self.nato_output.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="nsew")

        # ***   NATO Frame   *** #
        # Place the frame & Create the grid system
        self.nato_frame = ck.CTkFrame(master=self)
        self.nato_frame.grid(row=6, column=0, sticky="nsew", padx=(20, 10), pady=20)

        self.nato_frame.grid_columnconfigure(2, weight=1)
        self.nato_frame.grid_columnconfigure(6, weight=1)
        self.nato_frame.grid_columnconfigure(3, weight=0)
        self.nato_frame.grid_columnconfigure(4, weight=0)
        self.nato_frame.grid_columnconfigure(5, weight=0)

        # NATO Button
        self.nato_button = ck.CTkButton(master=self.nato_frame, text="NATO", command=self.nato_conversion)
        self.nato_button.grid(row=1, column=1, sticky="nwe", padx=20)

        # Audio Switch
        self.naudio_label = ck.CTkLabel(master=self.nato_frame, text="Audio")
        self.naudio_label.grid(row=0, column=4, sticky="sew", pady=(15, 0))

        self.naudio_off_label = ck.CTkLabel(master=self.nato_frame, text="Off", width=0)
        self.naudio_off_label.grid(row=1, column=3, sticky="ne")

        self.naudio = ck.StringVar(value="on")

        self.naudio_switch = ck.CTkSwitch(master=self.nato_frame, text="", width=50, variable=self.naudio,
                                          switch_width=50,
                                          offvalue="off", onvalue="on", command=self.naudio_change)
        self.naudio_switch.grid(row=1, column=4, sticky="n", padx=(20, 10))

        self.naudio_on_label = ck.CTkLabel(master=self.nato_frame, text="On", width=0)
        self.naudio_on_label.grid(row=1, column=5, sticky="nw")

        # Voice Switch
        self.voice_label = ck.CTkLabel(master=self.nato_frame, text="Voice")
        self.voice_label.grid(row=2, column=4, sticky="sew", pady=(10, 0))

        self.male_label = ck.CTkLabel(master=self.nato_frame, text="Male", width=0)
        self.male_label.grid(row=3, column=3, sticky="ne")

        self.voice = ck.StringVar(value="female")

        self.voice_switch = ck.CTkSwitch(master=self.nato_frame, text="", width=50, variable=self.voice,
                                         switch_width=50,
                                         offvalue="male", onvalue="female", command=self.voice_change)
        self.voice_switch.grid(row=3, column=4, sticky="n", padx=(20, 10))

        self.female_label = ck.CTkLabel(master=self.nato_frame, text="Female", width=0)
        self.female_label.grid(row=3, column=5, sticky="nw")

        # Speed Switch
        self.speed_label = ck.CTkLabel(master=self.nato_frame, text="Speed")
        self.speed_label.grid(row=4, column=4, sticky="sew", pady=(10, 0))

        self.slow_label = ck.CTkLabel(master=self.nato_frame, text="Slow", width=0)
        self.slow_label.grid(row=5, column=3, sticky="ne")

        self.voice_speed = ck.StringVar(value="normal")

        self.speed_switch = ck.CTkSwitch(master=self.nato_frame, text="", width=50, variable=self.voice_speed,
                                         switch_width=50,
                                         offvalue="slow", onvalue="normal", command=self.speed_change)
        self.speed_switch.grid(row=5, column=4, sticky="n", padx=(20, 10))

        self.normal_label = ck.CTkLabel(master=self.nato_frame, text="Normal", width=0)
        self.normal_label.grid(row=5, column=5, sticky="nw")

        # Visual Switch
        self.visual_label = ck.CTkLabel(master=self.nato_frame, text="Visual")
        self.visual_label.grid(row=6, column=4, sticky="sew", pady=(10, 0))

        self.off_label = ck.CTkLabel(master=self.nato_frame, text="Off", width=0)
        self.off_label.grid(row=7, column=3, sticky="ne")

        self.show_phonetics = ck.StringVar(value="on")

        self.visual_switch = ck.CTkSwitch(master=self.nato_frame, text="", width=50, variable=self.show_phonetics,
                                          switch_width=50,
                                         offvalue="off", onvalue="on", command=self.visual_change)
        self.visual_switch.grid(row=7, column=4, sticky="n", padx=(20, 10), pady=(0, 20))

        self.on_label = ck.CTkLabel(master=self.nato_frame, text="On", width=0)
        self.on_label.grid(row=7, column=5, sticky="nw")

        self.language = ck.CTkComboBox(master=self.nato_frame,
                                       values=["English (US)", "English (UK)", "English (India),",
                                               "English (Australia)"])
        self.language.grid(row=1, column=7, sticky="nwe", padx=20)

        # Language Combobox
        self.language = ck.CTkComboBox(master=self.nato_frame, width=200,
                                       values=["English (United States)",
                                               "English (Australia)",
                                               "English (United Kingdom)",
                                               "English (Canada)",
                                               "English (India)",
                                               "English (Ireland)",
                                               "English (South Africa)",
                                               "French (Canada)",
                                               "French (France)",
                                               "Mandarin (China Mainland)",
                                               "Mandarin (Taiwan)",
                                               "Portuguese (Brazil)",
                                               "Portuguese (Portugal)",
                                               "Spanish (Mexico)",
                                               "Spanish (Spain)",
                                               "Spanish (United States)"])
        self.language.grid(row=1, column=7, sticky="nwe", padx=20)

        # ***   Morse Frame   *** #
        # Place the frame & Create the grid system
        self.morse_frame = ck.CTkFrame(master=self)
        self.morse_frame.grid(row=6, column=4, sticky="nswe", padx=(10, 20), pady=20)

        self.morse_frame.grid_rowconfigure(4, minsize=20)
        self.morse_frame.grid_columnconfigure((2, 6), weight=1)

        # Morse Button
        self.morse_button = ck.CTkButton(master=self.morse_frame, text="Morse", command=self.morse_conversion)
        self.morse_button.grid(row=1, column=1, sticky="nwe", padx=(20, 0))

        # Morse Audio Switch
        self.audio_label = ck.CTkLabel(master=self.morse_frame, text="Audio")
        self.audio_label.grid(row=0, column=4, sticky="sew", pady=(15, 0))

        self.aoff_label = ck.CTkLabel(master=self.morse_frame, text="Off", width=0)
        self.aoff_label.grid(row=1, column=3, sticky="ne")

        self.morse_audio = ck.StringVar(value="on")

        self.audio_switch = ck.CTkSwitch(master=self.morse_frame, text="", width=50, variable=self.morse_audio,
                                         switch_width=50,
                                         offvalue="off", onvalue="on", command=self.maudio_change)
        self.audio_switch.grid(row=1, column=4, sticky="n", padx=(20, 10))

        self.aon_label = ck.CTkLabel(master=self.morse_frame, text="On", width=0)
        self.aon_label.grid(row=1, column=5, sticky="nw")

        # Morse Visual Switch
        self.mvisual_label = ck.CTkLabel(master=self.morse_frame, text="Visual")
        self.mvisual_label.grid(row=2, column=4, sticky="sew", pady=(10, 0))

        self.moff_label = ck.CTkLabel(master=self.morse_frame, text="Off", width=0)
        self.moff_label.grid(row=3, column=3, sticky="ne")

        self.morse_visual = ck.StringVar(value="on")

        self.mvisual_switch = ck.CTkSwitch(master=self.morse_frame, text="", width=50, variable=self.morse_visual,
                                           switch_width=50,
                                         offvalue="off", onvalue="on", command=self.mvisual_change)
        self.mvisual_switch.grid(row=3, column=4, sticky="n", padx=(20, 10))

        self.mon_label = ck.CTkLabel(master=self.morse_frame, text="On", width=0)
        self.mon_label.grid(row=3, column=5, sticky="nw")

        # Speed Slider
        self.wpm = ck.IntVar(value=self.WPM_INIT)
        self.mspeed_slider = ck.CTkSlider(master=self.morse_frame, from_=self.WPM_MIN, to=self.WPM_MAX,
                                          width=400, variable=self.wpm, command=self.mspeed_change)
        self.mspeed_slider.grid(row=6, column=1, columnspan=5, pady=(20, 0))

        self.mspeed_label = ck.CTkLabel(master=self.morse_frame, text="Speed (WPM)", width=0)
        self.mspeed_label.grid(row=6, column=6, sticky="sw", pady=(15, 0))

        self.mspeed_min_label = ck.CTkLabel(master=self.morse_frame, text=str(self.WPM_MIN), width=0)
        self.mspeed_min_label.grid(row=7, column=1, sticky="nw", padx=(30, 0), pady=0)

        self.mspeed_max_label = ck.CTkLabel(master=self.morse_frame, text=str(self.WPM_MAX), width=0)
        self.mspeed_max_label.grid(row=7, column=5, sticky="ne", padx=(0, 25), pady=0)

        self.ms_entry = ck.StringVar(value=str(self.wpm.get()))
        self.mspeed_entry = ck.CTkEntry(master=self.morse_frame, placeholder_text=str(self.wpm.get()), width=50,
                                        textvariable=self.ms_entry, justify=ck.CENTER)
        self.mspeed_entry.grid(row=7, column=2, sticky="ne", padx=0, pady=(5, 10))

        self.mspeed_set_button = ck.CTkButton(master=self.morse_frame, text="Set", width=50, command=self.set_mspeed)
        self.mspeed_set_button.grid(row=7, column=3, sticky="nw", padx=(5, 0), pady=(5, 10))

        # Tone Slider
        self.tone = ck.IntVar(value=self.TONE_INIT)
        self.mtone_slider = ck.CTkSlider(master=self.morse_frame, from_=self.TONE_MIN, to=self.TONE_MAX, width=400,
                                         variable=self.tone, command=self.mtone_change)
        self.mtone_slider.grid(row=8, column=1, columnspan=5, pady=(20, 0))

        self.mtone_label = ck.CTkLabel(master=self.morse_frame, text="Tone (Hz)", width=0)
        self.mtone_label.grid(row=8, column=6, sticky="sw", pady=(15, 0))

        self.mtone_min_label = ck.CTkLabel(master=self.morse_frame, text=str(self.TONE_MIN), width=0)
        self.mtone_min_label.grid(row=9, column=1, sticky="nw", padx=(25, 0), pady=0)

        self.mtone_max_label = ck.CTkLabel(master=self.morse_frame, text=str(self.TONE_MAX), width=0)
        self.mtone_max_label.grid(row=9, column=5, sticky="ne", padx=(0, 25), pady=0)

        self.mt_entry = ck.StringVar(value=str(self.tone.get()))
        self.mtone_entry = ck.CTkEntry(master=self.morse_frame, placeholder_text=str(self.tone.get()), width=50,
                                       textvariable=self.mt_entry, justify=ck.CENTER)
        self.mtone_entry.grid(row=9, column=2, sticky="ne", padx=0, pady=(5, 10))

        self.tone_set_button = ck.CTkButton(master=self.morse_frame, text="Set", width=50, command=self.set_tone)
        self.tone_set_button.grid(row=9, column=3, sticky="nw", padx=(5, 0), pady=(5, 10))

        self.reset()

        ck.set_appearance_mode("System")
        ck.set_default_color_theme("blue")

    def reset(self):
        self.input_text.delete("0.0", "end")
        self.nato_text.set("")
        self.naudio.set("on")
        self.voice.set("female")
        self.voice_speed.set("normal")
        self.show_phonetics.set("on")
        self.language.set("English (United States)")
        self.morse_audio.set("on")
        self.morse_visual.set("on")
        self.wpm.set(self.WPM_INIT)
        self.ms_entry.set(str(self.WPM_INIT))
        self.tone.set(self.TONE_INIT)
        self.mt_entry.set(str(self.TONE_INIT))

    def save_text_phonetics(self):
        print("Save Text & Phonetics")

    def save_morse(self):
        print("Save Morse")

    def save_config(self):
        print("Save Config")

    def load_config(self):
        print("Load Config")

    def print_nm(self):
        print("Print")

    def exit_app(self):
        self.on_closing()

    def cut(self):
        print("Cut")

    def copy(self):
        print("Copy")

    def paste(self):
        print("Paste")

    def delete(self):
        print("Delete")

    def copy_input(self):
        print("Copy Input Text")

    def copy_nato(self):
        print("Copy NATO Phonetics")

    def clear_input(self):
        print("Clear Input Text")

    def clear_nato(self):
        print("Clear NATO Phonetics")

    def clear_all(self):
        print("Clear All")

    def appearance(self):
        print("Appearance")

    def color_theme(self):
        print("Color Theme")

    def nato_conversion(self):
        print("NATO Conversion")

    def naudio(self):
        print("NATO Audio On/Off")

    def naudio_change(self):
        print(self.naudio.get())

    def voice_change(self):
        print(self.voice.get())

    def speed_change(self):
        print(self.voice_speed.get())

    def visual_change(self):
        print(self.show_phonetics.get())

    def morse_conversion(self):
        print("Morse Conversion")

    def maudio_change(self):
        print(self.morse_audio.get())

    def mvisual_change(self):
        print(self.morse_visual.get())

    def mspeed_change(self, _):
        print(self.wpm.get())
        self.ms_entry.set(str(self.wpm.get()))

    def set_mspeed(self):
        print("Set mspeed (WPM)")
        self.wpm.set(int(self.ms_entry.get()))
        print(self.ms_entry.get())

    def mtone_change(self, _):
        print(self.tone.get())
        self.mt_entry.set(str(self.tone.get()))

    def set_tone(self):
        print("Set Tone")
        self.tone.set(int(self.mt_entry.get()))
        print(self.mt_entry.get())

    def morse_speed(self):
        print("Morse Speed Menu")

    def morse_tone(self):
        print("Morse Tone Menu")

    def advanced(self):
        print("Advanced Settings")

    def reset_settings(self):
        print("Reset Settings")

    def reset_all(self):
        print("Reset Settings & Clear UI")

    def factory_reset(self):
        print("Factory Reset")

    def nm_help(self):
        print("Help!")

    def nm_about(self):
        print("About")

    def on_closing(self, event=0):
        self.destroy()

    def read_text(self):
        print("Hello")


if __name__ == "__main__":
    app = App()
    app.mainloop()
