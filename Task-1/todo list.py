from tkinter import *
root= Tk()
root.geometry("500x600")
root.title("To-DO List")
heading=Label(root, text="To-Do List", fg="black", font=("Helvetica", 20))
heading.pack()

number = 1
def add_task():
    global number 
    task = user.get()
    if task:  
        listbox.insert(END, f"{number}. {task}")
        user.delete(0, END)
        number+=1

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])


user = Entry(root, width=35)
user.pack(pady=10, padx=20, fill=X)

add = Button(root, text="Add Task", command=add_task)
add.pack(pady=5, padx=20, fill=X)

delete = Button(root, text="Delete Task", command=delete_task)
delete.pack(pady=5, padx=20, fill=X)

listbox = Listbox(root, width=45)
listbox.pack(pady=10, padx=20, fill=BOTH, expand=True)
root.mainloop()

