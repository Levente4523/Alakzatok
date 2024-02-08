from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Alakzatok')
root.geometry('1000x800')
root.resizable(False, False)
root.configure(bg='#343536')

optkor = ['Kör1', 'Kör2']
optvonal = ['Vonal1', 'Vonal2']
opttegla = ['Téglalap1', 'Téglalap2']

def vonalrajz():
    global tpl, clicked, entry1, entry2, entry3, entry4, entry5, drop, vx1, vy1, vx2, vy2, vvas
    clicked = StringVar()
    tpl = Toplevel()
    tpl.title('Kérdőív')
    tpl.geometry('500x800')
    tpl.resizable(False, False)
    tpl.configure(bg='#343536')
    choose = Label(tpl, text='Válassz alakzatot!', font=('Arial', 18), bg='#343536', fg='white')
    choose.pack(pady=10)
    drop = OptionMenu(tpl, clicked, *optvonal)
    drop.pack(pady=10)
    drop.config(bg='#343536', fg='white')
    drop['menu'].config(bg='#343536', fg='white')
    vx1 = Label(tpl, text='X1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    vx1.pack()
    entry1 = Entry(tpl, font=('Arial', 18))
    entry1.pack(pady=10)
    vy1 = Label(tpl, text='Y1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    vy1.pack()
    entry2 = Entry(tpl, font=('Arial', 18))
    entry2.pack(pady=10)
    vx2 = Label(tpl, text='X1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    vx2.pack()
    entry3 = Entry(tpl, font=('Arial', 18))
    entry3.pack(pady=10)
    vy2 = Label(tpl, text='Y1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    vy2.pack()
    entry4 = Entry(tpl, font=('Arial', 18))
    entry4.pack(pady=10)
    vvas = Label(tpl, text='Vastagság:', font=('Arial', 18), bg='#343536', fg='white')
    vvas.pack()
    entry5 = Entry(tpl, font=('Arial', 18))
    entry5.pack(pady=10)
    submit = Button(tpl, text='Kész', font=('Arial', 18), bg='white', fg='black', command=vrajz)
    submit.pack(pady=10)
    lekerd = Button(tpl, text='Lekérdezés1', font=('Arial', 18), bg='white', fg='black', command=vlekerd1)
    lekerd.pack(pady=10)
    lekerd2 = Button(tpl, text='Lekérdezés2', font=('Arial', 18), bg='white', fg='black', command=vlekerd2)
    lekerd2.pack(pady=10)
    torles = Button(tpl, text='Törlés', font=('Arial', 18), bg='white', fg='black', command=vtorles)
    torles.pack(pady=10)
    tpl.mainloop()

def korrajz():
    global tpl1, clicked1, entry6, entry7, entry8, entry9, drop1, kx, ky, kvas, sug
    clicked1 = StringVar()
    tpl1 = Toplevel()
    tpl1.title('Kérdőív')
    tpl1.geometry('500x800')
    tpl1.resizable(False, False)
    tpl1.configure(bg='#343536')
    choose = Label(tpl1, text='Válassz alakzatot!', font=('Arial', 18), bg='#343536', fg='white')
    choose.pack(pady=(10,0))
    drop1 = OptionMenu(tpl1, clicked1, *optkor)
    drop1.pack(pady=10)
    drop1.config(bg='#343536', fg='white')
    drop1['menu'].config(bg='#343536', fg='white')
    kx = Label(tpl1, text='X koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    kx.pack()
    entry6 = Entry(tpl1, font=('Arial', 18))
    entry6.pack(pady=10)
    ky = Label(tpl1, text='Y koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    ky.pack()
    entry7 = Entry(tpl1, font=('Arial', 18))
    entry7.pack(pady=10)
    sug = Label(tpl1, text='Sugár:', font=('Arial', 18), bg='#343536', fg='white')
    sug.pack()
    entry8 = Entry(tpl1, font=('Arial', 18))
    entry8.pack(pady=10)
    kvas = Label(tpl1, text='Vastagság:', font=('Arial', 18), bg='#343536', fg='white')
    kvas.pack()
    entry9 = Entry(tpl1, font=('Arial', 18))
    entry9.pack(pady=10)
    submit = Button(tpl1, text='Kész', font=('Arial', 18), bg='white', fg='black', command=krajz)
    submit.pack(pady=10)
    lekerd = Button(tpl1, text='Lekérdezés1', font=('Arial', 18), bg='white', fg='black', command=klekerd1)
    lekerd.pack(pady=10)
    lekerd2 = Button(tpl1, text='Lekérdezés2', font=('Arial', 18), bg='white', fg='black', command=klekerd2)
    lekerd2.pack(pady=10)
    torles = Button(tpl1, text='Törlés', font=('Arial', 18), bg='white', fg='black', command=ktorles)
    torles.pack(pady=10)
    tpl1.mainloop()

def teglarajz():
    global tpl2, clicked2, entry10, entry11, entry12, entry13, entry14, drop2, tx1, ty1, tx2, ty2
    clicked2 = StringVar()
    tpl2 = Toplevel()
    tpl2.title('Kérdőív')
    tpl2.geometry('500x800')
    tpl2.resizable(False, False)
    tpl2.configure(bg='#343536')
    choose = Label(tpl2, text='Válassz alakzatot!', font=('Arial', 18), bg='#343536', fg='white')
    choose.pack(pady=10)
    drop2 = OptionMenu(tpl2, clicked2, *opttegla)
    drop2.pack(pady=10)
    drop2.config(bg='#343536', fg='white')
    drop2['menu'].config(bg='#343536', fg='white')
    tx1 = Label(tpl2, text='X1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    tx1.pack()
    entry10 = Entry(tpl2, font=('Arial', 18))
    entry10.pack(pady=10)
    ty1 = Label(tpl2, text='Y1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    ty1.pack()
    entry11 = Entry(tpl2, font=('Arial', 18))
    entry11.pack(pady=10)
    tx2 = Label(tpl2, text='X1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    tx2.pack()
    entry12 = Entry(tpl2, font=('Arial', 18))
    entry12.pack(pady=10)
    ty2 = Label(tpl2, text='Y1 koordináta:', font=('Arial', 18), bg='#343536', fg='white')
    ty2.pack()
    entry13 = Entry(tpl2, font=('Arial', 18))
    entry13.pack(pady=10)
    tvas = Label(tpl2, text='Vastagság:', font=('Arial', 18), bg='#343536', fg='white')
    tvas.pack()
    entry14 = Entry(tpl2, font=('Arial', 18))
    entry14.pack(pady=10)
    submit = Button(tpl2, text='Kész', font=('Arial', 18), bg='white', fg='black', command=trajz)
    submit.pack(pady=10)
    lekerd = Button(tpl2, text='Lekérdezés1', font=('Arial', 18), bg='white', fg='black', command=tlekerd1)
    lekerd.pack(pady=10)
    lekerd2 = Button(tpl2, text='Lekérdezés2', font=('Arial', 18), bg='white', fg='black', command=tlekerd2)
    lekerd2.pack(pady=10)
    torles = Button(tpl2, text='Törlés', font=('Arial', 18), bg='white', fg='black', command=ttorles)
    torles.pack(pady=10)
    tpl2.mainloop()

def del_can():
    canvas.delete('all')

def vrajz():
    global vonal1_x1, vonal1_y1, vonal1_x2, vonal1_y2, vonal1_vas, vonal2_x1, vonal2_y1, vonal2_x2, vonal2_y2, vonal2_vas, mano1, mano2
    if clicked.get() == 'Vonal1':
        try:
            vonal1_x1 = int(entry1.get())
            vonal1_y1 = int(entry2.get())
            vonal1_x2 = int(entry3.get())
            vonal1_y2 = int(entry4.get())
            vonal1_vas = int(entry5.get())
            mano1 = canvas.create_line(vonal1_x1, vonal1_y1, vonal1_x2, vonal1_y2, width=vonal1_vas)
        except ValueError:
            messagebox.showerror('Naa', 'Számot adj meg mindenhova!')
    else:
        try:
            vonal2_x1 = int(entry1.get())
            vonal2_y1 = int(entry2.get())
            vonal2_x2 = int(entry3.get())
            vonal2_y2 = int(entry4.get())
            vonal2_vas = int(entry5.get())
            mano2 = canvas.create_line(vonal2_x1, vonal2_y1, vonal2_x2, vonal2_y2, width=vonal2_vas)
        except ValueError:
            messagebox.showerror('Naa', 'Számot adj meg mindenhova!')

def krajz():
    global kor1_x, kor1_y, r1, kor_vas1, kor2_x, kor2_y, r2, kor_vas2, mano3, mano4
    if clicked1.get() == 'Kör1':
        try:
            kor1_x = int(entry6.get())
            kor1_y = int(entry7.get())
            r1 = int(entry8.get())
            kor_vas1 = int(entry9.get())
            mano3 = Canvas.create_oval(canvas, kor1_x-r1, kor1_y-r1, kor1_x+r1, kor1_y+r1, width=kor_vas1)
        except ValueError:
            messagebox.showerror('Naa', 'Számot adj meg mindenhova!')
    else:
        try:
            kor2_x = int(entry6.get())
            kor2_y = int(entry7.get())
            r2 = int(entry8.get())
            kor_vas2 = int(entry9.get())
            mano4 = Canvas.create_oval(canvas, kor2_x-r2, kor2_y-r2, kor2_x+r2, kor2_y+r2, width=kor_vas2)
        except ValueError:
            messagebox.showerror('Naa', 'Számot adj meg mindenhova!')

def trajz():
    global tegla1_x1, tegla1_y1, tegla1_x2, tegla1_y2, tegla1_vas, tegla2_x1, tegla2_y1, tegla2_x2, tegla2_y2, tegla2_vas, mano5, mano6
    if clicked2.get() == 'Téglalap1':
        try:
            tegla1_x1 = int(entry10.get())
            tegla1_y1 = int(entry11.get())
            tegla1_x2 = int(entry12.get())
            tegla1_y2 = int(entry13.get())
            tegla1_vas = int(entry14.get())
            mano5 = Canvas.create_rectangle(canvas, tegla1_x1, tegla1_y1, tegla1_x2, tegla1_y2, width=tegla1_vas)
        except ValueError:
            messagebox.showerror('Naa', 'Számot adj meg mindenhova!')
    else:
        try:
            tegla2_x1 = int(entry10.get())
            tegla2_y1 = int(entry11.get())
            tegla2_x2 = int(entry12.get())
            tegla2_y2 = int(entry13.get())
            tegla2_vas = int(entry14.get())
            mano6 = Canvas.create_rectangle(canvas, tegla2_x1, tegla2_y1, tegla2_x2, tegla2_y2, width=tegla2_vas)
        except ValueError:
            messagebox.showerror('Naa', 'Számot adj meg mindenhova!')

def vlekerd1():
    try:
        entry1.delete(0, END)
        entry1.insert(0, vonal1_x1)
        entry2.delete(0, END)
        entry2.insert(0, vonal1_y1)
        entry3.delete(0, END)
        entry3.insert(0, vonal1_x2)
        entry4.delete(0, END)
        entry4.insert(0, vonal1_y2)
        entry5.delete(0, END)
        entry5.insert(0, vonal1_vas)
    except NameError:
        messagebox.showerror('Naa', 'Nincs adat eltárolva!')

def vlekerd2():
    try:
        entry1.delete(0, END)
        entry1.insert(0, vonal2_x1)
        entry2.delete(0, END)
        entry2.insert(0, vonal2_y1)
        entry3.delete(0, END)
        entry3.insert(0, vonal2_x2)
        entry4.delete(0, END)
        entry4.insert(0, vonal2_y2)
        entry5.delete(0, END)
        entry5.insert(0, vonal2_vas)
    except NameError:
        messagebox.showerror('Naa', 'Nincs adat eltárolva!')

def vtorles():
    global mano1, mano2
    try:
        if clicked.get() == 'Vonal1':
            canvas.delete(mano1)
        else:
            canvas.delete(mano2)
    except NameError:
        messagebox.showerror('Naa', 'Nem választottál ki semmit!')

def klekerd1():
    try:
        entry6.delete(0, END)
        entry6.insert(0, kor1_x)
        entry7.delete(0, END)
        entry7.insert(0, kor1_y)
        entry8.delete(0, END)
        entry8.insert(0, r1)
        entry9.delete(0, END)
        entry9.insert(0, kor_vas1)
    except NameError:
        messagebox.showerror('Naa', 'Nincs adat eltárolva!')

def klekerd2():
    try:
        entry6.delete(0, END)
        entry6.insert(0, kor2_x)
        entry7.delete(0, END)
        entry7.insert(0, kor2_y)
        entry8.delete(0, END)
        entry8.insert(0, r2)
        entry9.delete(0, END)
        entry9.insert(0, kor_vas2)
    except NameError:
        messagebox.showerror('Naa', 'Nincs adat eltárolva!')

def ktorles():
    global mano3, mano4
    try:
        if clicked1.get() == 'Kör1':
            canvas.delete(mano3)
        else:
            canvas.delete(mano4)
    except NameError:
        messagebox.showerror('Naa', 'Nem választottál ki semmit!')

def tlekerd1():
    try:
        entry10.delete(0, END)
        entry10.insert(0, tegla1_x1)
        entry11.delete(0, END)
        entry11.insert(0, tegla1_y1)
        entry12.delete(0, END)
        entry12.insert(0, tegla1_x2)
        entry13.delete(0, END)
        entry13.insert(0, tegla1_y2)
        entry14.delete(0, END)
        entry14.insert(0, tegla1_vas)
    except NameError:
        messagebox.showerror('Naa', 'Nincs adat eltárolva!')

def tlekerd2():
    try:
        entry10.delete(0, END)
        entry10.insert(0, tegla2_x1)
        entry11.delete(0, END)
        entry11.insert(0, tegla2_y1)
        entry12.delete(0, END)
        entry12.insert(0, tegla2_x2)
        entry13.delete(0, END)
        entry13.insert(0, tegla2_y2)
        entry14.delete(0, END)
        entry14.insert(0, tegla2_vas)
    except NameError:
        messagebox.showerror('Naa', 'Nincs adat eltárolva!')

def ttorles():
    global mano5, mano6
    try:
        if clicked2.get() == 'Téglalap1':
            canvas.delete(mano5)
        else:
            canvas.delete(mano6)
    except NameError:
        messagebox.showerror('Naa', 'Nem választottál ki semmit!')        

canvas = Canvas(root, width=900, height=600, bg='white')
canvas.pack(pady=20)

frame = LabelFrame(root, bg='#343536', fg='#343536')
frame.pack(pady=10)
vonal = Button(frame, text='Vonal', font=('Arial', 18), bg='white', command=vonalrajz)
vonal.grid(row=0, column=0, padx=(0,20))
kor = Button(frame, text='Kör', font=('Arial', 18), command=korrajz, bg='white')
kor.grid(row=0, column=1)
tegla = Button(frame, text='Téglalap', font=('Arial', 18), bg='white', command=teglarajz)
tegla.grid(row=0, column=2, padx=(20,0))

delete = Button(root, text='Összes törlése', font=('Arial', 18), command=del_can, bg='white')
delete.pack(pady=10)

root.mainloop()