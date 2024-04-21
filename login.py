from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
from hotel import HotelManagementSystem


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\Ojas\Pics\loginhotel.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"D:\Ojas\Pics\usericonlogo.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=135,y=100)

        # label
        lblusername=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        lblusername.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        lblpassword = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lblpassword.place(x=70, y=223)

        self.txtpass = ttk.Entry(frame, show="*", font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # ============Icon Images===============
        img2 = Image.open(r"D:\Ojas\Pics\usericon.jpg")
        img2 = img2.resize((25,25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"D:\Ojas\Pics\lock.jpg")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=393, width=25, height=25)

        # Loginbutton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # registerbutton
        registerbtn = Button(frame, text="New User? Register Here",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="red")
        registerbtn.place(x=16, y=350, width=160)

        # forgetpassbtn
        registerbtn = Button(frame, text="Forgot Password",command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        registerbtn.place(x=-9, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="ojasrkale" and self.txtpass.get()=="8654":
            messagebox.showinfo("Success","Welcome")
        else:
            conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="",database="hotelmanagement")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                     self.txtuser.get(),
                                                                                     self.txtpass.get()
                                                                                     ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Yes or No","Access only admin?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ==================reset password=======================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="",database="hotelmanagement")
            my_cursor=conn.cursor()
            qery=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qery,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()


    # ================forgot password window=================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="",database="hotelmanagement")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                fgtpswd=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                fgtpswd.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"),bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name","Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15,"bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password= Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, show="*",font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===========variables===================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        # ===========bg image========================
        self.bg=ImageTk.PhotoImage(file=r"D:\Ojas\Pics\hotelregister.jpg" )

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ==============left image=======================
        self.bg1 = ImageTk.PhotoImage(file=r"D:\Ojas\Pics\HotelLogo.png")
        left_lbl = Label(self.root,bg="white", image=self.bg1)
        left_lbl.place(x=180, y=100, width=360, height=550)

        # ===============main frame=======================

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="lightblue",fg="blue")
        register_lbl.place(x=20,y=20)

        # =================label and entry==================
        # ===========row1==================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame, text="Last Name",font=("times new roman", 15, "bold"), bg="white",fg="black")
        lname.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # =============row2==================
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white",fg="black")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # =================row3==================
        security_Q= Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=["Select","Your Birth Place","Your Girlfriend Name","Your Pet Name"]
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA, font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # ==================row4==================
        pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ===============checkbutton=================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check, text="I Agree the Terms & Conditions", font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        # ==================buttons==================
        img = Image.open(r"D:\Ojas\Pics\regbtn.png")
        img = img.resize((200, 55), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage, command=self.register_data, borderwidth=0,cursor="hand2", font=("times new roman",15,"bold"),fg="white")
        b1.place(x=30, y=418, width=200)

        img1 = Image.open(r"D:\Ojas\Pics\loginbtn.jpg")
        img1 = img1.resize((200, 55), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"),fg="white")
        b2.place(x=350, y=420, width=200)

        # ============function declaration================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="", database="hotelmanagement")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_SecurityA.get(),
                                                                                         self.var_pass.get()

                                                                                       ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()





if __name__== "__main__":
   main()
