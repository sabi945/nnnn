import tkinter as tk



root = tk.Tk()
labe = tk.Label(root, text="halo semuanya")
labe.pack()


farme_1 = tk.Frame(root,bg="#4C9900", width=200, height=200)
label_2 = tk.Label(farme_1, text="selamat datang di tempat kami",bg="#4C9900")
label_2.configure(bg=None)
label_2.pack()
farme_1.place(x=50,y=50)
farme_1.pack_propagate(False)
root.mainloop()