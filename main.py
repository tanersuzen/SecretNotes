import tkinter
from tkinter import *
import base64
from tkinter import messagebox

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def saving_notes():
    title = title_input.get()
    message = secret_input.get("1.0",END)
    master_key = master_key_input.get()

    if len(title) == 0:
        messagebox.showwarning(title="Error!",message="Please enter Title")

    elif len(message)== 1:
            messagebox.showwarning(title="Error!", message="Please enter Notes")

    elif len(master_key) == 0:
            messagebox.showwarning(title="Error!", message="Please enter Master Key")
    else:
        encrypted_message = encode(master_key,message)

        try:
            with open("MySecretNotes.txt","a") as data_file:
                data_file.write(f"\n{title}\n{encrypted_message}")
        except FileNotFoundError:
            with open("MySecretNotes.txt","w") as data_file:
                data_file.write(f"\n{title}\n{encrypted_message}")
        finally:
            title_input.delete(0,END)
            secret_input.delete("1.0",END)
            master_key_input.delete(0,END)

def decrypting_notes():
    already_encrypted_message=secret_input.get("1.0",END)
    key_word = master_key_input.get()
    if len(already_encrypted_message) == 1:
        messagebox.showwarning(title="Error!", message="Please enter Secret")
    elif len(key_word) == 0:
        messagebox.showwarning(title="Error!", message="Please enter Master Key")
    else:
        try:
            decrypted_message = decode(key_word, already_encrypted_message)
            secret_input.delete("1.0",END)
            secret_input.insert("1.0",decrypted_message)
        except:
            messagebox.showinfo(title="Error!",message="Please Enter Encrypted Text!")

window = Tk()
window.title("Secret Notes")
window.minsize(width=300,height=600)
window.config(padx=10,pady=10,bg="light grey")


photo = PhotoImage(file="topsecret.png")
photo_label=Label(image=photo)
photo_label.config(bg="light grey")
photo_label.pack()

title_label = Label(text="Enter your title")
title_label.config(bg="light grey",fg="black",font=("Arial",16,"normal"))
title_label.pack()

title_input = Entry(width=30)
title_input.config(bg="white",fg="black")
title_input.pack()

secret_label = Label(text="Enter your secret")
secret_label.config(bg="light grey",fg="black",font=("Arial",16,"normal"))
secret_label.pack()

secret_input = Text(width=50,height=25)
secret_input.config(bg="white",fg="black")
secret_input.pack()

master_key_label = Label(text="Enter your master key")
master_key_label.config(bg="light grey",fg="black",font=("Arial",16,"normal"))
master_key_label.pack()

master_key_input = Entry(width=30)
master_key_input.config(bg="white",fg="black")
master_key_input.pack()

Encrypt_button = Button(text="Save & Encrypt",bg="grey",borderwidth=0,pady=3,highlightcolor="grey",highlightthickness=0,command=saving_notes)
Encrypt_button.pack()

Decrypt_button = Button(text="Decrypt",bg="grey",borderwidth=0,pady=3,highlightcolor="grey",highlightthickness=0,command=decrypting_notes)
Decrypt_button.pack()

tkinter.mainloop()