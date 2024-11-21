import tkinter
import customtkinter as ctk

from tkinter import messagebox
import mysql.connector
from tkinter import *
from hotel import HotelManagementSystem
from tkinter import*
from PIL import Image,ImageTk

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')





class LoginForm:
    def __init__(self,root):

        self.root = root
        self.root.geometry('1500x1400')
        self.root.title('LOGIN')

        #photoimg is a class in tkinter tht allows u to display images on a label or bttn
        img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\pic 1.jpg'))
        background_label = ctk.CTkLabel(master=root, image=img1)
        background_label.pack()

        # Create a frame for the login form
        frame = ctk.CTkFrame(master=root, height=460, width=320, border_width=5, border_color='black')
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Create login widgets
        label_welcome = ctk.CTkLabel(master=frame, text='Welcome Back!', font=('Georgia', 30, 'bold'))
        label_welcome.place(x=45, y=20)

        label_log_in = ctk.CTkLabel(master=frame, text='Log Into Your Account', font=('Georgia', 20, 'italic'))
        label_log_in.place(x=65, y=55)

        self.username_entry = ctk.CTkEntry(master=frame, width=250, placeholder_text="Username:")
        self.username_entry.place(x=40, y=140)

        self.password_entry = ctk.CTkEntry(master=frame, width=250, placeholder_text="Password:", show='*')
        self.password_entry.place(x=40, y=220)


        login_button = ctk.CTkButton(master=frame, text='Login', width=240, corner_radius=20, font=('Georgia', 25), command=self.check_login)
        login_button.place(x=40, y=350)


    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ishan@120806',
            database='login'
                            )
        cursor = conn.cursor()

        # Retrieve user data from the database
        cursor.execute("SELECT username, password FROM users WHERE username=%s", (username,))
        user_data = cursor.fetchone()

        if user_data is not None and user_data[1] == password:
            messagebox.showinfo('Success', 'Login Successful')
    
            self.nw=Toplevel(self.root)
            self.app=HotelManagementSystem(self.nw)
            
        else:
            messagebox.showerror('Invalid', 'Wrong credentials')
        
        # Close the database connection
        cursor.close()
        conn.close()

    '''def hotel(self):
        self.nw=Toplevel(self.root)
        self.app=HotelManagementSystem(self.nw)'''


if __name__ == "__main__":
    root=Tk()
    obj=LoginForm(root)
    root.mainloop()

