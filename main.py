import tkinter
from tkinter import BOTH, END, StringVar, messagebox
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('Hello GUI World')
root.iconbitmap('wave.ico')
root.geometry('400x400')
root.resizable(False, False)

# define fonts and colors
root_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'
root.config(bg=root_color)

# define functions
def submit_name():
    if name.get() == '':
        tkinter.messagebox.showwarning("Warning", "input can not be empty before submiting")
        return

    if case_style.get() == 'normal':
        name_label = tkinter.Label(output_frame, text="Hello " + name.get() + "! Keep learning tkinter")
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text=("Hello " + name.get() + "! Keep learning tkinter").upper())
    name_label.config(bg=output_color)
    name_label.pack()
    name.delete(0, END)


# define layout
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# define input and button
name = tkinter.Entry(input_frame, text='Enter your name', width=20)
submit_button = tkinter.Button(input_frame, text='Submit', command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# define radio buttons
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text='Normal Case', variable=case_style, value='normal')
normal_button.config(bg=input_color)
upper_button = tkinter.Radiobutton(input_frame, text='Upper Case', variable=case_style, value='upper')
upper_button.config(bg=input_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# add an image
smile_img = ImageTk.PhotoImage(Image.open('smile.png'))
smile_label = tkinter.Label(output_frame, image=smile_img)
smile_label.config(bg=output_color)
smile_label.pack()

root.mainloop()