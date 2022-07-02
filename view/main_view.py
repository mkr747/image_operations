import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(0, minsize=100, weight=1)

s = ttk.Style()
s.configure("TFrame", relief=tk.RAISED)

frame_components = ttk.Frame(
    master=window, width=300, height=900)

button_frame1 = ttk.Button(
    frame_components, text="Erode").grid(column=0, row=0)
button_frame2 = ttk.Button(
    frame_components, text="Dilate").grid(column=0, row=1)
button_frame3 = ttk.Button(
    frame_components, text="Opening").grid(column=0, row=2)
button_frame4 = ttk.Button(
    frame_components, text="Closing").grid(column=0, row=3)
button_frame5 = ttk.Button(
    frame_components, text="Gradient").grid(column=0, row=4)

frame_components.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
#frame_components.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame_right = ttk.Frame(master=window, width=1200, height=900)
frame_right.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")

frame_algorithm = ttk.Frame(master=frame_right, width=400, height=600)

listbox = tk.Listbox(frame_algorithm)
listbox.place(x=10, y=0)
checkbutton = tk.Checkbutton(listbox, text='test').pack()
listbox.insert(tk.END, checkbutton)
listbox.insert(tk.END, 'sdsd')

frame_algorithm.grid(row=0, column=3, padx=1, pady=1, sticky="nsew")
#frame_algorithm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


frame_image = ttk.Frame(master=frame_right, width=800, height=600)

frame_image.grid(row=0, column=7, padx=1, pady=1, sticky="nsew")
#frame_image.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame_params = ttk.Frame(master=frame_right, width=400, height=300)

frame_params.grid(row=6, column=3, padx=1, pady=1, sticky="nsew")
#frame_params.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


frame_ai = ttk.Frame(master=frame_right, width=800, height=300)

frame_ai.grid(row=6, column=7, padx=1, pady=1, sticky="nsew")

#frame_ai.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# entry = tk.Entry(width=40, bg="white", fg="black")
# entry.pack()
# entry.insert(0, "sup")
window.mainloop()
