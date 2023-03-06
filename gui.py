#pip install tkinker
#pip install customtkinter

from tkinter import *
import customtkinter 


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.layout()
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


    def layout(self):
        # configure window
        self.title("Demo application")
        self.geometry(f"{1100}x{820}")

        # configure grid layout for horizontal and vertical tabs
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        
        # create sidebar frame with widgets
        self.sidebar_framev = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_framev.grid(row=0, column=0, rowspan=3, sticky="ns", pady=(0,20))

        self.sidebar_frameh = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frameh.grid(row=0, column=1,rowspan=1,columnspan=4, sticky="ew")
        self.sidebar_frameh.grid_rowconfigure(1, weight=1)
        
        self.startStopFrame  =customtkinter.CTkFrame(self.sidebar_frameh, corner_radius=25)
        self.startStopFrame.pack(side='top',pady=(40,10))

        #Define start stop buttons
        self.sidebar_startButton = customtkinter.CTkButton(self.startStopFrame, command=lambda : self.progressBar(False),text="Start", width=150,height=50,)
        self.sidebar_startButton.pack(side='left', padx=20, pady=(20))

        self.sidebar_stopButton = customtkinter.CTkButton(self.startStopFrame,command=lambda :self.progressBar(True) ,text="Stop", width=150,height=50)
        self.sidebar_stopButton.pack(side='left', padx=20, pady=(20))

        #Define tabs
        self.tabview = customtkinter.CTkTabview(self.sidebar_framev)
        self.tabview.pack(padx=20, pady=20,expand=True,fill='both')
        self.tabview.add("Configuration")
        self.tabview.add("Help")
        self.tabview.add("Stats")
        

        #Define Stats tab content
        self.tabviewStatsFrame = customtkinter.CTkFrame(self.tabview.tab("Stats"),fg_color="transparent")
        self.tabviewStatsFrame.pack(padx=0, pady=0,expand=True,fill='both')
        self.label_statsTitle = customtkinter.CTkLabel(self.tabviewStatsFrame, text="Statistics:",font=('Helvetica', 16, 'bold'))
        self.label_statsTitle.pack(padx=0, pady=(0,0),side="top")
        self.textbox_followback = customtkinter.CTkTextbox(self.tabviewStatsFrame,height=670,wrap="word")
        self.textbox_followback.pack( padx=0, pady=(20,10),side="top", fill='x')
        self.textbox_followback.insert(index="end",text="Currently there is no statistic to display.")


        #Define Help tab content
        self.tabviewHelpFrame = customtkinter.CTkFrame(self.tabview.tab("Help"),fg_color="transparent")
        self.tabviewHelpFrame.pack(padx=0, pady=0,expand=True,fill='both')
        self.label_helpTitle = customtkinter.CTkLabel(self.tabviewHelpFrame, text="Basic info to get you started ",font=('Helvetica', 16, 'bold'))
        self.label_helpTitle.pack(padx=0, pady=(0,0),side="top")
        self.textbox_help = customtkinter.CTkTextbox(self.tabviewHelpFrame,height=670,wrap="word")
        self.textbox_help.pack( padx=0, pady=(20,10),side="top", fill='x')
        helpText="Just a help textbox\n\n"
        self.textbox_help.insert(index="end",text=helpText )


        #Define Configuration tab content
        self.tabviewConfigFrame = customtkinter.CTkFrame(self.tabview.tab("Configuration"),fg_color="transparent")
        self.tabviewConfigFrame.pack(padx=0, pady=0,expand=True,fill='both')

        self.sidebar_button1 = customtkinter.CTkButton(self.tabviewConfigFrame,text="Demo button 1")
        self.sidebar_button1.pack(side='top',fill='x', padx=20, pady=(20,0))
        self.label_EntryBoxName = customtkinter.CTkLabel(self.tabviewConfigFrame, text="Demo label for entrybox")
        self.label_EntryBoxName.pack(padx=0, pady=(20,0),side="top", fill='x')
        self.entryBox_Demo = customtkinter.CTkEntry(self.tabviewConfigFrame, placeholder_text="Demo entry box")
        self.entryBox_Demo.pack(padx=0, pady=(0,10),side="top", fill='x')


        self.label_slider1 = customtkinter.CTkLabel(self.tabviewConfigFrame, text="Demo label for slider 1")
        self.label_slider1.pack(padx=0, pady=(0,0),side="top", fill='x')
        self.slider_slider1 = customtkinter.CTkSlider(self.tabviewConfigFrame, from_=0, to=100, number_of_steps=20)
        self.label_slider1Value = customtkinter.CTkLabel(self.tabviewConfigFrame, text=int(self.slider_slider1.get()))
        self.label_slider1Value.pack(padx=0, pady=(0,0),side="top", fill='x')
        self.slider_slider1.bind("<ButtonRelease-1>", command=lambda a: [self.label_slider1Value.configure(text=int(self.slider_slider1.get()))])
        self.slider_slider1.pack(padx=0, pady=(0,10),side="top", fill='x')

        self.label_segmentedButton1 = customtkinter.CTkLabel(self.tabviewConfigFrame, text="Demo label for segmented button")
        self.label_segmentedButton1.pack(padx=0, pady=(0,0),side="top", fill='x')
        self.seg_button_segmentedButton1 = customtkinter.CTkSegmentedButton(self.tabviewConfigFrame)
        self.seg_button_segmentedButton1.pack(padx=0, pady=(0,10),side="top", fill='x')
        self.seg_button_segmentedButton1.configure(values=["Choice 1", "Choice 2", "Choice 3"])
        self.seg_button_segmentedButton1.set("Choice 1")
         
        self.label_textbox1 = customtkinter.CTkLabel(self.tabviewConfigFrame, text="Demo label for textbox 1")
        self.label_textbox1.pack(padx=0, pady=(10,0),side="top", fill='x')
        self.textbox_textbox1 = customtkinter.CTkTextbox(self.tabviewConfigFrame,height=60,wrap="word")
        self.textbox_textbox1.pack( padx=0, pady=(0,10),side="top", fill='x')

        self.label_textbox2 = customtkinter.CTkLabel(self.tabviewConfigFrame, text="Demo label for textbox2")
        self.label_textbox2.pack(padx=0, pady=(10,0),side="top", fill='x')
        self.textbox_textbox2 = customtkinter.CTkTextbox(self.tabviewConfigFrame,height=60,wrap="word")
        self.textbox_textbox2.pack( padx=0, pady=(0,10),side="top", fill='x')

        self.label_slider2 = customtkinter.CTkLabel(self.tabviewConfigFrame, text="Demo label for slider 2")
        self.label_slider2.pack(padx=0, pady=(0,0),side="top", fill='x')
        self.slider_slider2 = customtkinter.CTkSlider(self.tabviewConfigFrame, from_=0, to=5, number_of_steps=5)
        self.label_slider2Value = customtkinter.CTkLabel(self.tabviewConfigFrame, text=int(self.slider_slider2.get()))
        self.label_slider2Value.pack(padx=0, pady=(0,0),side="top", fill='x')
        self.slider_slider2.bind("<ButtonRelease-1>", command=lambda a: [self.label_slider2Value.configure(text=int(self.slider_slider2.get()))])
        self.slider_slider2.pack(padx=0, pady=(0,10),side="top", fill='x')

        self.checkbox_checkbox1 = customtkinter.CTkCheckBox(master=self.tabviewConfigFrame,text="Demo text for checkbox")
        self.checkbox_checkbox1.pack(padx=0, pady=(10,0),side="top", fill='x')

        self.sidebar_button_writeToConfig = customtkinter.CTkButton(self.tabviewConfigFrame,text="Demo button 2")
        self.sidebar_button_writeToConfig.pack(side='top',fill='x', padx=20, pady=(20))
        
        # create main textbox
        self.textbox_MainDescription = customtkinter.CTkTextbox(self,wrap="word")
        self.textbox_MainDescription.grid(row=1, column=1,rowspan=2, columnspan=3, padx=20, pady=20, sticky="nsew")
        
        # set default values
        self.textbox_MainDescription.insert(index=0.0,text="After the start, script logs will be displayed here.")


    def progressBar(self,destroy):
        if destroy: 
            self.progressbar_RunningScript.destroy()
            return
        self.progressbar_RunningScript = customtkinter.CTkProgressBar(self.sidebar_frameh)
        self.progressbar_RunningScript.pack(side='bottom', padx=20, pady=20)
        self.progressbar_RunningScript.configure(mode="indeterminnate")
        self.progressbar_RunningScript.start()    



app = App()
app.mainloop()

