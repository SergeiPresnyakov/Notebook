import tkinter as tk


def set_window(window):
    """Window params"""
    window.title('Interface')
    window.resizable(False, False)

    height = 480
    width = 720

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = int((ws/2) - (width/2))
    y = int((hs/2) - (height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')


# button logic
def save_note(text):
    with open('notes.txt', 'a+') as file:
       input = text.get('1.0', tk.END)
       file.write(input)
       file.write('-' * 50 + '\n')


def clear_text(text):
    text.delete('1.0', tk.END)


def read_all(text):
    with open('notes.txt') as file:
        for line in file:
            text.insert(tk.END, line)


def read_last(text):
    with open('notes.txt') as file:
        notes = file.read().split('-' * 50 + '\n')
        notes = [note.strip() for note in notes if note]
        text.delete('1.0', tk.END)
        text.insert(tk.END, notes[-1])


# button colors
def set_color(event):
    event.widget.config(bg='#5a5a5a')


def restore_color(event):
    event.widget.config(bg='#494949')


# window init
root = tk.Tk()
set_window(root)

# interface elements
text = tk.Text(
    root,
    font='"ubuntu mono" 20',
    width=50,
    height=13,
    wrap=tk.WORD,
    padx=10,
    pady=10,
    bg='#494949',
    fg='#d4ff98'
)

button_save = tk.Button(
    root,
    text='Save',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: save_note(text),
    bg='#494949',
    fg='#d4ff98',
    activebackground='gray'
)

button_readall = tk.Button(
    root,
    text='Read all',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: read_all(text),
    bg='#494949',
    fg='#d4ff98',
    activebackground='gray'
)

button_clear = tk.Button(
    root,
    text='Clear',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: clear_text(text),
    bg='#494949',
    fg='#d4ff98',
    activebackground='gray'
)

button_readlast = tk.Button(
    root,
    text='Read last',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: read_last(text),
    bg='#494949',
    fg='#d4ff98',
    activebackground='gray'
)

# placing
text.place(relx=0.5, rely=0.05, anchor='n')
button_save.place(x=50, y=410)
button_readall.place(x=217, y=410 )
button_readlast.place(x=383, y=410)
button_clear.place(x=550, y=410)

# button colors change binding
button_save.bind('<Enter>', set_color)
button_save.bind('<Leave>', restore_color)
button_readlast.bind('<Enter>', set_color)
button_readlast.bind('<Leave>', restore_color)
button_readall.bind('<Enter>', set_color)
button_readall.bind('<Leave>', restore_color)
button_clear.bind('<Enter>', set_color)
button_clear.bind('<Leave>', restore_color)

# mainloop
root.mainloop()