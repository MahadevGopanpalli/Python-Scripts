import tkinter
from tkinter import filedialog

delete=''

import os
import shutil
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def main():  
    path=os.path.abspath(delete)
    
    data={}

    for F,SF,f in os.walk(path):
        for file in f:
            path=os.path.join(F,file)
            chk=hashfile(path)

            if chk in data:
                data[chk].append(path)
            else:
                data[chk]=[path]
    


    newdata=list(filter(lambda  x:len(x)>1,data.values()))
    count=0
    for outer in newdata:
        icnt=0
        for inner in outer:
            icnt=icnt+1
            if icnt>=2:
                count=count+1
                inner=os.path.abspath(inner)
                os.remove(inner)
    print(count)
    from tkinter import messagebox
    messagebox.showinfo("","Successfully Done...\nDeleted {} Duplicate files...".format(count))  
    Cancel()



def Pastehere():
    filez = filedialog.askdirectory(parent=root,title='Choose a Folder')
    if(len(filez)==0):
        return
    delete=filez
    res1.configure(text = "Delete Duplicate files from:\n{}".format(str(filez)))
    if delete!='':
        browsebutton1.configure(state=DISABLED)
        c.config(state=NORMAL)
    else:
        c.config(state=DISABLED)

def Cancel():
    
    delete=''
    res.configure(text = " ")
    res1.configure(text = " ")
    browsebutton1.configure(state=NORMAL)

from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Copy & Paste')

root.geometry('700x800')
img=Image.open("m.png")
img=img.resize((100, 100))
img = ImageTk.PhotoImage(img) 

h1=Label(root,image=img)
h1.pack(side=TOP,pady=20)

h2 = Label(root,text='DUPLICATE FILE REMOVER' ,font=('verdana',30),justify=LEFT)
h2.pack(fill=X,padx=3)




res = Label(root,font=('verdana',15),justify=LEFT)
res.pack(fill=X,padx=10,pady=20)



h3 = Label(root,text='Select Folder:' ,font=('verdana',25),justify=LEFT)
h3.pack(fill=X,padx=10,pady=10)

#dest=Entry(root,font=('verdana',18))
#dest.pack(side=TOP,fill=X,padx=20,pady=10)


browsebutton1 = Button(root, text="Browse", command=Pastehere,font=('verdana',18))
browsebutton1.pack()

res1 = Label(root,font=('verdana',15),justify=LEFT)
res1.pack(fill=X,padx=10,pady=20)


top = Frame(root)

top.pack(side=TOP)
b = Button(root, text="Cancel",font=('verdana',18), command=Cancel)


c = Button(root, text="Delete", font=('verdana',18),command=main,state=DISABLED)


b.pack(in_=top, side=LEFT,padx=20)
c.pack(in_=top, side=LEFT,padx=20)

root.mainloop()

