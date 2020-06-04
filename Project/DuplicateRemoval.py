import sys
import os
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

def main(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exits=os.path.isdir(path)

    if exits:
        print(path)
    
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
    messagebox.showinfo("","Successfully Done...\nCopied {} text files...".format(count))  
    Cancel()


