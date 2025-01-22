import tkinter as tk

root = tk.Tk()
root.title("kreslení kruhu")

canvas = tk.Canvas(root)
canvas.pack()

def kruh(r):
    canvas.create_oval(r,r,2*r,2*r)
    canvas.create_rectangle(r,r,2*r,2*r)
kruh(10)
kruh(20)
kruh(50)

root.mainloop()