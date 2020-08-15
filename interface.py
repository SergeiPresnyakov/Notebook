#!/usr/bin/python3.8
import tkinter as tk


def set_window(window):
    """Window params"""
    window.title('Interface')
    window.resizable(False, False)
    window.config(bg="#494949")

    height = 500
    width = 720

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = int((ws/2) - (width/2))
    y = int((hs/2) - (height/2))

    window.geometry(f'{width}x{height}+{x}+{y}')


# notes content
current_note_index = 0
with open('notes.txt', 'a+') as file:
    content = [line.strip() for line in file.read().split('-' * 50 + '\n') if line]


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
        global content
        global current_note_index

        notes = file.read().split('-' * 50 + '\n')
        notes = [note.strip() for note in notes if note]
        content = notes
        total_notes_label.config(text=len(notes))
        current_note_number_label.config(text='All')
        text.delete('1.0', tk.END)

        if len(notes):
            for line in notes:
                text.insert(tk.END, line + '\n--------------------------------------------------\n')
        else:
            text.insert(tk.END, '[!] You have no notes yet.')
        


def read_last(text):
    with open('notes.txt') as file:
        global content
        global current_note_index

        notes = file.read().split('-' * 50 + '\n')
        notes = [note.strip() for note in notes if note]
        total_notes_label.config(text=len(notes))
        text.delete('1.0', tk.END)

        if len(notes):
            text.insert(tk.END, notes[-1])
            content = notes
            current_note_index = len(notes) - 1
            current_note_number_label.config(text=current_note_index + 1)
        else:
            text.insert(tk.END, '[!] You have no notes yet.')


def switch_message(i):
    global current_note_index
    if current_note_index + i < 0 or current_note_index + i == len(content):
        i = 0
    try:    
        text.delete('1.0', tk.END)
        text.insert(tk.END, content[current_note_index + i])
        current_note_index += i
        current_note_number_label.config(text=current_note_index + 1)
        
    except IndexError:
        text.delete('1.0', tk.END)
        text.insert(tk.END, 'You have to read something first')


# button colors
def set_color(event):
    event.widget.config(bg='#5d5d5d', activebackground='#333333', activeforeground='#d4ff98')


def restore_color(event):
    event.widget.config(bg='#494949', fg='#d4ff98')


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
    bg='#333333',
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
)

button_readall = tk.Button(
    root,
    text='Read all',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: read_all(text),
    bg='#494949',
    fg='#d4ff98'
)

button_clear = tk.Button(
    root,
    text='Clear',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: clear_text(text),
    bg='#494949',
    fg='#d4ff98'
)

button_readlast = tk.Button(
    root,
    text='Read last',
    width=10,
    font='"ubuntu mono" 16',
    command=lambda: read_last(text),
    bg='#494949',
    fg='#d4ff98'
)

button_next = tk.Button(
    root,
    text='>>',
    width=10,
    font='"ubuntu mono" 16',
    bg='#494949',
    fg='#d4ff98',
    command=lambda: switch_message(1)
)

button_prev = tk.Button(
    root,
    text='<<',
    width=10,
    font='"ubuntu mono" 16',
    bg='#494949',
    fg='#d4ff98',
    command=lambda: switch_message(-1)
)

total_notes_label = tk.Label(
    root, 
    font='"ubuntu mono" 20',
    fg='#d4ff98',
    bg='#494949',
    text=len(content),
    width=3
)

current_note_number_label = tk.Label(
    root,
    font='"ubuntu mono" 20',
    fg='#d4ff98',
    bg='#494949',
    text=current_note_index + 1,
    width=3
)

# placing
text.place(relx=0.5, rely=0.02, anchor='n')
button_save.place(x=50, y=410)
button_readall.place(x=217, y=410 )
button_readlast.place(x=383, y=410)
button_clear.place(x=550, y=410)
button_prev.place(x=217, y=460)
button_next.place(x=383, y=460)
total_notes_label.place(x=100, y=460)
current_note_number_label.place(x=600, y=460)

# button colors change binding
button_save.bind('<Enter>', set_color)
button_save.bind('<Leave>', restore_color)
button_readlast.bind('<Enter>', set_color)
button_readlast.bind('<Leave>', restore_color)
button_readall.bind('<Enter>', set_color)
button_readall.bind('<Leave>', restore_color)
button_clear.bind('<Enter>', set_color)
button_clear.bind('<Leave>', restore_color)
button_next.bind('<Enter>', set_color)
button_next.bind('<Leave>', restore_color)
button_prev.bind('<Enter>', set_color)
button_prev.bind('<Leave>', restore_color)

# mainloop
root.mainloop()
