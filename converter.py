from tkinter import *
l = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def conv(num, base):
    r = ''
    base = int(base)
    if base >= len(l):
        raise ValueError
    while num != 0:
        b = num // base
        r += l[num % base]
        num = b
    return r[::-1]

def deconv(num, base):
    r = 0
    base = int(base)
    num = str(num)
    if base >= len(l):
        raise ValueError
    for i,x in enumerate(num[::-1]):
        r += base**i * l.find(x)
    return r

def converter(fromnum, frombase, tobase):
    if frombase != 10:
        fromnum = deconv(fromnum, frombase)
    return conv(fromnum, tobase)

def pressed():
    fromnum = entnum.get()
    frombase = entfrmbase.get()
    tobase = enttobase.get()
    lbl.configure(text=str(converter(fromnum, frombase, tobase)))

if __name__ == '__main__':
    window = Tk()
    window.title('Conv')
    window.geometry('223x90')
    window.wm_iconbitmap('favicon.ico')
    
    lblfrm = Label(window, text='From',padx=10)
    lblto = Label(window, text='To',padx=10)
    lblarrow = Label(window, text = '->',padx=10)
    lblresult = Label(window, text = 'Result',padx=10)
    lbl = Label(window,padx=10, text = '')
    lbl1 = Label(window,padx=10)
    
    entfrmbase = Entry(window,width=5)
    enttobase = Entry(window,width=5)
    entnum = Entry(window,width=5)
    
    btn = Button(window, text='Convert!', command=pressed, width=6)
    
    lblfrm.grid(row=0, column=0)
    lblto.grid(row=0, column=1)
    lblarrow.grid(row=0, column=2)
    lblresult.grid(row=0, column=4)
    lbl.grid(row=1, column=4)
    lbl1.grid(row=1, column=3)
    
    entfrmbase.grid(row=1, column=0)
    enttobase.grid(row=1, column=1)
    entnum.grid(row=2, column=0)
    
    btn.grid(row=3, column=2)
    