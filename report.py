from tkinter import*
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import mysql.connector


class report:

    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variables
        self.var_ref = StringVar()
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_floor = StringVar()
        self.var_RoomNo = StringVar()
        self.var_RoomType = StringVar()

        # ================title===================
        lbl_title = Label(self.root, text="REPORT", font=("times new roman", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ================logo==============
        img2 = Image.open(r"D:\Ojas\Pics\logohotel.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # =============Show Cust Report==================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Customer Report", font=("arial", 12, "bold"))
        Table_Frame.place(x=50, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.Cust_Report_Table = ttk.Treeview(Table_Frame, column=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address","contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays","floor"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Report_Table.xview)
        scroll_y.config(command=self.Cust_Report_Table.yview)

        self.Cust_Report_Table.heading("ref", text="Refer No")
        self.Cust_Report_Table.heading("name", text="Name")
        self.Cust_Report_Table.heading("mother", text="Mother")
        self.Cust_Report_Table.heading("gender", text="Gender")
        self.Cust_Report_Table.heading("post", text="Post")
        self.Cust_Report_Table.heading("mobile", text="Mobile")
        self.Cust_Report_Table.heading("email", text="Email")
        self.Cust_Report_Table.heading("nationality", text="Nationality")
        self.Cust_Report_Table.heading("idproof", text="Id Proof")
        self.Cust_Report_Table.heading("idnumber", text="Id Number")
        self.Cust_Report_Table.heading("address", text="Address")
        self.Cust_Report_Table.heading("contact", text="Contact")
        self.Cust_Report_Table.heading("checkin", text="Check-in")
        self.Cust_Report_Table.heading("checkout", text="Check-Out")
        self.Cust_Report_Table.heading("roomtype", text="Room Type")
        self.Cust_Report_Table.heading("roomavailable", text="Room No")
        self.Cust_Report_Table.heading("meal", text="Meal")
        self.Cust_Report_Table.heading("noOfdays", text="NoOfDays")
        self.Cust_Report_Table.heading("floor", text="Floor")


        self.Cust_Report_Table["show"] = "headings"

        self.Cust_Report_Table.column("ref", width=100)
        self.Cust_Report_Table.column("name", width=100)
        self.Cust_Report_Table.column("mother", width=100)
        self.Cust_Report_Table.column("gender", width=100)
        self.Cust_Report_Table.column("post", width=100)
        self.Cust_Report_Table.column("mobile", width=100)
        self.Cust_Report_Table.column("email", width=100)
        self.Cust_Report_Table.column("nationality", width=100)
        self.Cust_Report_Table.column("idproof", width=100)
        self.Cust_Report_Table.column("idnumber", width=100)
        self.Cust_Report_Table.column("address", width=100)
        self.Cust_Report_Table.column("contact", width=100)
        self.Cust_Report_Table.column("checkin", width=100)
        self.Cust_Report_Table.column("checkout", width=100)
        self.Cust_Report_Table.column("roomtype", width=100)
        self.Cust_Report_Table.column("roomavailable", width=100)
        self.Cust_Report_Table.column("meal", width=100)
        self.Cust_Report_Table.column("noOfdays", width=100)
        self.Cust_Report_Table.column("floor", width=100)


        self.Cust_Report_Table.pack(fill=BOTH, expand=1)
        self.Cust_Report_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Report_Table.focus()
        content = self.Cust_Report_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),
        self.var_contact.set(row[11]),
        self.var_checkin.set(row[12]),
        self.var_checkout.set(row[13]),
        self.var_roomtype.set(row[14]),
        self.var_roomavailable.set(row[15]),
        self.var_meal.set(row[16]),
        self.var_noofdays.set(row[17]),
        self.var_floor.set(row[18])


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", port="3306", username="root", password="", database="hotelmanagement")
        my_cursor1 = conn.cursor()
        my_cursor1.execute("select * from customer RIGHT JOIN room ON customer.Mobile= room.Contact RIGHT JOIN details on room.room=details.RoomNo")
        rows1 = my_cursor1.fetchall()
        if len(rows1) != 0:
            self.Cust_Report_Table.delete(*self.Cust_Report_Table.get_children())
            for i1 in rows1:
                self.Cust_Report_Table.insert("", END, values=i1)
            conn.commit()
        conn.close()




if __name__=="__main__":
    root=Tk()
    obj=report(root)
    root.mainloop()
