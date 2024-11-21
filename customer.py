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

        #==================logo==================================
                imglogo=Image.open(r'C:\Users\ishan\OneDrive\Desktop\CODING\HOTEL MANAGEMENT SYS\logo1.jpg')
                imglogo=imglogo.resize((55,53), Image.Resampling.LANCZOS)
                self.photologo=ImageTk.PhotoImage(imglogo)
                imglbl=Label(self.root,image=self.photologo,border=4)
                imglbl.place(x=0,y=1,width=55,height=53)
        #================Tk label frame======================
                lblframe=LabelFrame(self.root,bd=2,text='Customer Details',font=('Times New Roman',15,'bold','italic'),padx=2)
                lblframe.place(x=5,y=55,width=425,height=490)
        #======ref no=======================
                lbl_cust_ref=Label(lblframe, text="--Customer Ref--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_ref.grid(row=0, column=0)

                ref_entry = CTkEntry(master=lblframe,textvariable=self.ref,width=250, placeholder_text="Ref ID:",corner_radius=10,state='read')
                ref_entry.grid(row=0,column=1)
        #==============cust name==================
                lbl_cust_name=Label(lblframe,text="--Customer Name--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_name.grid(row=1, column=0)

                name_entry = CTkEntry(master=lblframe,textvariable=self.name,width=250, placeholder_text="Name:",corner_radius=10)
                name_entry.grid(row=1,column=1)   
        #========gender========================================
                lbl_cust_gender=Label(lblframe, text="--Customer Gender--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_gender.grid(row=2, column=0)

                gender_entry = CTkComboBox(master=lblframe, values=['Male','Female'],fg_color='lavender',border_color='navy')
                gender_entry.grid(row=2,column=1)
                self.gen=gender_entry
                
        #============mobile===========================
                lbl_cust_mb=Label(lblframe, text="--Customer Mobile--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_mb.grid(row=4, column=0)

                mb_entry = CTkEntry(master=lblframe,textvariable=self.mb_no, width=250, placeholder_text="Number:",corner_radius=10)
                mb_entry.grid(row=4,column=1)     
        #=====emailid=================================
                lbl_cust_mail=Label(lblframe, text="--Customer Mail--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_mail.grid(row=5, column=0)

                id_entry = CTkEntry(master=lblframe,textvariable=self.emid, width=250, placeholder_text="Mail ID:",corner_radius=10)
                id_entry.grid(row=5,column=1)
        #==============id proof==========
                lbl_cust_id=Label(lblframe, text="--Verification ID--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_id.grid(row=7, column=0)

                idno_entry = CTkComboBox(master=lblframe, values=['Aadhar Card','Driving License','Pan Card','Passport'],fg_color='lavender',border_color='navy')
                idno_entry.grid(row=7,column=1)
                self.idproof=idno_entry

                lbl_cust_idno=Label(lblframe, text="--ID NUM:--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_idno.grid(row=8, column=0)

                idno_entry = CTkEntry(master=lblframe,textvariable=self.idnum, width=250, placeholder_text="ID NUMBER:",corner_radius=10)
                idno_entry.grid(row=8,column=1)

        #=======addresss===================
                lbl_cust_add=Label(lblframe, text="--Customer Address--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_add.grid(row=9, column=0)

                address_entry = CTkEntry(master=lblframe,textvariable=self.addrs, width=250, placeholder_text="ADDRESS:",corner_radius=10)
                address_entry.grid(row=9,column=1)
        #==========postcode====================
                lbl_cust_pin=Label(lblframe, text="--Pin Code--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_pin.grid(row=3, column=0)

                pin_entry = CTkEntry(master=lblframe,textvariable=self.pin, width=250, placeholder_text="Pin:",corner_radius=10)
                pin_entry.grid(row=3,column=1)   
        #========Nationality===============================
                lbl_cust_nation=Label(lblframe, text="--Customer Country--", font=("times new roman",12, "bold"), padx=2, pady=6)
                lbl_cust_nation.grid(row=6, column=0)

                nation_entry = CTkComboBox(master=lblframe, values=['Indian','Non-Indian'],fg_color='lavender',border_color='navy')
                nation_entry.grid(row=6,column=1) 
                self.nation=nation_entry
                
        #***********************btnupdate===================
                btn_tkframe=CTkFrame(master=lblframe,border_width=2,border_color='black',width=412,height=40)
                btn_tkframe.place(x=2,y=400)

                btn_add=CTkButton(master=btn_tkframe,command=self.add_data,text='ADD',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_add.grid(row=0,column=0)

                btn_UPDATE=CTkButton(master=btn_tkframe,command=self.update_cust,text='UPDATE',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_UPDATE.grid(row=0,column=1)

                btn_DELETE=CTkButton(master=btn_tkframe,command=self.mDelete,text='DELETE',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_DELETE.grid(row=0,column=2)

                btn_RESET=CTkButton(master=btn_tkframe,command=self.reset,text='RESET',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_RESET.grid(row=0,column=3)

        #=============Tktable frame 2nd part==================================
                Table_Frame=LabelFrame(self.root, bd=2,text="View Deatils And Search",font=("Times New Roman",15,"bold",'italic'), padx=2)
                Table_Frame.place(x=435, y=55,width=850, height=490)
        #===============srch by===============================================
                lbl_srch=Label(Table_Frame, text="--SEARCH BY--", font=("times new roman",12, "bold"),bg="goldenrod1")
                lbl_srch.grid(row=0, column=0)

                self.srchv=StringVar()
                srch_combobox = CTkComboBox(master=Table_Frame, values=['MOBILE NO.',"NAME"],fg_color='khaki',border_color='DeepSkyBlue2')
                srch_combobox.grid(row=0,column=1,padx=3)
                self.srchv=srch_combobox

                self.txt=StringVar()
                srch_entry = CTkEntry(master=Table_Frame,textvariable=self.txt,width=250, placeholder_text="",corner_radius=10)
                srch_entry.grid(row=0,column=2,padx=2)
                

                btn_SEARCH=CTkButton(master=Table_Frame,command=self.srch,text='SEARCH',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_SEARCH.grid(row=0,column=3)

                btn_SHOW=CTkButton(master=Table_Frame,command=self.fetch_data,text='SHOW ALL',font=('Georgia',12),fg_color='black',hover_color='cyan',text_color='gold',corner_radius=32,width=100)
                btn_SHOW.grid(row=0,column=4,padx=1)

        #====================table data=====================
                details_table=Frame(Table_Frame, bd=2)
                details_table.place(x=0, y=50, width=840,height=350)

                scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)



                self.det_table=ttk.Treeview(details_table,columns=('c1','c2','c3','c4','c5','c6','c7','c8','c9','c10'),
                                        show='headings',xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)      
                scroll_x.config(command=self.det_table.xview)
                scroll_y.config(command=self.det_table.yview)




                self.det_table.heading('c1',text='REFER NO')
                self.det_table.heading('c2',text='NAME')
                self.det_table.heading('c3',text='GENDER')
                self.det_table.heading('c4',text='MOBILE NO.')
                self.det_table.heading('c5',text='EMAIL ID.')
                self.det_table.heading('c6',text='ID PROOF')
                self.det_table.heading('c7',text='ID NUM')
                self.det_table.heading('c8',text='ADDRESS')
                self.det_table.heading('c9',text='PINCODE')
                self.det_table.heading('c10',text='NATIONALITY')


                self.det_table.column("c1", width=130)
                self.det_table.column("c2", width=130)
                self.det_table.column("c3", width=130)
                self.det_table.column("c4", width=130)
                self.det_table.column("c5", width=130)
                self.det_table.column("c6", width=130)
                self.det_table.column("c7", width=130)
                self.det_table.column("c8", width=130)
                self.det_table.column("c9", width=130)
                self.det_table.column("c10", width=130)

                self.det_table.pack(fill=BOTH,expand=1)
                
                self.fetch_data()

        #made det_table an instance variable by putting self before===========================

                self.det_table.bind("<ButtonRelease-1>",self.get_cursor)
        #================for showing error if user hasnt inputed the info=================================
        def add_data(self):
                if self.mb_no.get()=="" or self.name.get()=="":
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
                                cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                self.ref.get(),
                                                                                self.name.get(),
                                                                                self.gen.get(),
                                                                                self.mb_no.get(),
                                                                                self.emid.get(),
                                                                                self.idproof.get(),
                                                                                self.idnum.get(),
                                                                                self.addrs.get(),
                                                                                self.pin.get(),
                                                                                self.nation.get()
                                                                                
                                                                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo('Success','Customer Has Been Added Successfully',parent=self.root)
                        except Exception as es:
                                messagebox.showwarning('Warning',f'Something Went Wrong:{str(es)}',parent=self.root)
        #=========this way we can get data from mysql===========================================
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from customer")
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
        def get_cursor(self,event=''):
                        cursor_row=self.det_table.focus() #seletcting the row
                        content=self.det_table.item(cursor_row)#getting the data in row which i seletcted                       
                        row=content["values"]#opening the vlues and storing in  row var
                        self.ref.set(row[0]), #setting the data of row 0 to ref.
                        self.name.set(row[1]), 
                        self.gen.set(row[2]),
                        self.mb_no.set(row[3]),
                        self.emid.set(row[4]),
                        self.idproof.set(row[5]),
                        self.idnum.set(row[6]),
                        self.addrs.set(row[7])
                        self.pin.set(row[8]), 
                        self.nation.set(row[9])
        def update_cust(self):
                if self.mb_no.get()=="":
                        messagebox.showerror('ERROR','Please Enter Mobile Number',parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                        my_cursor=conn.cursor()#this line creates a cursor object. The cursor is used to execute SQL commands.
                        my_cursor.execute('update customer set `NAME`=%s, `GENDER`=%s, `MOBILE NO.`=%s, `EMAIL ID.`=%s, `ID PROOF`=%s, `ID NUM`=%s, `ADDRESS`=%s, `PINCODE`=%s, `NATIONALITY`=%s where `Ref`=%s',(
                                                                        
                        
                                                                        
                                                                        self.name.get(),
                                                                        self.gen.get(),
                                                                        self.mb_no.get(),
                                                                        self.emid.get(),
                                                                        self.idproof.get(),
                                                                        self.idnum.get(),
                                                                        self.addrs.get(),
                                                                        self.pin.get(),
                                                                        self.nation.get(),
                                                                        self.ref.get()                                       
                                                                                                                ))
                                #"""BACKTICK(`)was added so tht the spaces or any special char can be ignored"""       
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('UPDATE','Customer Details Has Been Updated',parent=self.root)

                '''%s is used as a placeholder for the values you want to update in the database. When the execute method is called, 
                each %s in the SQL command is replaced by the corresponding value in the tuple that follows it. For example,
 the first %s is replaced by the value of self.name.get(), the second %s is replaced by the value of self.gen.get(), and so on.'''

                
        def mDelete(self):
                delete=messagebox.askyesno('HOTEL RIMBERIO','DO YOU WANT TO DELETE THIS CUSTOMER DETAILS?',parent=self.root)           
                if delete==True:
                        conn=mysql.connector.connect(host="localhost",username="root", password="ishan@120806",database="hote_managementl")
                        my_cursor=conn.cursor()
                        my_cursor.execute("delete from customer where Ref=%s",(self.ref.get(),))
                        conn.commit()
                        self.fetch_data()#to display updated data
                        conn.close()      

                else:
                                return

        def reset(self):
                
                self.name.set(""), 
                
                self.mb_no.set(""),
                self.emid.set(""),
                
                self.idnum.set(""),
                self.addrs.set("")
                self.pin.set(""),
                
                x=random.randint(10000,100000)
                self.ref.set(str(x))

        def srch(self):
                conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='ishan@120806',
                        database='hote_managementl'
                                        )
                cursor = conn.cursor()


                '''In the line query = "SELECT * FROM customer WHERE {} LIKE %s".format(self.srchv.get()), 
                the {} is a placeholder that gets replaced with the value of self.srchv.get(), which is the column name you want to search in.

The %s in the query is a placeholder for the search term. 
However, because youre using a LIKE clause in your SQL query, you need to include % symbols around the search term (for example, %search_term%). 
This is done in the execute method: cursor.execute(query, ('%' + self.txt.get() + '%',)).

This way, the SQL query becomes something like SELECT * FROM customer WHERE column_name LIKE '%search_term%', 
which selects all rows from the customer table where column_name contains search_term.'''



                query = "SELECT * FROM customer WHERE `{}` LIKE %s".format(self.srchv.get())
                cursor.execute(query, ('%' + self.txt.get() + '%',))
                rows = cursor.fetchall()
                
                if len(rows) != 0:
                        messagebox.showinfo('FOUND','Person Found',parent=self.root)
                        self.det_table.delete(*self.det_table.get_children())#if row isnt empty i.e a match is found , it deletes all the existing rows and then
                        for i in rows:#for loop adds the row with the matching data at the end of table
                                self.det_table.insert("", END, values=i)

                else:
                        messagebox.showerror('Error', 'Person not found')               
                        conn.commit()#saves the data to database
                conn.close()





              
              



    







if __name__ == "__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
    