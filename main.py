
from tkinter import IntVar, Tk, Toplevel
from tkinter import ttk
from tkinter import messagebox
#from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("MyApp")
#root.iconbitmap("py_icon.png")
root.geometry("800x300")

def new_button():
    top = Toplevel()
    top.title("Example")
    top.geometry("200x200")
    top.resizable(False, False)
    
    btn = ttk.Button(top, text="New Button", padding=10)
    btn.pack()
    
    top.mainloop()
    return

def new_text():
    top = Toplevel()
    top.title("Example")
    top.geometry("300x300")
    top.resizable(True, True)
    
    e = ttk.Entry(top, width=50, text="Enter text here", font=("Arial", 20))
    e.pack()

    top.mainloop()

    return

def radio_buttons():
    def Clicked(value):
        print(value.get())
    
    top = Toplevel()
    top.title("Example")
    top.geometry("200x200")
    top.resizable(False, False)
    
    ttk.Label(top, text="Hello this is a new window").pack()
    
    var = IntVar()
    var.set(1)

    ttk.Radiobutton(top, text="Option 1", variable=var, value=1, command=lambda: Clicked(var)).pack()
    ttk.Radiobutton(top, text="Option 2", variable=var, value=2, command=lambda: Clicked(var)).pack()
    ttk.Radiobutton(top, text="Option 3", variable=var, value=3, command=lambda: Clicked(var)).pack()

    myLabel = ttk.Label(top, text = Clicked(var))
    myLabel.pack()

    top.mainloop()
    return

class MessageBox:
    def show_info():
        messagebox.showinfo(title="Example", message="Hello World")
        return

    def show_warning():
        messagebox.showwarning(title="Example", message="Do you wish to continue?")
        return

    def show_error():
        messagebox.showerror(title="Example", message="This is an error")
        return
  
    def ask_question():
        resp = messagebox.askquestion(title="Example", message="Do you like Python?")
        print(resp)
        if resp == True:
            print("User clicked yes")
        else:
            print("User clicked no")
        return
    
    def ask_ok_cancel():
        resp = messagebox.askokcancel(title="Example", message="Do you like Python?")
        print(resp)
        if resp == True:
            print("User clicked ok")
        else:
            print("User clicked cancel")
        return
    
    def ask_retry_cancel():
        resp = messagebox.askretrycancel(title="Example", message="Do you like Python?")
        print(resp)
        if resp == True:
            print("User clicked retry")
        else:
            print("User clicked cancel")
        return

    def ask_yes_no():
        resp = messagebox.askyesno(title="Example", message="Do you like Python?")
        print(resp)
        if resp == True:
            print("User clicked yes")
        else:
            print("User clicked no")
        return
    
    def ask_yes_no_cancel():
        resp = messagebox.askyesnocancel(title="Example", message="Do you like Python?")
        print(resp)
        if resp == True:
            print("User clicked yes")
        elif resp == False:
            print("User clicked no")
        else:
            print("User clicked cancel")
        return

def new_window():
    top = Toplevel()
    top.title("Example")
    top.geometry("200x200")
    top.resizable(False, False)
    
    ttk.Label(top, text="Hello this is a new window").pack()

    top.mainloop()
    return

def show_files():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    return

def slider():
    vertical = ttk.Scale(root, from_=0, to=100)
    vertical.pack()
    return

def checkboxs():
    top = Toplevel()
    top.title("Example")
    top.geometry("200x200")
    top.resizable(False, False)
    
    ttk.Label(top, text="Hello this is a new window").pack()
    
    var = IntVar()
    cb = ttk.Checkbutton(top, text="Check me", variable=var)
    cb.pack()

    top.mainloop()
    return



frm = ttk.Frame(root, padding=10)
frm.grid()

#ttk.Label(frm, text="Misc").grid(column=0, row=1)
ttk.Button(text="Button", command=new_button).grid(column=0, row=1)
ttk.Button(text="Text", command=new_text).grid(column=1, row=1)

ttk.Button(text="Show Radio Buttons", command=radio_buttons).grid(column=1, row=2)

#ttk.Label(frm, text="Message Boxies").grid(column=0, row=3)
ttk.Button(text="Show Info", command=MessageBox.show_info).grid(column=0, row=3)
ttk.Button(text="Show Warn", command=MessageBox.show_warning).grid(column=1, row=3)
ttk.Button(text="Show error", command=MessageBox.show_error).grid(column=2, row=3)
ttk.Button(text="Ask Question", command=MessageBox.ask_question).grid(column=3, row=3)
ttk.Button(text="Ask OK Cancel", command=MessageBox.ask_ok_cancel).grid(column=4, row=3)
ttk.Button(text="Ask Retry Cancel", command=MessageBox.ask_retry_cancel).grid(column=5, row=3)
ttk.Button(text="Ask Yes No", command=MessageBox.ask_yes_no).grid(column=6, row=3)
ttk.Button(text="Ask Yes No Cancel", command=MessageBox.ask_yes_no_cancel).grid(column=7, row=3)

#ttk.Label(frm, text="Stuff").grid(column=0, row=4)
ttk.Button(text="New Window", command=new_window).grid(column=0, row=4)
ttk.Button(text="Show Files", command=show_files).grid(column=1, row=4)
ttk.Button(text="Show Slider", command=None).grid(column=2, row=4)
ttk.Button(text="Show Checkboxs", command=checkboxs).grid(column=3, row=4)

root.mainloop()