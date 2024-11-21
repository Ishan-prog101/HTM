from tkinter import*
from PIL import Image,ImageTk
from customtkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
import random
from tkinter import messagebox
class cust_win:
        def __init__(self,root):
                self.root=root
                self.root.title('CUSTOMER')
                self.root.geometry('1295x550+232+220')    #lenth(x)height and x-axis and y-axis
        #*********VARR########################
                self.ref=StringVar()
                x=random.randint(10000,100000)
                self.ref.set(str(x))


                self.name=StringVar()
                self.gen=StringVar()
                self.mb_no=StringVar()
                self.emid=StringVar()
                self.idproof=StringVar()
                self.idnum=StringVar()
                self.addrs=StringVar()
                self.pin=StringVar()
                self.nation=StringVar()
                
                


        #============label=======================================
                lbl_titile=Label(self.root,text="CUSTOMER DETAILS",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile.place(x=0,y=0,width=1295,height=55)
