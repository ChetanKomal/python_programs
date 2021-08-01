import tkinter as tk
root= tk.Tk()
root.title("copy label")
root.maxsize(500,400)
root.minsize(500,400)

ll =tk.Label(text="cbaddk")
ll.pack(expand=1)

lll =tk.Entry(bd=0,font=(20))
lll.pack(expand=1)
lll.insert(0,"chetanverma cdcsdc")
lll.config(state="readonly")
root.mainloop()