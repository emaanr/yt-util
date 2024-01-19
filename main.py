import tkinter as tk

root = tk.Tk()

root.geometry("1000x500")
root.title("YouTube Util")

label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack()

button = tk.Button(root, text="Button to Click", font=('Arial', 16))
button.pack(padx=10, pady=10)

root.mainloop()