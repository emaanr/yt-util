import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
import functions

# Variables
title = "YouTube Util"
units = (
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

# Functions
def get_playlist_duration():
    # Get inputs
    playlist_id = entry.get()
    unit = combo.get()
    # Apply functions
    videos_in_playlist = functions.get_videos_in_playlist(playlist_id)
    duration = functions.get_total_duration(videos_in_playlist)
    duration_in_unit = functions.get_duration_in_unit(duration, unit)
    result.config(text=duration_in_unit)

# When Entry field is focused
def on_entry_focus_in(event):
    if entry.get() == default_playlist_id:
        entry.delete(0, "end")
        entry.configure(foreground="white")


# When Entry field is no longer focused
def on_entry_focus_out(event):
    if entry.get() == "":
        entry.insert(0, default_playlist_id)
        entry.configure(foreground="gray")
    

# Create Window
window = tk.Tk()
style = Style("darkly")
window.title(title)
window.minsize(500, 125)
window.geometry("550x150")
window.maxsize(600, 200)

# Default Values
default_unit = tk.StringVar(value=units[2])
default_playlist_id = "Enter Playlist ID"

# Create Notebook
notebook = ttk.Notebook(master=window)

# Create Tabs
yt_pdc = ttk.Frame(master=notebook)
yt_gvt = ttk.Frame(master=notebook)

# Create Frames
content = ttk.Frame(master=yt_pdc)
enter_playlist_id = ttk.Frame(master=yt_pdc)
calculate_duration_in_units = ttk.Frame(master=yt_pdc)

# Create Label
label = ttk.Label(master=content, text=title, font=('Helvetica', 18), background="red")
label.grid(row=0, column=0, columnspan=3)

# Create Entry Label
entry_label = tk.Label(master=enter_playlist_id, text="https://www.youtube.com/playlist?list=")
entry_label.grid(row=1, column=0, pady=0)

# Create Entry
entry = ttk.Entry(master=enter_playlist_id, foreground="gray")
entry.insert(0, default_playlist_id)
entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)
entry.grid(row=1, column=1, pady=0)

# Create Button
button = tk.Button(master=calculate_duration_in_units, text="Calculate", command=get_playlist_duration)
button.grid(row=0, column=2, pady=0)

# Create Combobox
combo = ttk.Combobox(master=calculate_duration_in_units, values=units, textvariable=default_unit, state="readonly")
combo.grid(row=0, column=3, padx=0, pady=0)

# Create Label
result = ttk.Label(master=content, text="", font=('Helvetica', 18))
result.grid(row=3, column=0, columnspan=4, pady=0)

# Pack content into window
content.pack()
enter_playlist_id.pack()
calculate_duration_in_units.pack()

# Add Tabs to Notebook
notebook.add(child=yt_pdc, text="Playlist Duration Calculator")
notebook.add(child=yt_gvt, text="Generate Video Transcript")

# Pack Notebook into Window
notebook.pack()

# Updates the GUI and checks for Events
window.mainloop()