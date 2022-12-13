import tkinter as tk
import customtkinter as ck
from nato import convert_to_nato, speak_nato, text_config, speech_config


class App(ck.CTk):
    WIDTH = 1300
    HEIGHT = 900

    WPM_MIN = 5
    WPM_MAX = 100
    WPM_INIT = 40

    TONE_MIN = 50
    TONE_MAX = 15000
    TONE_INIT = 400

    MENU_FONT = ("Sans Serif", 13)

    APPEARANCES = ["system", "dark", "light"]
    THEMES = ["blue", "dark-blue", "green"]

    APPEARANCE = APPEARANCES[0]
    THEME = THEMES[0]

    def __init__(self):
        super().__init__()

        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.title("NATO Phonetics and Morse Code")
        self.iconbitmap("nm_gold_icon.ico")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.FONT = tk.font.Font(family="Arial", size=16, weight="bold")

        # ***   Create the menu bar   *** #
        menubar = tk.Menu()
        self.config(menu=menubar)

        # Create the File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Text & Phonetics", font=self.MENU_FONT, command=self.save_text_phonetics)
        file_menu.add_command(label="Save Morse", font=self.MENU_FONT, command=self.save_morse)
        file_menu.add_command(label="Save Config", font=self.MENU_FONT, command=self.save_config)
        file_menu.add_command(label="Load Config", font=self.MENU_FONT, command=self.load_config)
        file_menu.add_command(label="Print", font=self.MENU_FONT, command=self.print_nm)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", font=self.MENU_FONT, command=self.exit_app)

        # Create the Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", font=self.MENU_FONT, menu=edit_menu)
        edit_menu.add_command(label="Cut", font=self.MENU_FONT, command=lambda: self.focus_get().event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", font=self.MENU_FONT, command=lambda: self.focus_get().event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", font=self.MENU_FONT, command=lambda: self.focus_get().event_generate("<<Paste>>"))
        edit_menu.add_command(label="Delete", font=self.MENU_FONT, command=lambda: self.focus_get().event_generate("<Delete>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Copy Input Text", font=self.MENU_FONT, command=self.copy_input)
        edit_menu.add_command(label="Copy NATO Phonetics", font=self.MENU_FONT, command=self.copy_nato)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear Input Text", font=self.MENU_FONT, command=self.clear_input)
        edit_menu.add_command(label="Clear NATO Phonetics", font=self.MENU_FONT, command=self.clear_nato)
        edit_menu.add_command(label="Clear All", font=self.MENU_FONT, command=self.clear_all)

        # Create the Convert menu
        convert_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Convert", menu=convert_menu)
        convert_menu.add_command(label="to NATO Phonetics", font=self.MENU_FONT, command=self.nato_conversion)
        convert_menu.add_command(label="to Morse Code", font=self.MENU_FONT, command=self.morse_conversion)

        # Create the Config menu
        config_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Config", menu=config_menu)
        appearance_sub = tk.Menu(config_menu, tearoff=0)
        config_menu.add_cascade(label="Appearance", menu=appearance_sub, font=self.MENU_FONT)
        for a in self.APPEARANCES:
            appearance_sub.add_command(label=a.title(), font=self.MENU_FONT, command=lambda ap=a: self.appearance(ap))
        color_theme_sub = tk.Menu(config_menu, tearoff=0)
        config_menu.add_cascade(label="Color Theme", menu=color_theme_sub, font=self.MENU_FONT)
        for t in self.THEMES:
            color_theme_sub.add_command(label=t.title(), font=self.MENU_FONT, command=lambda th=t: self.theme(th))
        config_menu.add_separator()
        config_menu.add_command(label="NATO Audio", font=self.MENU_FONT, command=self.naudio_menu_cmd)
        config_menu.add_command(label="NATO Voice", font=self.MENU_FONT, command=self.voice_change)
        config_menu.add_command(label="NATO Speech Tempo", font=self.MENU_FONT, command=self.speed_change)
        config_menu.add_command(label="Show NATO Phonetics", font=self.MENU_FONT, command=self.visual_change)
        config_menu.add_separator()
        config_menu.add_command(label="Morse Audio", font=self.MENU_FONT, command=self.maudio_change)
        config_menu.add_command(label="Morse Visual", font=self.MENU_FONT, command=self.mvisual_change)
        config_menu.add_command(label="Morse Speed", font=self.MENU_FONT, command=self.morse_speed)
        config_menu.add_command(label="Morse Tone", font=self.MENU_FONT, command=self.morse_tone)
        config_menu.add_separator()
        config_menu.add_command(label="Advanced Settings", font=self.MENU_FONT, command=self.advanced)
        config_menu.add_separator()
        config_menu.add_command(label="Reset Settings", font=self.MENU_FONT, command=self.reset_settings)
        config_menu.add_command(label="Reset Settings & Clear UI", font=self.MENU_FONT, command=self.reset_all)
        config_menu.add_command(label="Factory Reset", font=self.MENU_FONT, command=self.factory_reset)

        # Create the Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help", font=self.MENU_FONT, command=self.nm_help)
        help_menu.add_separator()
        help_menu.add_command(label="About", font=self.MENU_FONT, command=self.nm_about)

        # ***** -----     CREATE THE GUI     ----- ***** #
        # Create the grid system
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=2)

        # ***   Input Text Area   *** #
        # Input Text Label
        self.input_text_label = ck.CTkLabel(master=self, text="Input Text:", font=("Arial Bold", 16))
        self.input_text_label.grid(row=1, column=0, sticky="sw", padx=25, pady=(10, 0))

        # Input Textbox
        self.input_text = ck.CTkTextbox(master=self, font=("Arial", 16))
        self.input_text.grid(row=2, column=0, columnspan=5, padx=20, pady=(5, 10), sticky="nsew")

        # ***   Output Text Area   *** #
        # Output Label
        self.output_text_label = ck.CTkLabel(master=self, text="NATO Phonetics:", font=("Arial Bold", 16))
        self.output_text_label.grid(row=3, column=0, sticky="sw", padx=25, pady=(10, 0))

        # Output Area
        self.nato_output = ck.CTkTextbox(master=self, text_color="white", font=("Arial Bold", 16), state="disabled",
                                         fg_color="#D4AF37")
        self.nato_output.grid(row=4, column=0, columnspan=5, padx=20, pady=(5, 0), sticky="nsew")

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

        self.mspeed_entry.bind("<Return>", self.set_mspeed)

        self.mspeed_set_button = ck.CTkButton(master=self.morse_frame, text="Set", width=50, command=self.set_mspeed)
        self.mspeed_set_button.grid(row=7, column=3, sticky="nw", padx=(5, 0), pady=(5, 10))

        self.mspeed_reset_button = ck.CTkButton(master=self.morse_frame, text="Reset", width=50, command=self.reset_mspeed)
        self.mspeed_reset_button.grid(row=7, column=4, sticky="nw", padx=(5, 0), pady=(5, 10))

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
        self.mtone_entry.grid(row=9, column=2, sticky="ne", padx=0, pady=(5, 20))

        self.mtone_entry.bind("<Return>", self.set_tone)

        self.tone_set_button = ck.CTkButton(master=self.morse_frame, text="Set", width=50, command=self.set_tone)
        self.tone_set_button.grid(row=9, column=3, sticky="nw", padx=(5, 0), pady=(5, 20))

        self.tone_reset_button = ck.CTkButton(master=self.morse_frame, text="Reset", width=50, command=self.reset_tone)
        self.tone_reset_button.grid(row=9, column=4, sticky="nw", padx=(5, 0), pady=(5, 20))

        # ***** -----   Set Initial State   ----- ***** #
        self.reset()
        self.appearance(self.APPEARANCE)
        self.theme(self.THEME)


    def reset(self):
        self.input_text.delete("0.0", "end")
        self.nato_output.configure(state="normal")
        self.nato_output.delete("0.0", "end")
        self.nato_output.configure(state="disabled")
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

    def appearance(self, appearance):
        self.APPEARANCE = appearance
        ck.set_appearance_mode(self.APPEARANCE)

    def theme(self, th):
        self.THEME = th
        ck.set_default_color_theme(self.THEME)

    def nato_conversion(self):
        if self.show_phonetics.get() == "on":
            text_config["show"]["current"] = True
            output = ""
            line = ""
            for word in convert_to_nato(self.input_text.get("0.0", "end")).split(text_config["word_sep"]["current"] + 2 * text_config["char_sep"]["current"]):
                if self.FONT.measure(line + text_config["word_sep"]["current"] + 2 * text_config["char_sep"]["current"] + word) < self.nato_output.winfo_width() / 1.2:
                    if line:
                        line += text_config["word_sep"]["current"] + 2 * text_config["char_sep"]["current"] + word
                    else:
                        line = word
                else:
                    if output:
                        output += "\n" + line
                    else:
                        output = line
                    line = word
            if line:
                if output:
                    output += "\n" + line
                else:
                    output = line
            self.nato_output.configure(state="normal")
            self.nato_output.delete("0.0", "end")
            self.nato_output.insert("0.0", output)
            self.nato_output.update()
            self.nato_output.configure(state="disabled")
        else:
            self.nato_output.configure(state="normal")
            self.nato_output.delete("0.0", "end")
            self.nato_output.update()
            self.nato_output.configure(state="disabled")
            text_config["show"]["current"] = False

        if self.naudio.get() == "on":
            speech_config["speak"]["current"] = True
            if self.voice.get() == "male":
                speech_config["male"]["current"] = True
            else:
                speech_config["male"]["current"] = False
            if self.voice_speed.get() == "slow":
                speech_config["speed"]["current"] = True
            else:
                speech_config["speed"]["current"] = False
            speak_nato(self.input_text.get("0.0", "end"))
        else:
            speech_config["speak"]["current"] = False

    def naudio_menu_cmd(self):
        if self.naudio.get() == "off":
            self.naudio.set("on")
        else:
            self.naudio.set("off")
        self.naudio_change()

    def naudio_change(self):
        if self.naudio.get() == "off":
            speech_config["speak"]["current"] = False
        else:
            speech_config["speak"]["current"] = True

    def voice_change(self):
        if self.voice.get() == "male":
            speech_config["male"]["current"] = True
            self.speed_switch.configure(state="disabled")
            self.speed_switch.grid_forget()
            self.speed_label.configure(text="")
            self.slow_label.configure(text="")
            self.normal_label.configure(text="")
        else:
            speech_config["male"]["current"] = False
            self.speed_switch.configure(state="normal")
            self.speed_switch.grid(row=5, column=4, sticky="n", padx=(20, 10))
            self.speed_label.configure(text="Speed")
            self.slow_label.configure(text="Slow")
            self.normal_label.configure(text="Normal")

    def speed_change(self):
        if self.voice_speed.get() == "slow":
            speech_config["speed"]["current"] = True
        else:
            speech_config["speed"]["current"] = False

    def visual_change(self):
        if self.show_phonetics.get() == "off":
            text_config["show"]["current"] = False
        else:
            text_config["show"]["current"] = True

    def morse_conversion(self):
        print("Morse Conversion")

    def maudio_change(self):
        print(self.morse_audio.get())

    def mvisual_change(self):
        print(self.morse_visual.get())

    def mspeed_change(self, _):
        print(self.wpm.get())
        self.ms_entry.set(str(self.wpm.get()))

    def set_mspeed(self, e=None):
        try:
            wpm = max(min(int(self.ms_entry.get()), self.WPM_MAX), self.WPM_MIN)
            self.wpm.set(wpm)
            self.ms_entry.set(str(wpm))
        except ValueError:
            self.ms_entry.set(str(self.wpm.get()))

    def reset_mspeed(self):
        self.wpm.set(self.WPM_INIT)
        self.ms_entry.set(str(self.WPM_INIT))

    def mtone_change(self, _):
        print(self.tone.get())
        self.mt_entry.set(str(self.tone.get()))

    def set_tone(self, e=None):
        try:
            freq = max(min(int(self.mt_entry.get()), self.TONE_MAX), self.TONE_MIN)
            self.tone.set(freq)
            self.mt_entry.set(str(freq))
        except ValueError:
            self.mt_entry.set(str(self.tone.get()))

    def reset_tone(self):
        self.tone.set(self.TONE_INIT)
        self.mt_entry.set(str(self.TONE_INIT))

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
