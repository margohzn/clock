from tkinter import *
from time import strftime

def get_time():
    str_time = strftime('%H:%M:%S %p')
    clock.config(text = str_time)
    clock.after(1000, get_time)
    #after fonction is like the schedualing fonction in pygame





window = Tk()
window.geometry("400x100")
window.configure(background = "orange")
window.resizable(False, False)

clock = Label(window, text = "", fg = "black", bg = "orange", font = ("times", 70))
clock.pack(anchor = "center")
get_time()

window.mainloop()