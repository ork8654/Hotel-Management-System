from tkinter import *


class HotelmanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")

        # ***************1st img*******8

        # ************logo*************

        # **************title*********
        lbl_title = Label(self.root, text="HOTEl MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # **************main Frame*******
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=198, width=1550, height=620)

        # **************menu********
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # *************bton frame*************
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", width=22, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0)

        if __name__ == "__main__":
        root = Tk()
        obj = HotelmanagementSystem(root)
        root.mainloop()