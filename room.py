from tkinter import*
from PIL import Image,ImageTk
from customtkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
import random
from tkinter import messagebox


from datetime import datetime

class room_win:
        def __init__(self,root):
                self.root=root
                self.root.title('ROOM BOOKING')
                self.root.geometry('1295x550+232+220') 

                lbl_titile=Label(self.root,text="ROOM BOOKING",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile.place(x=0,y=0,width=1295,height=55)



                self.ref=StringVar()
                x=random.randint(10000,100000)
                self.ref.set(str(x))

                self.cont=StringVar()
                self.chk_in=StringVar()
                self.chk_out=StringVar()
                self.room=StringVar()
                self.roomno=StringVar()
                self.meal=StringVar()
                self.days=StringVar()
                self.tax=StringVar()
                self.cost=StringVar()
               



        #==================logo==================================
                imglogo=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\logo1.jpg')
                imglogo=imglogo.resize((55,53), Image.Resampling.LANCZOS)
                self.photologo=ImageTk.PhotoImage(imglogo)
                imglbl=Label(self.root,image=self.photologo,border=4)
                imglbl.place(x=0,y=1,width=55,height=53)


                #================Tk label frame======================
                lblframe=LabelFrame(self.root,bd=2,text='ROOM BOOKING',font=('Times New Roman',15,'bold','italic'),padx=2)
                lblframe.place(x=5,y=55,width=425,height=490)

 #======CONTACT no=======================
                lbl_cust_cont=Label(lblframe, text="--Contact Number--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_cont.grid(row=0, column=0)
                

                cont_entry = CTkEntry(master=lblframe,textvariable=self.cont,width=250, placeholder_text="CONTACT NO. ",corner_radius=10)
                cont_entry.grid(row=0,column=1)
#=================check in date============
                lbl_check_in=Label(lblframe, text="--Check In Date--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_check_in.grid(row=1, column=0)

                checkin_entry = CTkEntry(master=lblframe,textvariable=self.chk_in,width=250, placeholder_text="CHECK IN:",corner_radius=10)
                checkin_entry.grid(row=1,column=1)
#=================check out date============
                lbl_check_out=Label(lblframe, text="--Check Out Date--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_check_out.grid(row=2, column=0)

                checkout_entry = CTkEntry(master=lblframe,textvariable=self.chk_out,width=250, placeholder_text="CHECK OUT:",corner_radius=10)
                checkout_entry.grid(row=2,column=1)
#================type rooms====================
                lbl_room=Label(lblframe, text="--Rooms--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_room.grid(row=3, column=0)

                room_entry = CTkComboBox(master=lblframe, values=['King Bedroom With Golf View','King Bed With Runway View','ANDAAZ Signature King Room','Signature Room With Pool'],fg_color='lavender',border_color='navy',width=250)
                room_entry.grid(row=3,column=1)
                self.room=room_entry
                
#==================ava rooms========================

                lbl_avaroom=Label(lblframe, text="--Room Number--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_avaroom.grid(row=4, column=0)

                avaroom_entry = CTkEntry(master=lblframe,textvariable=self.roomno
                                         
                                         
                                         
                                         
                                         
                                         ,width=250, placeholder_text="CHECK IN:",corner_radius=10)
                avaroom_entry.grid(row=4,column=1)

#===========meal=======================================

                lbl_meal=Label(lblframe, text="--Meals--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_meal.grid(row=5, column=0)

                meal_entry = CTkEntry(master=lblframe,textvariable=self.meal,width=250, placeholder_text="Meal:",corner_radius=10)
                meal_entry.grid(row=5,column=1)
                 
#===================days===============
                lbl_days=Label(lblframe, text="--Number Of Days--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_days.grid(row=6, column=0)
               

                days_entry = CTkEntry(master=lblframe,textvariable=self.days,width=250, placeholder_text="NUMBER OF DAYS:",corner_radius=10)
                days_entry.grid(row=6,column=1)

#===================TAX===============================
                lbl_tax=Label(lblframe, text="--TAX--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_tax.grid(row=7, column=0)

                tax_entry = CTkEntry(master=lblframe,textvariable=self.tax,width=250, placeholder_text="TAX:",corner_radius=10)
                tax_entry.grid(row=7,column=1)

#===============cost==========================
                lbl_cost=Label(lblframe, text="--Total Bill--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cost.grid(row=8, column=0)

                cost_entry = CTkEntry(master=lblframe,textvariable=self.cost,width=250, placeholder_text="Cost:",corner_radius=10)
                cost_entry.grid(row=8,column=1)

#======ref no=======================
                lbl_ref=Label(lblframe, text="--Room Ref--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_ref.grid(row=10, column=0)

                ref_entry = CTkEntry(master=lblframe,textvariable=self.ref,width=250, placeholder_text="Ref ID:",corner_radius=10,state='read')
                ref_entry.grid(row=10,column=1)                
#=======================BILL=======================
                btn_bill=CTkButton(master=lblframe,text='BILL',command=self.total,font=('Georgia',18),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_bill.place(x=2,y=360)
#================btn=========================================
                btn_tkframe=CTkFrame(master=lblframe,border_width=2,border_color='black',width=412,height=40)
                btn_tkframe.place(x=2,y=400)

                btn_add=CTkButton(master=btn_tkframe,command=self.add_data,text='ADD',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_add.grid(row=0,column=0)

                btn_UPDATE=CTkButton(master=btn_tkframe,command=self.update_room,text='UPDATE',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_UPDATE.grid(row=0,column=1)

                btn_DELETE=CTkButton(master=btn_tkframe,command=self.mDelete,text='DELETE',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_DELETE.grid(row=0,column=2)

                btn_RESET=CTkButton(master=btn_tkframe,command=self.reset,text='RESET',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_RESET.grid(row=0,column=3)

#=======================IMGS OF ROOMS====================================================
                dlx_room=CTkLabel(master=self.root,text='KBGV(Rs.8000)',bg_color='khaki',font=('Times New Roman',20))
                dlx_room.place(x=470,y=62)

                dlxlogo=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\kbgv.jpg')
                dlxlogo=dlxlogo.resize((200,150), Image.Resampling.LANCZOS)
                self.photologo1=ImageTk.PhotoImage(dlxlogo)
                dlxlbl=Label(self.root,image=self.photologo1,border=4)
                dlxlbl.place(x=445,y=90,width=200,height=150)


                kb_room=CTkLabel(master=self.root,text='KBRV(Rs.9000)',bg_color='khaki',font=('Times New Roman',20))
                kb_room.place(x=690,y=62)
                kblogo=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\kbrv.jpg')
                kblogo=kblogo.resize((200,150), Image.Resampling.LANCZOS)
                self.photologo2=ImageTk.PhotoImage(kblogo)
                kblbl=Label(self.root,image=self.photologo2,border=4)
                kblbl.place(x=655,y=90,width=200,height=150)


                ask_room=CTkLabel(master=self.root,text='ASKR(Rs.11000)',bg_color='khaki',font=('Times New Roman',20))
                ask_room.place(x=890,y=62)
                asklogo=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\ASK1.jpg')
                asklogo=asklogo.resize((200,150), Image.Resampling.LANCZOS)
                self.photologo3=ImageTk.PhotoImage(asklogo)
                asklbl=Label(self.root,image=self.photologo3,border=4)
                asklbl.place(x=865,y=90,width=200,height=150)

                srp_room=CTkLabel(master=self.root,text='SRPV(Rs.12000)',bg_color='khaki',font=('Times New Roman',20))
                srp_room.place(x=1100,y=62)
                srplogo=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\ASK.jpeg')
                srplogo=srplogo.resize((200,150), Image.Resampling.LANCZOS)
                self.photologo4=ImageTk.PhotoImage(srplogo)
                srplbl=Label(self.root,image=self.photologo4,border=4)
                srplbl.place(x=1075,y=90,width=200,height=150)





                

#=======================SRCH TABLE=====================================
                Table_Frame=LabelFrame(self.root, bd=2,text="View Deatils And Search",font=("Times New Roman",15,"bold",'italic'), padx=2)
                Table_Frame.place(x=435, y=250,width=850, height=290)
        #===============srch by===============================================
                lbl_srch=Label(Table_Frame, text="--SEARCH BY--", font=("times new roman",12, "bold"),bg="goldenrod1")
                lbl_srch.grid(row=0, column=0)
               
                self.srchbox=StringVar()
                srch_combobox = CTkComboBox(master=Table_Frame, values=['CONTACT NO.',"ROOM NO."],fg_color='khaki',border_color='DeepSkyBlue2')
                srch_combobox.grid(row=0,column=1,padx=3)
                self.srchbox=srch_combobox

                self.txtsrch=StringVar()
                srch_entry = CTkEntry(master=Table_Frame,textvariable=self.txtsrch,width=250, placeholder_text="",corner_radius=10)
                srch_entry.grid(row=0,column=2,padx=2)
               

                btn_SEARCH=CTkButton(master=Table_Frame,command=self.srch,text='SEARCH',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_SEARCH.grid(row=0,column=3)

                btn_SHOW=CTkButton(master=Table_Frame,command=self.fetch_data,text='SHOW ALL',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_SHOW.grid(row=0,column=4,padx=1)

        #====================table data=====================
                details_table=Frame(Table_Frame, bd=2)
                details_table.place(x=0, y=40, width=840,height=220)

                scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)



                self.room_table=ttk.Treeview(details_table,columns=('c1','c2','c3','c4','c5','c6','c7','c8','c9'),
                                        show='headings',xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)      
                scroll_x.config(command=self.room_table.xview)
                scroll_y.config(command=self.room_table.yview)



                self.room_table.heading('c1',text='Ref.')
                self.room_table.heading('c2',text='CONTACT NO.')
                self.room_table.heading('c3',text='CHECK IN DATE')
                self.room_table.heading('c4',text='CHECK OUT DATE')
                self.room_table.heading('c5',text='ROOM')
                self.room_table.heading('c6',text='ROOM NO.')
                self.room_table.heading('c7',text='MEAL')
                self.room_table.heading('c8',text='NO. OF DAYS')
                self.room_table.heading('c9',text='BILL')

                self.room_table.column("c1", width=130)
                self.room_table.column("c2", width=130)
                self.room_table.column("c3", width=130)
                self.room_table.column("c4", width=130)
                self.room_table.column("c5", width=130)
                self.room_table.column("c6", width=130)
                self.room_table.column("c7", width=130)
                self.room_table.column("c8", width=130)
                self.room_table.column("c9", width=130)

                self.room_table.pack(fill=BOTH,expand=1)

                self.fetch_data()

                self.room_table.bind("<ButtonRelease-1>",self.get_cursor)#creating an event when mouse left btn is clicked
        #========add data ================================
        def add_data(self):
                if self.cont.get()=="" or self.chk_in.get()=="":
                        messagebox.showerror("Error", "All fields are requaired",parent=self.root)
                

                else:
                
                        try:
                                conn = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='ishan@120806',
                                database='hote_managementl'
                                                )
                                cursor = conn.cursor()
                                cursor.execute('insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                self.ref.get(),
                                                                                self.cont.get(),
                                                                                self.chk_in.get(),
                                                                                self.chk_out.get(),
                                                                                self.room.get(),
                                                                                self.roomno.get(),
                                                                                self.meal.get(),
                                                                                self.days.get(),
                                                                                self.cost.get()
                                                                                
                                                                                
                                                                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo('Success','Room Booked',parent=self.root)
                        except Exception as es:
                                messagebox.showwarning('Warning',f'Something Went Wrong:{str(es)}',parent=self.root)


#=========getting all the data==================
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room")
                rows=my_cursor.fetchall()
                if len(rows) !=0:
                        self.room_table.delete(*self.room_table.get_children())    #deletes all the rows in self.det table       
                        
                        '''“children” refers to the items or rows 
                        that are currently displayed in the Treeview. Each row in the Treeview is considered a “child” of the Treeview widget.'''
                        for i in rows:
                                self.room_table.insert("",END, values=i)
                                '''(""): This is the parent item. In this case, its an empty string, 
                                which means the new item will be inserted at the root of the Treeview.

END: This is the index where the new item will be inserted. END is a special constant that represents the last child of the parent. 
So, the new item will be inserted at the end of the list of existing items.

values=i: This is a tuple that contains the values of the new item.  i is a row of data fetched from a database.'''
                        conn.commit()
                conn.close()



        def get_cursor(self,event=''):
                        cursor_row=self.room_table.focus() #seletcting the row
                        content=self.room_table.item(cursor_row)#getting the data in row which i seletcted                       
                        row=content["values"]#opening the vlues and storing in  row var
                        self.ref.set(row[0]), #setting the data of row 0 to ref.
                        self.cont.set(row[1]), 
                        self.chk_in.set(row[2]),
                        self.chk_out.set(row[3]),
                        self.room.set(row[4]),
                        self.roomno.set(row[5]),
                        self.meal.set(row[6]),
                        self.days.set(row[7]),
                        self.bill.set(row[8])
                               
        #=========update==============================================================
        def update_room(self):
                if self.days.get()=="":
                        messagebox.showerror('ERROR','Please Enter Days Number',parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                        my_cursor=conn.cursor()#this line creates a cursor object. The cursor is used to execute SQL commands.
                        my_cursor.execute('update room set `CONTACT NO.`=%s, `CHECK IN DATE`=%s, `CHECK OUT DATE`=%s, `ROOM`=%s, `ROOM NO.`=%s, `MEAL`=%s, `NO. OF DAYS`=%s, `BILL`=%s where `Ref`=%s',(
                                                                        
                        
                                                                                self.cont.get(),
                                                                                
                                                                                self.chk_in.get(),
                                                                                self.chk_out.get(),
                                                                                self.room.get(),
                                                                                self.roomno.get(),
                                                                                self.meal.get(),
                                                                                self.days.get(),
                                                                                self.cost.get(),
                                                                                self.ref.get()
                                                                                                                 
                                                                                                                ))
                                #"""BACKTICK(`)was added so tht the spaces or any special char can be ignored"""       
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('UPDATE','Room Details Has Been Updated',parent=self.root)

#=============delete==============================
        def mDelete(self):
                delete=messagebox.askyesno('HOTEL RIMBERIO','DO YOU WANT TO DELETE THIS ROOM DETAILS?',parent=self.root)           
                if delete==True:
                        conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                        my_cursor=conn.cursor()
                        my_cursor.execute("delete from room where Ref=%s",(self.ref.get(),))
                        messagebox.showinfo('Success','Data Deleted',parent=self.root)
                        conn.commit()
                        self.fetch_data()#to display updated data
                        conn.close()      

                else:
                        return



#========================reset==============================
        def reset(self):
                
                self.cont.set(""), 
                
                self.chk_in.set(""),
                self.chk_out.set(""),
                
                self.days.set(""),
                self.room.set("")
                self.roomno.set(""),
                self.meal.set(""),
                self.cost.set(""),
                self.tax.set(""),
                
                
                x=random.randint(10000,100000)
                self.ref.set(str(x))

#==total===========================
        def total(self):
                indate=self.chk_in.get()
                outdate=self.chk_out.get()
                indate=datetime.strptime(indate,'%d/%m/%Y')
                outdate=datetime.strptime(outdate,'%d/%m/%Y')
                self.days.set(abs(outdate-indate).days)
                
                if self.meal.get().casefold()=="breakfast".casefold():
                        if self.room.get()=="King Bedroom With Golf View":
                                q1=float(300)
                                q2=float (8000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="King Bed With Runway View":
                                q1=float(500)
                                q2=float (9000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="ANDAAZ Signature King Room":
                                q1=float(700)
                                q2=float (11000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="Signature Room With Pool":
                                q1=float(700)
                                q2=float (12000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                elif self.meal.get().casefold()=="lunch".casefold():
                        if self.room.get()=="King Bedroom With Golf View":
                                q1=float(400)
                                q2=float (8000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="King Bed With Runway View":
                                q1=float(600)
                                q2=float (9000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="ANDAAZ Signature King Room":
                                q1=float(700)
                                q2=float (11000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="Signature Room With Pool":
                                q1=float(800)
                                q2=float (11000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                elif self.meal.get().casefold()=="dinner".casefold():
                        if self.room.get()=="King Bedroom With Golf View":
                                q1=float(600)
                                q2=float (8000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="King Bed With Runway View":
                                q1=float(700)
                                q2=float (9000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="ANDAAZ Signature King Room":
                                q1=float(800)
                                q2=float (11000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
                        elif self.room.get()=="Signature Room With Pool":
                                q1=float(900)
                                q2=float (11000)
                                q3=float(self.days.get())
                                q4=float(q1+q2)
                                q5=float(q3*q4)
                                tax=(q5*0.18)
                             
                                Tax = "Rs." + str(tax)
                                TT = "Rs." + str(tax + q5)
                                self.tax.set(Tax)
                        
                                self.cost.set(TT)
#=====srch sys======================
        def srch(self):
                conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='ishan@120806',
                        database='hote_managementl'
                                        )
                cursor = conn.cursor()


                '''In the line query = "SELECT * FROM room WHERE {} LIKE %s".format(self.srchv.get()), 
                the {} is a placeholder that gets replaced with the value of self.srchv.get(), which is the column name you want to search in.

The %s in the query is a placeholder for the search term. 
However, because youre using a LIKE clause in your SQL query, you need to include % symbols around the search term (for example, %search_term%). 
This is done in the execute method: cursor.execute(query, ('%' + self.txt.get() + '%',)).

This way, the SQL query becomes something like SELECT * FROM room WHERE column_name LIKE '%search_term%', 
which selects all rows from the room table where column_name contains search_term.'''



                query = "SELECT * FROM room WHERE `{}` LIKE %s".format(self.srchbox.get())
                cursor.execute(query, ('%' + self.txtsrch.get() + '%',))
                rows = cursor.fetchall()
                
                if len(rows) != 0:
                        messagebox.showinfo('FOUND','Person Found',parent=self.root)
                        self.room_table.delete(*self.room_table.get_children())#if row isnt empty i.e a match is found , it deletes all the existing rows and then
                        for i in rows:#for loop adds the row with the matching data at the end of table
                                self.room_table.insert("", END, values=i)

                else:
                        messagebox.showerror('Error', 'Person not found',parent=self.root)               
                        conn.commit()#saves the data to database
                conn.close()







if __name__ == "__main__":
    root=Tk()
    obj=room_win(root)
    root.mainloop()


    #===================END====================================================================================================================================================