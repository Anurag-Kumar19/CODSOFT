from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Contact Book")
root.geometry("700x500")
root.config(bg="#f5f5f5")

contacts = []


def add_contact():
    name = entry_name.get().strip()
    mobile = entry_mobile.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name == "" or mobile == "":
        messagebox.showwarning("Warning", "Name and Mobile No. are required!")
        return

    contacts.append({
        "Name": name,
        "Mobile": mobile,
        "Email": email,
        "Address": address
    })
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    view_contacts()

def view_contacts():
    listbox.delete(0, END)
    for i, contact in enumerate(contacts, start=1):
        listbox.insert(END, f"{i}. {contact['Name']} | {contact['Mobile']} | {contact['Email']} | {contact['Address']}")

def search_contact():
    search_term = entry_search.get().strip().lower()
    listbox.delete(0, END)
    for i, contact in enumerate(contacts, start=1):
        if (search_term in contact['Name'].lower() or
            search_term in contact['Mobile'] or
            search_term in contact['Email'].lower() or
            search_term in contact['Address'].lower()):
            listbox.insert(END, f"{i}. {contact['Name']} | {contact['Mobile']} | {contact['Email']} | {contact['Address']}")
    if listbox.size() == 0:
        listbox.insert(END, "No results found.")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        del contacts[index]
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
        view_contacts()
    except:
        messagebox.showwarning("Warning", "Please select a contact to delete!")

def update_contact():
    try:
        index = listbox.curselection()[0]
        name = entry_name.get().strip()
        mobile = entry_mobile.get().strip()
        email = entry_email.get().strip()
        address = entry_address.get().strip()

        if name == "" or mobile == "":
            messagebox.showwarning("Warning", "Name and Mobile No. are required!")
            return

        contacts[index] = {
            "Name": name,
            "Mobile": mobile,
            "Email": email,
            "Address": address
        }
        messagebox.showinfo("Updated", "Contact updated successfully!")
        clear_entries()
        view_contacts()
    except:
        messagebox.showwarning("Warning", "Please select a contact to update!")

def clear_entries():
    entry_name.delete(0, END)
    entry_mobile.delete(0, END)
    entry_email.delete(0, END)
    entry_address.delete(0, END)



Label(root, text="Name:", bg="#f5f5f5").place(x=20, y=20)
entry_name = Entry(root, width=25)
entry_name.place(x=100, y=20)

Label(root, text="Mobile:", bg="#f5f5f5").place(x=20, y=60)
entry_mobile = Entry(root, width=25)
entry_mobile.place(x=100, y=60)

Label(root, text="Email:", bg="#f5f5f5").place(x=20, y=100)
entry_email = Entry(root, width=25)
entry_email.place(x=100, y=100)

Label(root, text="Address:", bg="#f5f5f5").place(x=20, y=140)
entry_address = Entry(root, width=25)
entry_address.place(x=100, y=140)


Button(root, text="Add", width=12, command=add_contact, bg="lightgreen").place(x=350, y=20)
Button(root, text="Update", width=12, command=update_contact, bg="lightblue").place(x=350, y=60)
Button(root, text="Delete", width=12, command=delete_contact, bg="salmon").place(x=350, y=100)
Button(root, text="View All", width=12, command=view_contacts, bg="orange").place(x=350, y=140)

Label(root, text="Search:", bg="#f5f5f5").place(x=20, y=200)
entry_search = Entry(root, width=25)
entry_search.place(x=100, y=200)
Button(root, text="Search", width=12, command=search_contact, bg="yellow").place(x=350, y=200)

 
listbox = Listbox(root, width=100, height=15)
listbox.place(x=20, y=250)

root.mainloop()
