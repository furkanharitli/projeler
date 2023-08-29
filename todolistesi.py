
from tkinter import *

root = Tk()
root.title("To-Do List")

tasks = []


# Kullanıcı girdisi için etiket ve giriş kutusu
task_label = Label(root, text="Yapılacak öğe:")
task_label.pack()

task_entry = Entry(root)
task_entry.pack()

# "Ekle" düğmesi için işlev
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_entry.delete(0, END)
        update_listbox()

add_button = Button(root, text="Ekle", command=add_task)
add_button.pack()




# Liste kutusu için fonksiyonlar
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert(END, task)

def clear_listbox():
    lb_tasks.delete(0, END)

# Liste kutusu
lb_tasks = Listbox(root)
lb_tasks.pack()


# "Sil" düğmesi için işlev
def delete_task():
    task = lb_tasks.get(ANCHOR)
    if task in tasks:
        tasks.remove(task)
        update_listbox()

delete_button = Button(root, text="Sil", command=delete_task)
delete_button.pack()

root.mainloop()