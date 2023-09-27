# ---------------------------------------------------------------------------
# |                     TYPING LEGENDS: Typing Speed Test                   |
# ---------------------------------------------------------------------------
# | Submitted by: CASTRO, PATRICK JOSUAH          BSIS-NS-2AB               |
# |               DACQUEL, ALFREDO                                          |
# |               SALANGSANG, ARSENIC                                       |
# |                                                                         |
# | Submitted to: PROF. PERAGRINO AMADOR                                    |
# ---------------------------------------------------------------------------

from tkinter import * 
from tkinter import messagebox
import time
import threading
import random
import pygame

class TypeSpeedGUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("Typing Speed Application")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.config(bg = "#132225")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.logoScreen()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Happy.mp3")
        pygame.mixer.music.play(-1)

# ---------------------------------------------------------------------------
# | Function to display the logo screen                                     |
# ---------------------------------------------------------------------------
    def logoScreen(self):
        self.imageS = PhotoImage(file = "bgs1.png")
        self.imgLbl = Label(self, image = self.imageS)
        self.imgLbl.grid(row = 0, column = 0)

        self.logoFrame = Frame(self, bg = "#0B1922", width = 300, height = 50, highlightthickness= 4, highlightbackground= "gold", highlightcolor="gold")
        self.logoFrame.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)
        self.logoFrame.place(relx=0.5, rely=0.5, anchor='center')

        loadLabel = Label(self.logoFrame, text="TYPING\nLEGENDS", font = ("Beaufort", 36), fg = "gold", bg = "#0B1922", justify="left")
        loadLabel.grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 25, sticky = "nsew")

        self.update()
        time.sleep(1.5)
        self.logoFrame.destroy()
        self.startScreen()

# ---------------------------------------------------------------------------
# | Function to display the Start screen/Main Menu                          |
# ---------------------------------------------------------------------------
    def startScreen(self):
        self.imageS = PhotoImage(file = "bgs1.png")
        self.imgLbl = Label(self, image = self.imageS)
        self.imgLbl.grid(row = 0, column = 0)
        
        self.startframe = Frame(self,width = 300, height = 50, bg = "#0B1922", highlightthickness= 3, highlightbackground= "gold")
        self.startframe.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.startframe.place(relx=0.5, rely=0.48, anchor='center')
        
        self.title = Label(self.startframe, text="TYPING\nLEGENDS", font = ("Beaufort", 36), fg = "gold", highlightthickness= .5, highlightbackground= "gold", bg = "#0B1922", justify="left")
        self.title.grid(row = 0, column = 0, columnspan = 1, ipadx = 100, sticky = "nsew")

        start_button = Button(self.startframe, text = "S T A R T", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.loadingScreen())
        start_button.grid(columnspan = 2, pady=5)
        start_button.config(relief="solid", highlightbackground="#a1ceca", borderwidth=0)
        start_button.bind("<Enter>", self.on_enter)
        start_button.bind("<Leave>", self.on_leave)
        start_button.bind("<Button-1>", self.soundFX)

        music = Button(self.startframe, text = "M U S I C", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.music())
        music.grid(columnspan = 2, pady=5)
        music.config(relief="solid", highlightbackground="#a1ceca", borderwidth=0)
        music.bind("<Enter>", self.on_enter)
        music.bind("<Leave>", self.on_leave)
        music.bind("<Button-1>", self.soundFX)

        about = Button(self.startframe, text = "A B O U T", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.aboutDisp())
        about.grid(columnspan = 2, pady=5)
        about.config(relief="solid", highlightbackground="#a1ceca", borderwidth=0)
        about.bind("<Enter>", self.on_enter)
        about.bind("<Leave>", self.on_leave)
        about.bind("<Button-1>", self.soundFX)

        exit = Button(self.startframe, text = "E X I T", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.on_exit())
        exit.grid(columnspan = 2, pady=5)
        exit.config(relief="solid", highlightbackground="#a1ceca", borderwidth=0)
        exit.bind("<Enter>", self.on_enter)
        exit.bind("<Leave>", self.on_leave)

# ---------------------------------------------------------------------------
# | Function to display the loading screen                                  |
# ---------------------------------------------------------------------------
    def loadingScreen(self):
        self.startframe.destroy()
        self.imageS = PhotoImage(file = "bgs1.png")
        self.imgLbl = Label(self, image = self.imageS)
        self.imgLbl.grid(row = 0, column = 0)

        self.loadFrame = Frame(self, bg = "#0B1922", width = 300, height = 50, highlightthickness= 0, highlightbackground= "gold", highlightcolor="gold")
        self.loadFrame.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)
        self.loadFrame.place(relx=0.5, rely=0.5, anchor='center')

        loadLabel = Label(self.loadFrame, text = "L O A D I N G . . .", font = ("Beaufort", 18), fg = "gold", bg = "#0B1922")
        loadLabel.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = "nsew")

        self.update()
        time.sleep(2)
        self.loadFrame.destroy()
        self.widgets()

# ---------------------------------------------------------------------------
# | Function to display the test itself                                     |
# ---------------------------------------------------------------------------
    def widgets(self):
        
        self.imageS = PhotoImage(file = "bgs1.png")
        self.imgLbl = Label(self, image = self.imageS)
        self.imgLbl.grid(row = 0, column = 0)
        self.texts = open("texts.txt", "r").read().split("\n")
        
        self.frame = Frame(self, bg = "#0B1922", width = 300, height = 80, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.frame.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.frame.place(relx=0.5, rely=0.46, anchor='center')

        self.sample_label = Label(self.frame, text = random.choice(self.texts), font = ("Beaufort", 20), fg = "gold", bg = "#0B1922")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 30, sticky = "nsew")
        
        self.input_entry = Entry(self.frame, width = 45, font = ("Beaufort", 20), fg = "gray", bg = "#222629", highlightthickness= 1, highlightbackground= "gold", highlightcolor="gold")
        self.input_entry.insert(0, "Enter your text here")
        self.input_entry.bind("<FocusIn>", self.on_focus_in)
        self.input_entry.config(justify = "center")
        self.input_entry.grid(row = 1, column = 0, columnspan = 2, padx = 5, sticky = "nsew")
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = Label(self.frame, text = "0.00 CPS    0.00 CPM    0.00 WPS    0.00 WPM    0.00 s", font = ("Beaufort", 14), fg = "white", bg = "#0B1922")
        self.speed_label.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 30, sticky = "nsew")

        self.reset_button = Button(self.frame, text = "R E S E T", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.reset())
        self.reset_button.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 10, ipadx = 0)
        self.reset_button.config(relief="solid", borderwidth = 0)
        self.reset_button.bind("<Enter>", self.on_enter)
        self.reset_button.bind("<Leave>", self.on_leave)
        self.reset_button.bind("<Button-1>", self.soundFX)

        self.backframe = Frame(self, bg = "#0B1922", width = 30, height = 10, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.backframe.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0)
        self.backframe.place(relx=0.1, rely=0.9, anchor='center')

        self.back_button = Button(self.backframe, text = "B A C K", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.startScreen())
        self.back_button.grid(row = 0, column = 0, columnspan = 2, ipadx = 25)
        self.back_button.config(relief="solid", borderwidth=0)
        self.back_button.bind("<Enter>", self.on_enter)
        self.back_button.bind("<Leave>", self.on_leave)
        self.back_button.bind("<Button-1>", self.soundFX)

        self.counter = 0
        self.running = False

        self.mainloop()

# ---------------------------------------------------------------------------
# | Function to display the Music Navigation Screen                         |
# ---------------------------------------------------------------------------
    def music(self):
        self.imageS = PhotoImage(file = "bgs1.png")
        self.imgLbl = Label(self, image = self.imageS)
        self.imgLbl.grid(row = 0, column = 0)
        
        self.frame = Frame(self, bg = "#0B1922", width = 300, height = 50, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.frame.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.musiclabel = Label(self.frame, text = "M U S I C ?", font = ("Beaufort", 18), fg = "gold", bg = "#0B1922")
        self.musiclabel.grid(row = 0, column = 0, columnspan = 2, padx = 60, pady = 5)

        self.musicbutton = Button(self.frame, text="Y E S", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=self.playMusic)
        self.musicbutton.grid(row = 1, column = 0, columnspan = 2, ipadx = 60)
        self.musicbutton.config(relief="solid", borderwidth=0)
        self.musicbutton.bind("<Enter>", self.on_enter)
        self.musicbutton.bind("<Leave>", self.on_leave)
        self.musicbutton.bind("<Button-1>", self.soundFX)

        self.musicbuttonNO = Button(self.frame, text="N O", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=self.pauseMusic)
        self.musicbuttonNO.grid(row = 2, column = 0, columnspan = 2, ipadx = 60)
        self.musicbuttonNO.config(relief="solid", borderwidth=0)
        self.musicbuttonNO.bind("<Enter>", self.on_enter)
        self.musicbuttonNO.bind("<Leave>", self.on_leave)
        self.musicbuttonNO.bind("<Button-1>", self.soundFX)
        
        self.scalelabel = Label(self.frame, text="V O L U M E", font = ("Beaufort", 18), fg = "gold", bg = "#0B1922", justify = "center")
        self.scalelabel.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.scalelabel.grid(row=3)

        volume = Scale(self.frame, from_=0, to=1, resolution=0.1, orient="horizontal", activebackground="#0A323C", troughcolor="#0A323C", command=self.set_volume)
        volume.config(font = ("Beaufort", 10), bg = "#0B1922", fg = "gold", highlightthickness=0)
        volume.grid(row = 4, columnspan = 2, ipadx = 20, ipady=5)

        self.backframe = Frame(self, bg = "#0B1922", width = 30, height = 10, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.backframe.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0)
        self.backframe.place(relx=0.1, rely=0.9, anchor='center')

        self.back1_button = Button(self.backframe, text = "B A C K", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.startScreen())
        self.back1_button.grid(row = 0, column = 0, columnspan = 2, ipadx = 25)
        self.back1_button.config(relief="solid", borderwidth=0)
        self.back1_button.bind("<Enter>", self.on_enter)
        self.back1_button.bind("<Leave>", self.on_leave)
        self.back1_button.bind("<Button-1>", self.soundFX)

# ---------------------------------------------------------------------------
# | Function to display the About Screen                                    |
# ---------------------------------------------------------------------------
    def aboutDisp(self):
        self.imageS = PhotoImage(file = "bgs1.png")
        self.imgLbl = Label(self, image = self.imageS)
        self.imgLbl.grid(row = 0, column = 0)
        
        self.frame = Frame(self, bg = "#0B1922", width = 300, height = 50, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.frame.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.frame.place(relx=0.5, rely=0.3, anchor='center')

        self.title = Label(self.frame, text="This is a project made by Patrick Josuah Castro, Alfredo Dacquel and Arsenic Salangsang.\nThey are from BSIS-NS-2B of Technological University of the Philippines, Manila.\nThe theme is based from the game we love, League of Legends.\nThis program assesses your typing speed and displays the results,\n This includes the speed and accuracy of your typing.")
        self.title.config(font = ("Beaufort", 13), fg = "gold", highlightthickness= .5, highlightbackground= "gold", bg = "#0B1922", justify="center")
        self.title.grid(row = 0, column = 0, columnspan = 1, ipadx = 30, ipady = 20, sticky = "nsew")

        self.frame = Frame(self, width = 110, height = 110, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.frame.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.frame.place(relx=0.3, rely=0.6, anchor='center')

        self.imageS1 = PhotoImage(file = "Pat.png")
        self.imgLbl = Label(self, image = self.imageS1)
        self.imgLbl.place (relx=0.3, rely=0.6, anchor='center')

        self.label =Label(self, text = "CASTRO, PATRICK JOSUAH", bg = "#0B1922", fg = "gold", font = ("Beaufort", 8))
        self.label.place(relx = 0.3, rely=0.72, anchor='center')
        
        self.frame = Frame(self, width = 110, height = 110, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.frame.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.frame.place(relx=0.5, rely=0.6, anchor='center')

        self.imageS2 = PhotoImage(file = "Dac.png")
        self.imgLbl = Label(self, image = self.imageS2)
        self.imgLbl.place (relx=0.5, rely=0.6, anchor='center')

        self.label =Label(self, text = "DACQUEL, ALFREDO", bg = "#0B1922", fg = "gold", font = ("Beaufort", 8))
        self.label.place(relx = 0.5, rely=0.72, anchor='center')

        self.frame = Frame(self, width = 110, height = 110, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.frame.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.frame.place(relx=0.7, rely=0.6, anchor='center')

        self.imageS3 = PhotoImage(file = "Ars.png")
        self.imgLbl = Label(self, image = self.imageS3)
        self.imgLbl.place (relx=0.7, rely=0.6, anchor='center')

        self.label =Label(self, text = "SALANGSANG, ARSENIC", bg = "#0B1922", fg = "gold", font = ("Beaufort", 8))
        self.label.place(relx = 0.7, rely=0.72, anchor='center')
        
        self.backframe = Frame(self, bg = "#0B1922", width = 30, height = 10, highlightthickness= 2, highlightbackground= "gold", highlightcolor="gold")
        self.backframe.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0)
        self.backframe.place(relx=0.1, rely=0.9, anchor='center')

        self.back1_button = Button(self.backframe, text = "B A C K", font = ("Beaufort", 12), fg = "#C89B3C", bg = "#0B1922", activebackground= "#0B1922", activeforeground= "gold", command=lambda: self.startScreen())
        self.back1_button.grid(row = 0, column = 0, columnspan = 2, ipadx = 25)
        self.back1_button.config(relief="solid", borderwidth=0)
        self.back1_button.bind("<Enter>", self.on_enter)
        self.back1_button.bind("<Leave>", self.on_leave)
        self.back1_button.bind("<Button-1>", self.soundFX)

# ------------------------------------------------------------------------------------------------------
# | Function to display a message box and ask the user for confirmation before exiting the application |
# ------------------------------------------------------------------------------------------------------
    def on_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()
            
# ---------------------------------------------------------------------------
# | Function to setting the volume of the music                             |
# ---------------------------------------------------------------------------
    def set_volume(self, val):
        volume_value = float(val)
        pygame.mixer.music.set_volume(volume_value)

# ---------------------------------------------------------------------------
# | Function for sound effect when a button is pressed                      |
# ---------------------------------------------------------------------------
    def soundFX(self, event):
        self.play_sound()

# ---------------------------------------------------------------------------
# | Function to call and play the sound effect of the button                |
# ---------------------------------------------------------------------------
    def play_sound(self):
        button_sound = pygame.mixer.Sound("click.wav")
        button_sound.set_volume(0.3)
        button_sound.play()

# ---------------------------------------------------------------------------
# | Function to delete "Enter your text here" on the input widget          |
# ---------------------------------------------------------------------------
    def on_focus_in(self, event):
        # Delete the placeholder text when the Entry widget is focused
        event.widget.delete(0, END)

# ---------------------------------------------------------------------------
# | Function to change the color of a button when hover                     |
# ---------------------------------------------------------------------------
    def on_enter(self, event):
        event.widget.config(fg = "gold")

# ---------------------------------------------------------------------------
# | Function to bring back the color of a button when the cursor leaves     |
# ---------------------------------------------------------------------------
    def on_leave(self, event):
        event.widget.config(fg = "#C89B3C")

# ---------------------------------------------------------------------------
# | Function to play the music when a button is pressed                     |
# ---------------------------------------------------------------------------
    def playMusic(self):
            pygame.mixer.music.play()

# ---------------------------------------------------------------------------
# | Function to pause the music when a button is pressed                    |
# ---------------------------------------------------------------------------
    def pauseMusic(self):
            pygame.mixer.music.pause()

# ---------------------------------------------------------------------------
# | Function to start the timer when the user types on the input widget     |
# ---------------------------------------------------------------------------
    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target = self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg = "#C3073F")
        else:
            self.input_entry.config(fg = "white")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg = "green")

# -----------------------------------------------------------------------
# | Function to count the time and accuracy of the user when typing     |
# -----------------------------------------------------------------------
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text = f"{cps: .2f} CPS    {cpm: .2f} CPM    {wps: .2f} WPS    {wpm: .2f} WPM {self.counter: .2f} s", fg = "white") 

# -----------------------------------------------------------------------
# | Function to reset the test sentence that the user is copying        |
# -----------------------------------------------------------------------
    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text = "0.00 CPS    0.00 CPM    0.00 WPS    0.00 WPM    0.00s")
        self.sample_label = Label(self.frame, text = random.choice(self.texts), font = ("Beaufort", 20), fg = "gold", bg = "#0B1922")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 30, sticky = "nsew")
        self.input_entry = Entry(self.frame, width = 45, font = ("Beaufort", 20), fg = "gray", bg = "#222629", highlightthickness= 1, highlightbackground= "gold", highlightcolor="gold")
        self.input_entry.insert(0, "Enter your text here")
        self.input_entry.bind("<FocusIn>", self.on_focus_in)
        self.input_entry.config(justify = "center")
        self.input_entry.grid(row = 1, column = 0, columnspan = 2, padx = 5, sticky = "nsew")
        self.input_entry.bind("<KeyRelease>", self.start)

type = TypeSpeedGUI()
type.startScreen()
type.mainloop()