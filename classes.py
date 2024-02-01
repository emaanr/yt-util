import tkinter as tk
import ttkbootstrap as ttk
import functions

class App(tk.Tk):
    def __init__(self, title, minsize, geometry, maxsize):
        
    # Main Setup
        
        super().__init__() # Ensure tk.Tk is inherited properly
        ttk.Style('yt-dark')
        self.title(title)
        self.minsize(minsize[0], minsize[1])
        self.geometry(f"{geometry[0]}x{geometry[1]}")
        self.maxsize(maxsize[0], maxsize[1])

    # Widgets
        
        self.notebook = Notebook(self)
        self.tab_pdc = Tab(self.notebook, "Playlist Duration Calculator")
        self.tab_gvt = Tab(self.notebook, "Generate Video Transcript")
        self.pdc = PDC(self.tab_pdc)
        self.notebook.add_frames(self.tab_pdc, self.tab_gvt)

    # Run
        
        self.mainloop()

# Notebook Wrapper
class Notebook(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

    def add_frames(self, *tabs):
        for tab in tabs:
            self.add(tab, text=tab.tab_text)
        
        self.pack(expand=True, fill="both")
            
# Frame Wrapper that is "Tab" of Notebook Wrapper
class Tab(ttk.Frame):
    def __init__(self, parent, tab_text):
        super().__init__(parent)
        self.tab_text = tab_text

# Frame Wrapper that is Playlist Duration Calculator content
class PDC(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    # Row 0: Title Label
        
        self.title_label = ttk.Label(self, text="Playlist Duration Calculator")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=0, pady=0)

    # Row 1: Label and Entry Box
       
        self.url_label = ttk.Label(self, text="https://www.youtube.com/playlist?list=")
        self.url_label.grid(row=1, column=0, pady=0)

        self.default_playlist_id = "Enter Playlist ID"
        self.entry = ttk.Entry(self, foreground="grey")
        self.entry.insert(0, self.default_playlist_id)

        # Bind events to Entry field
        self.entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.entry.bind("<FocusOut>", self.on_entry_focus_out)

        self.entry.grid(row=1, column=1, padx=0, pady=0)

    # Row 2: Calculate Button and Combobox
        
        self.calculate_button = ttk.Button(self, text="Calculate", command=self.get_playlist_duration)
        self.calculate_button.grid(row=2, column=0, padx=0, pady=0, sticky='e')

        self.units = (
            "Seconds",
            "Minutes",
            "Hours",
            "Days",
            "Weeks",
            "Months",
            "Years",
            "Decades",
            "Century"
        )

        self.default_unit = tk.StringVar(value=self.units[2])
        self.combo = ttk.Combobox(self, values=self.units, textvariable=self.default_unit, state="readonly")
        self.combo.grid(row=2, column=1, padx=0, pady=0, sticky='w')

    # Row 3: Result Label
        
        self.result_label = ttk.Label(self, text="Result: ")
        self.result_label.grid(row=3, column=0, padx=0, pady=0)

        self.result = ttk.Label(self, text="")
        self.result.grid(row=3, column=1, padx=0, pady=0)

    # Pack the Frame itself
        
        self.pack()

    # When Entry field is focused
    def on_entry_focus_in(self, event):
        if self.entry.get() == self.default_playlist_id:
            self.entry.delete(0, "end")
            self.entry.configure(foreground="white")

    # When Entry field is no longer focused
    def on_entry_focus_out(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, self.default_playlist_id)
            self.entry.configure(foreground="grey")

    # Functions
    def get_playlist_duration(self):
        # Get inputs
        playlist_id = self.entry.get()
        unit = self.combo.get()
        # Apply functions
        videos_in_playlist = functions.get_videos_in_playlist(playlist_id)
        duration = functions.get_total_duration(videos_in_playlist)
        duration_in_unit = functions.get_duration_in_unit(duration, unit)
        self.result.config(text=duration_in_unit)

# Frame Wrapper that is Generate Video Transcript content
class GVT(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

App('Title', (600, 200), (600, 200), (600, 200))