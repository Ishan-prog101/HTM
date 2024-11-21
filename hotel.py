from tkinter import*    
from PIL import Image,ImageTk
from customtkinter import *
from customer import cust_win
from room import room_win
from details import detail_win
from report import report_win
class HotelManagementSystem:
        def __init__(self,root):
                self.root=root
                self.root.title("HOTEL MANAGEMENT")
                self.root.geometry('1520x780+0+0')
                """The __init__ method allows you to set up the initial state of the object, initialize its attributes, 
                and perform any necessary setup tasks. It's a crucial part of object-oriented programming in Python
                and is often used to ensure that objects start in a consistent and usable state when they are created"""
        #====================first img===========================        
                img1=Image.open(r'C:\Users\ishan\OneDrive\Desktop\CODING\HOTEL MANAGEMENT SYS\pic 4.jpg')
                img1=img1.resize((1350,140), Image.Resampling.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                lbl=Label(self.root,image=self.photoimg1,border=2)
                lbl.place(x=220,y=0,width=1350,height=140)


                
        #=======================logo===============
                imglogo=Image.open(r'C:\Users\ishan\OneDrive\Desktop\CODING\HOTEL MANAGEMENT SYS\logo1.jpg')
                imglogo=imglogo.resize((230,140), Image.Resampling.LANCZOS)
                self.photologo=ImageTk.PhotoImage(imglogo)
                imglbl=Label(self.root,image=self.photologo,border=4)
                imglbl.place(x=0,y=0,width=230,height=140)

        #============title=========================
                lbl_titile=Label(root,text="HOTEL RIMBERIO",font=('Bahnschrift Light Condensed',35,'bold'),bg='orchid2',
                                fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile.place(x=0,y=140,width=1520,height=55)
        #==============frame==============================
                frame=CTkFrame(master=root,fg_color='transparent',border_color='gold',border_width=4,width=1520,height=590)
                frame.place(x=0,y=190)

                imgrlogo=Image.open(r'C:\Users\ishan\OneDrive\Desktop\CODING\HOTEL MANAGEMENT SYS\pic 3.png')
                imgrlogo=imgrlogo.resize((230,140), Image.Resampling.LANCZOS)
                self.photologor=ImageTk.PhotoImage(imgrlogo)
                imgrlbl=Label(frame,image=self.photologor,border=4)
                imgrlbl.place(x=0,y=240,width=230,height=140)

                img4=Image.open(r'C:\Users\ishan\OneDrive\Desktop\CODING\HOTEL MANAGEMENT SYS\ASK1.jpg')
                img4=img4.resize((234,140),Image.Resampling.LANCZOS)
                self.img4=ImageTk.PhotoImage(img4)
                img4lbl=Label(frame,image=self.img4,border=4)
                img4lbl.place(x=0,y=380)

        #==============MENU======================================================================
                lbl_menu=Label (frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", 
                                fg="gold",highlightthickness=2,highlightbackground='gold')
                lbl_menu.place(x=0, y=0,width=230)
        #===============framebttn================
                btnframe=CTkFrame(master=frame,fg_color='black',border_color='gold',border_width=4,width=230,height=160)
                btnframe.place(x=0,y=40)

                cusbtn=CTkButton(master=btnframe,fg_color='black',border_color='gold',
                                corner_radius=2,border_width=4,text='CUSTOMER',font=('Times New Roman',18),hover_color='cyan',
                                text_color='gold',width=230,height=40,command=self.cust_det)
                cusbtn.place(x=0,y=0)

                roombtn=CTkButton(master=btnframe,fg_color='black',border_color='gold',
                                corner_radius=2,border_width=4,text='ROOMS',font=('Times New Roman',18),hover_color='cyan',
                                text_color='gold',width=230,height=40,command=self.room)
                roombtn.place(x=0,y=40)

                detabtn=CTkButton(master=btnframe,command=self.detail,fg_color='black',border_color='gold',
                                corner_radius=2,border_width=4,text='DETAILS',font=('Times New Roman',18),hover_color='cyan',
                                text_color='gold',width=230,height=40)
                detabtn.place(x=0,y=80)

                repbtn=CTkButton(master=btnframe,command=self.report,fg_color='black',border_color='gold',
                                corner_radius=2,border_width=4,text='REPORT',font=('Times New Roman',18),hover_color='cyan',
                                text_color='gold',width=230,height=40)
                repbtn.place(x=0,y=120)

                logoutbtn=CTkButton(master=btnframe,fg_color='black',border_color='gold',
                                corner_radius=2,border_width=4,text='LOGOUT',font=('Times New Roman',18),hover_color='cyan',
                                text_color='gold',width=230,height=40)
                logoutbtn.place(x=0,y=160)
        #=========pic==================================
                img3=Image.open(r"C:\Users\ishan\OneDrive\Desktop\CODING\HOTEL MANAGEMENT SYS\pic 2.jpg")
                img3=img3.resize((1310,570), Image.Resampling.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                lblimg3=Label(frame,image=self.photoimg3)
                lblimg3.place(x=232,y=2,width=1280,height=585)

                

        #=====func===========================
        def cust_det(self):
                self.nw=Toplevel(self.root)
                self.app=cust_win(self.nw)

        def room(self):
                self.nw=Toplevel(self.root)
                self.app=room_win(self.nw)

        def detail(self):
                self.nw=Toplevel(self.root)
                self.app=detail_win(self.nw)

        def report(self):
                self.nw=Toplevel(self.root)
                self.app=report_win(self.nw)













if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
