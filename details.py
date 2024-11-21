from tkinter import*
from PIL import Image,ImageTk
from customtkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
import random
from tkinter import messagebox

from datetime import datetime



class detail_win:
        def __init__(self,root):
                self.root=root
                self.root.title('DETAILS')
                self.root.geometry('1295x550+232+220') 

                lbl_titile=Label(self.root,text="ROOM DETAILS",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile.place(x=0,y=0,width=1295,height=55)


                self.room=StringVar()
                self.roomtype=StringVar()

    #==================logo==================================
                imglogo=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\logo1.jpg')
                imglogo=imglogo.resize((55,53), Image.Resampling.LANCZOS)
                self.photologo=ImageTk.PhotoImage(imglogo)
                imglbl=Label(self.root,image=self.photologo,border=4)
                imglbl.place(x=0,y=1,width=55,height=53)


                #================Tk label frame======================
                lblframe=LabelFrame(self.root,bd=2,text='ROOM BOOKING',font=('Times New Roman',15,'bold','italic'),padx=2)
                lblframe.place(x=40,y=90,width=525,height=350)

                lbl_cust_ref=Label(lblframe, text="--ROOM NO.--", font=("times new roman",12, "bold"),bg="goldenrod1", padx=2, pady=6)
                lbl_cust_ref.grid(row=0, column=0)
                room_entry = CTkEntry(master=lblframe,textvariable=self.room,width=250, placeholder_text="Room No:",corner_radius=10)
                room_entry.grid(row=0,column=1)

                room_ref=Label(lblframe, text="--ROOM TYPE--", font=("times new roman",12, "bold"),bg="goldenrod1", padx=2, pady=6)
                room_ref.grid(row=1, column=0)
                roomtype_entry = CTkEntry(master=lblframe,textvariable=self.roomtype,width=250, placeholder_text="Room Type:",corner_radius=10)
                roomtype_entry.grid(row=1,column=1)


                lbl_srch=Label(lblframe, text="--AVAILABILITY--", font=("times new roman",12, "bold"),bg="goldenrod1")
                lbl_srch.grid(row=3, column=0)


                self.srchv1=StringVar()
                srch_combobox = CTkComboBox(master=lblframe, values=['Occupied',"Not Occupied"],fg_color='khaki',border_color='DeepSkyBlue2')
                srch_combobox.grid(row=3,column=1,padx=3)
                self.srchv1=srch_combobox


                img1=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\kbgv.jpg')
                img1=img1.resize((220,150), Image.Resampling.LANCZOS)
                self.photologo1=ImageTk.PhotoImage(img1)
                imglbl1=Label(self.root,image=self.photologo1,border=4)
                imglbl1.place(x=60,y=230,width=220,height=150)

                img2=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\pool.jpg')
                img2=img2.resize((220,150), Image.Resampling.LANCZOS)
                self.photologo2=ImageTk.PhotoImage(img2)
                imglbl2=Label(self.root,image=self.photologo2,border=4)
                imglbl2.place(x=300,y=230,width=220,height=150)


                img3=Image.open(r'C:\Users\gunja\Desktop\HOTEL MANAGEMENT SYS\pic 4.jpg')
                img3=img3.resize((1288,130), Image.Resampling.LANCZOS)
                self.photologo3=ImageTk.PhotoImage(img3)
                imglbl3=Label(self.root,image=self.photologo3,border=4)
                imglbl3.place(x=3,y=430,width=1288,height=130)



            




                btn_tkframe=CTkFrame(master=lblframe,border_width=2,border_color='black',width=412,height=40)
                btn_tkframe.place(x=43,y=270)

                btn_add=CTkButton(master=btn_tkframe,command=self.add_data,text='ADD',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_add.grid(row=0,column=0)

                btn_UPDATE=CTkButton(master=btn_tkframe,command=self.update_cust,text='UPDATE',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_UPDATE.grid(row=0,column=1)

                btn_DELETE=CTkButton(master=btn_tkframe,command=self.mDelete,text='DELETE',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_DELETE.grid(row=0,column=2)

                btn_RESET=CTkButton(master=btn_tkframe,command=self.reset,text='RESET',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_RESET.grid(row=0,column=3)

#==========making table=============================

                Table_Frame=LabelFrame(self.root, bd=2,text="View Deatils And Search",font=("Times New Roman",15,"bold",'italic'), padx=2)
                Table_Frame.place(x=635, y=90,width=625,height=300)


#======================table
                details_table=Frame(Table_Frame, bd=2)
                details_table.place(x=10, y=50, width=530,height=220)

               
                scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)



                self.det_table=ttk.Treeview(details_table,columns=('c1','c2','c3'),
                                        show='headings',yscrollcommand=scroll_y.set)
                
                
                
                scroll_y.pack(side=RIGHT,fill=Y)      
                
                scroll_y.config(command=self.det_table.yview)




                self.det_table.heading('c1',text='Room')
                self.det_table.heading('c2',text='Room Type')
                self.det_table.heading('c3',text='Availability')


                self.det_table.column("c1", width=130)
                self.det_table.column("c2", width=130)
                self.det_table.column("c3", width=130)

                self.det_table.pack(fill=BOTH,expand=1)
                
                self.fetch_data()

        #made det_table an instance variable by putting self before===========================

                self.det_table.bind("<ButtonRelease-1>",self.get_cursor)




#======srchby==========================================
                lbl_srch=Label(Table_Frame, text="--SEARCH BY--", font=("times new roman",12, "bold"),bg="goldenrod1")
                lbl_srch.grid(row=0, column=0)

                self.srchv=StringVar()
                srch_combobox = CTkComboBox(master=Table_Frame, values=['Room NO.',"Room Type",'Availability'],fg_color='khaki',border_color='DeepSkyBlue2')
                srch_combobox.grid(row=0,column=1,padx=3)
                self.srchv=srch_combobox

                self.txt=StringVar()
                srch_entry = CTkEntry(master=Table_Frame,textvariable=self.txt,width=100, placeholder_text="",corner_radius=10)
                srch_entry.grid(row=0,column=2,padx=2)
                

                btn_SEARCH=CTkButton(master=Table_Frame,command=self.srch,text='SEARCH',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=75)
                btn_SEARCH.grid(row=0,column=3)

                btn_SHOW=CTkButton(master=Table_Frame,command=self.fetch_data,text='SHOW ALL',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=75)
                btn_SHOW.grid(row=0,column=4,padx=1)
#-------------add btn datA==============================
        def add_data(self):
                if self.room.get()=="" or self.roomtype.get()=="":
                        messagebox.showerror("Error", "All fields are required",parent=self.root)
                

                else:
                
                        try:
                                conn = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='ishan@120806',
                                database='hote_managementl'
                                                )
                                cursor = conn.cursor()
                                cursor.execute('insert into detail values(%s,%s,%s)',(
                                                                                self.room.get(),
                                                                                self.roomtype.get(),
                                                                                self.srchv1.get()
                                                                                
                                                                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo('Success','Room Details Has Been Added Successfully',parent=self.root)
                        except Exception as es:
                                messagebox.showwarning('Warning',f'Something Went Wrong:{str(es)}',parent=self.root)
#=====get all data===========================================
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from detail")
                rows=my_cursor.fetchall()
                if len (rows) !=0:
                        self.det_table.delete(*self.det_table.get_children())    #deletes all the rows in self.det table       
                        
                        '''“children” refers to the items or rows 
                        that are currently displayed in the Treeview. Each row in the Treeview is considered a “child” of the Treeview widget.'''
                        for i in rows:
                                self.det_table.insert("",END, values=i)
                                '''(""): This is the parent item. In this case, its an empty string, 
                                which means the new item will be inserted at the root of the Treeview.

END: This is the index where the new item will be inserted. END is a special constant that represents the last child of the parent. 
So, the new item will be inserted at the end of the list of existing items.

values=i: This is a tuple that contains the values of the new item.  i is a row of data fetched from a database.'''
                        conn.commit()
                        conn.close()

#========event=============================================
        def get_cursor(self,event=''):
                        cursor_row=self.det_table.focus() #seletcting the row
                        content=self.det_table.item(cursor_row)#getting the data in row which i seletcted                       
                        row=content["values"]#opening the vlues and storing in  row var
                        self.room.set(row[0]), #setting the data of row 0 to ref.
                        self.roomtype.set(row[1]), 
#================update/del/reset=============================
        def update_cust(self):
                if self.room.get()=="":
                        messagebox.showerror('ERROR','Please Enter Room Number',parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                        my_cursor=conn.cursor()#this line creates a cursor object. The cursor is used to execute SQL commands.
                        my_cursor.execute('update detail set `Room Type`=%s, `Availability`=%s where `Room NO.`=%s',(
                                                                        
                        
                                                                        
                                                                        
                                                                        self.roomtype.get(),
                                                                        self.srchv1.get(),
                                                                        self.room.get()
                                                                                                          
                                                                                                                ))
                                #"""BACKTICK(`)was added so tht the spaces or any special char can be ignored"""       
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('UPDATE','ROOM Details Has Been Updated',parent=self.root)

                '''%s is used as a placeholder for the values you want to update in the database. When the execute method is called, 
                each %s in the SQL command is replaced by the corresponding value in the tuple that follows it. For example,
 the first %s is replaced by the value of self.name.get(), the second %s is replaced by the value of self.gen.get(), and so on.'''

                
        def mDelete(self):
                delete=messagebox.askyesno('HOTEL RIMBERIO','DO YOU WANT TO DELETE THIS ROOM DETAILS?',parent=self.root)           
                if delete==True:
                        conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                        my_cursor=conn.cursor()
                        my_cursor.execute("delete from detail where `Room NO.`=%s",(self.room.get(),))
                        conn.commit()
                        self.fetch_data()#to display updated data
                        conn.close()      

                else:
                                return
                        
        def reset(self):
                
                self.room.set(""), 
                
                self.roomtype.set(""),
                self.srchv1.set(""),
                
#==============srch===========================================================


        def srch(self):
                conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='ishan@120806',
                        database='hote_managementl'
                                        )
                cursor = conn.cursor()


                '''In the line query = "SELECT * FROM detail WHERE {} LIKE %s".format(self.srchv.get()), 
                the {} is a placeholder that gets replaced with the value of self.srchv.get(), which is the column name we want to search in.

The %s in the query is a placeholder for the search term. 
However, because we are using a LIKE clause in our SQL query, we need to include % symbols around the search term (for example, %search_term%). 
This is done in the execute method: cursor.execute(query, ('%' + self.txt.get() + '%',)).

This way, the SQL query becomes something like SELECT * FROM detail WHERE column_name LIKE '%search_term%', 
which selects all rows from the detail table where column_name contains search_term.'''



                query = "SELECT * FROM detail WHERE `{}` LIKE %s".format(self.srchv.get())
                cursor.execute(query, ('%' + self.txt.get() + '%',))
                rows = cursor.fetchall()
                
                if len(rows) != 0:
                        messagebox.showinfo('FOUND','Person Found')
                        self.det_table.delete(*self.det_table.get_children())#if row isnt empty i.e a match is found , it deletes all the existing rows and then
                        for i in rows:#for loop adds the row with the matching data at the end of table
                                self.det_table.insert("", END, values=i)

                else:
                        messagebox.showerror('Error', 'Person not found')               
                        conn.commit()#saves the data to database
                conn.close()



if __name__ == "__main__":
    root=Tk()
    obj=detail_win(root)
    root.mainloop()
