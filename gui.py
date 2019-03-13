import tkinter as tk
import subprocess as sbp
class gui:

    def __init__(self,master):

        #expression
        self.f2=tk.Frame(master)
        self.f2.pack()
        self.f2.place(x=10,y=10)

        #token box
        self.out=tk.Frame(master)
        self.out.grid_propagate(False)
        self.out.pack()
        self.out.place(height=100,width=400,x=10,y=60)

        #button
        self.but=tk.Frame(master)
        self.but.pack()
        self.but.place(x=10,y=180)
        #result box
        self.result=tk.Frame(master)
        self.result.grid_propagate(False)
        self.result.pack()
        self.result.place(height=45,width=120,x=130,y=170)

        #type box
        self.wid()

    def wid(self):

        self.text=tk.Label(self.f2,text='expressão:').pack()
        self.expression=tk.Entry(self.f2,text='exp').pack()

        self.texttok=tk.Label(self.out,text='token:').pack()
        self.tok=tk.Text(self.out)
        #self.tok.insert(tk.INSERT,"hello\n")
        self.tok.pack()
        self.tok.config(state="disabled")

        self.b1=tk.Button(self.but,text='Avaliar',bg='white',font=('arial','8'),width=15,command=lambda: self.con())
        self.b1.pack()

        self.txtvlr=tk.Label(self.result,text='valor:').pack()
        self.vlr=tk.Text(self.result)
        self.vlr.insert(tk.INSERT,"bye\n")
        self.vlr.pack()
        self.vlr.config(state="disabled")

    def con(self):

        self.tok.insert(tk.INSERT,'hello')


root=tk.Tk()
app=gui(root)
root.mainloop()
