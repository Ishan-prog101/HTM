from tkinter import*
from customtkinter import*



class report_win:
        def __init__(self,root):
                self.root=root
                self.root.title('DETAILS')
                self.root.geometry('1295x550+232+220') 

                lbl_titile=Label(self.root,text="STUDENT DETAILS",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile.place(x=0,y=0,width=1295,height=55)

                lbl_titile1=Label(self.root,text="NAMES:",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile1.place(x=50,y=100,width=200,height=55)
                
                lbl_titile2=Label(self.root,text="ISHAN UPADHYAY",font=('Bahnschrift Light Condensed',35,'bold'),bg='lightblue',fg='red',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile2.place(x=300,y=100,width=800,height=55)

                lbl_titile3=Label(self.root,text="CLASS:",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile3.place(x=100,y=170,width=500,height=55)

                lbl_titile4=Label(self.root,text="12 C",font=('Bahnschrift Light Condensed',35,'bold'),bg='lightblue',fg='red',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile4.place(x=700,y=170,width=500,height=55)


                lbl_titile4=Label(self.root,text="ROLL NUMBER:",font=('Bahnschrift Light Condensed',35,'bold'),bg='black',fg='gold',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile4.place(x=100,y=235,width=500,height=55)

                lbl_titile5=Label(self.root,text="13",font=('Bahnschrift Light Condensed',35,'bold'),bg='lightblue',fg='red',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile5.place(x=700,y=235,width=500,height=55)

                lbl_titile6=Label(self.root,text="THANK YOU",font=('Bahnschrift Light Condensed',50,'bold'),bg='pink',fg='navyblue',bd=4,highlightbackground='gold',highlightthickness=2)
                lbl_titile6.place(x=330,y=335,width=500,height=155)



if __name__ == "__main__":
    root=Tk()
    obj=report_win(root)
    root.mainloop()
