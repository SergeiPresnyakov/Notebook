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
       file.write('-' * 50)


def clear_text(text):
    text.delete('1.0', tk.END)


def read_all(text):
    with open('notes.txt') as file:
        for line in file:
            text.insert(tk.END, line)


# window init
root = tk.Tk()
set_window(root)

# interface elements
text = tk.Text(
    root,
    font='monaco 17',
    width=50,
    height=10,
    wrap=tk.WORD,
    padx=10,
    pady=10,
    bg='gray',
    fg='lime'
)

button_save = tk.Button(
    root,
    text='Save',
    width=10,
    font='monaco 16',
    command=lambda: save_note(text)
)

button_readall = tk.Button(
    root,
    text='Read all',
    width=10,
    font='monaco 16',
    command=lambda: read_all(text)
)

button_clear = tk.Button(
    root,
    text='Clear',
    width=10,
    font='monaco 16',
    command=lambda: clear_text(text)
)

# placing
text.place(x=0, y=0)
button_save.place(x=80, y=410)
button_readall.place(x=280, y=410)
button_clear.place(x=480, y=410)

# mainloop
root.mainloop()