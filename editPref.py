import sys
import tkinter
import tkinter.messagebox

prefFile = open("config.txt", 'r')
pref = prefFile.readlines()
vol = int(pref[1][:-1])
width = int(pref[4][:-1])
height = int(pref[5][:-1])
prefFile.close()

def update(event):
    global vol_edit
    vol_edit = scale_vol.get()

def validate(w, h):
    res = w.isnumeric() and h.isnumeric()
    return res

def saveandquit():
    if validate(txtbox_width.get(), txtbox_height.get()) == True:
        writeBuf = open("config.txt", 'w')
        pref[1] = str(vol_edit) + '\n'
        pref[4] = txtbox_width.get() + '\n'
        pref[5] = txtbox_height.get() + '\n'
        writeBuf.writelines(pref)
        writeBuf.close()
        sys.exit()
    else:
        tkinter.messagebox.showerror(title="Error", message="Width and Height Value is Invalid")

def discardandquit():
    sys.exit()

root = tkinter.Tk()
root.geometry("400x300")
root.title("Benzodiazepine Preferences")
root.resizable(False, False)

frame_sound = tkinter.LabelFrame(root, text="Sound Settings", relief="solid", bd=2)
frame_sound.pack(side="top", fill='both', padx = 5, pady=5, expand=False)
# frame_sound.place(x=5, y=5, width= 290, height= 100)
frame_display = tkinter.LabelFrame(root, text="Display Settings", relief="solid", bd=2)
frame_display.pack(fill="both", padx = 5, pady=5, expand=True)

label_vol = tkinter.Label(frame_sound, text="Volume")
scale_vol = tkinter.Scale(frame_sound, orient="horizontal", showvalue=True, length=250, command=update)
scale_vol.set(vol)
scale_vol.pack(side="right", padx=10, pady=10, expand=True)
label_vol.pack(side="left", padx=10, pady=10)

label_width = tkinter.Label(frame_display, text="Width\n\nHeight")
# label_height = tkinter.Label(frame_display, text="Height")
label_width.pack(side='left', padx=10, pady=10)
# label_height.pack(side="bottom", padx=10, pady=10)

txtbox_width = tkinter.Entry(frame_display, width=15)
txtbox_height = tkinter.Entry(frame_display, width=15)
txtbox_width.pack(side='top', padx=15, pady=13)
txtbox_height.pack(side='top', padx=15, pady= 13)
txtbox_width.insert(0, str(width))
txtbox_height.insert(0, str(height))

okbutton = tkinter.Button(root, overrelief='solid', text="Save", command=saveandquit)
quitbutton = tkinter.Button(root, overrelief='solid', text="Discard", command=discardandquit)

okbutton.pack(side='right', padx=5, pady=5)
quitbutton.pack(side='right', padx=5, pady=5)

root.mainloop()
