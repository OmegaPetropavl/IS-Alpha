import customtkinter as ctk
from customtkinter import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

# Selecting GUI theme - dark, 
# light , system (for system default)
ctk.set_appearance_mode("light")
  
# Selecting color theme-blue, green, dark-blue
ctk.set_default_color_theme("green")
  
app = ctk.CTk()
app.geometry("400x450")
app.title("АИС 'Аренда помещений'")

# defining the login function
def login():
    # pre-defined username
    username = "Geeks" 
    # pre-defined password
    password = "12345" 
    

    if user_entry.get() == username and user_pass.get() == password:
        showinfo(title="Login Successful",
          message="You have logged in Successfully!")
        new_window = ctk.CTkToplevel(app)
        ctk.CTk.destroy
        new_window.title("New Window")
        new_window.geometry("800x600")
        ctk.CTkLabel(new_window,
                     text="GeeksforGeeks is best \
                     for learning ANYTHING !!").pack()
        

          

    elif user_entry.get() == username and user_pass.get() != password:
        showwarning(title='Неправильный пароль',
             message='Пожалуйста, проверьте правильность ввода пароля')
        

    elif user_entry.get() != username and user_pass.get() == password:
        showwarning(title='Неправильный логин',
             message='Пожалуйста, проверьте правильность ввода логина')
        

    else:
        showerror(title="Login Failed",
           message="Invalid Username and password")
# Set the label

# Create a frame
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,
           fill='both',expand=True)
  
# Set the label inside the frame
label = ctk.CTkLabel(master=frame,
                     text='Добро пожаловать!')
label.pack(pady=52,padx=1)

  
# Create the text box for taking
# username input from user
user_entry= ctk.CTkEntry(master=frame,
                         placeholder_text="Логин")
user_entry.pack(pady=1,padx=10)
  
# Create a text box for taking 
# password input from user
user_pass= ctk.CTkEntry(master=frame,
                        placeholder_text="Пароль",
                        show="*")
user_pass.pack(pady=12,padx=10)
  
# Create a login button to login
button = ctk.CTkButton(master=frame,
                       text='Login',command=login)
button.pack(pady=12,padx=10)
  
# Create a remember me checkbox
checkbox = ctk.CTkCheckBox(master=frame,
                           text='Запомнить меня')
checkbox.pack(pady=12,padx=10)

app.mainloop()