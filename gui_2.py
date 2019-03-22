import tkinter as tk
#import request

#general config:
#functions:

#def clc():

    #output.delete(first=0,last=1000)

def insdata():
    out.delete(0.0,'end')
    inp=Expr.get()
    tokexpr=inp+"\n"
    out.insert(0.0,tokexpr)


root=tk.Tk()
root.geometry("400x200")
Exprlabel=tk.Label(root,text='Expressão: ')
Expr=tk.Entry(root)
Tokenlabel=tk.Label(root,text='Tokens:')
out=tk.Text(root,width=25,height=10,wrap='word')
ButtonAval=tk.Button(root,text='Avaliar',command=insdata)
#Buttonclean=tk.Button(root,text='Limpar',command=clc())
Resultlabel=tk.Label(root,text='Resultado:')
result=tk.Text(root,width=10,height=1)
#config widgets
Exprlabel.grid(row=0)
Tokenlabel.grid(row=1)
Expr.grid(row=0,column=1)
out.grid(row=3,columnspan=2,sticky='w')
ButtonAval.grid(row=4)
#Buttonclean.grid(row=5)
Resultlabel.grid(row=4,column=1)
result.grid(row=4,column=2)
root.mainloop()
