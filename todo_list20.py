from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    try:
        lb.delete(ANCHOR)
    except:
        messagebox.showwarning("Warning", "No task selected to delete.")

def deleteAllTasks():
    lb.delete(0, END) 

def exitApp():
    ws.destroy()

ws = Tk()
ws.geometry('500x500+250+250')
ws.title('Task Manager')
ws.config(bg='#00FFFF')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=4)

tasklist_label = Label(frame, text="Task List", font=('times', 18), bg='#00FFFF')
tasklist_label.pack()

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(ws, font=('times', 24))
my_entry.pack(pady=20)

instruction_label = Label(ws, text="Enter a task and press 'Add Task'", font=('times', 14), bg='#00FFFF')
instruction_label.pack()

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times', 14),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times', 14),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delAllTasks_btn = Button(
    button_frame,
    text='Delete All Tasks',
    font=('times', 14),
    bg='#ffb347',
    padx=20,
    pady=10,
    command=deleteAllTasks
)
delAllTasks_btn.pack(fill=BOTH, expand=True, side=LEFT)

exit_btn = Button(
    button_frame,
    text='Exit',
    font=('times', 14),
    bg='#ff6f61',
    padx=20,
    pady=10,
    command=exitApp
)
exit_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
