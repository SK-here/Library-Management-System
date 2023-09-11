'''
@Tittle: Library Management System
@Description: This project is submitted for the partial fulfillment of Python Trainning By Blendvidya
@Project Supervisior: Sindhu Nair Mam
@Author: Saksham Trivedi
@Email: trivedisaksham@gmail.com
@Contact: +918602145587
'''

from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


# Main class 
class LibraryManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        # ++++++++++++++++++++++++++++++++++++++++++++++++++++ Database Variable ++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()

        # ========================================  Console Frame ============================================
        lbltitle=Label(self.root, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0,y=130, width=1530, height=400)

        # ========================================== DataFrame Left ==========================================

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="black", bd=12, relief=RIDGE, font=("times new roman", 14, "bold"))
        DataFrameLeft.place( x = 0, y = 5, width =900, height = 350)

        # Member Type 
        lblMember = Label (DataFrameLeft, bg = "powder blue" ,text = "Member Type", font = ("times new roman", 14, "bold"), padx = 2, pady = 6)
        lblMember.grid (row = 0, column = 0, sticky = W)

        comMember = ttk.Combobox(DataFrameLeft, font = ("times new roman", 14, "bold"), width = 27, state = "readonly", textvariable=self.member_var)
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid (row = 0, column = 1)

        # PRN Number Entry
        lblref = Label (DataFrameLeft, bg = "powder blue", text = "PRN No:", font = ("arial", 12, "bold"), padx = 2)
        lblref.grid (row = 1, column = 0, sticky = W)
        txtref = Entry (DataFrameLeft,font = ("arial", 12, "bold"), width = 29, textvariable=self.prn_var)
        txtref.grid (row = 1, column = 1)

        # Title
        lblTitle = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "ID no.", padx = 2, pady = 6, bg = "powder blue")
        lblTitle.grid (row = 2, column = 0, sticky = W)
        txtTitle = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.id_var)
        txtTitle.grid (row = 2, column = 1)

        # First Name
        lblFirstName = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "First Name:", padx = 2, pady = 6, bg = "powder blue")
        lblFirstName.grid (row = 3, column = 0, sticky = W)
        txtFirstName = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.firstname_var)
        txtFirstName.grid (row = 3, column = 1)

        # Last Name
        lblLastName = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Last Name", padx = 2, pady = 6, bg = "powder blue")
        lblLastName.grid (row = 4, column = 0, sticky = W)
        txtLastName = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.lastname_var)
        txtLastName.grid (row = 4, column = 1)

        # Address Line 1
        lblAddress1 = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Address-1:", padx = 2, pady = 6, bg = "powder blue")
        lblAddress1.grid (row = 5, column = 0, sticky = W)
        txtAddress1 = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.address1_var)
        txtAddress1.grid (row = 5, column = 1)

        # Address Line 2
        lblAddress2 = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Address-2:", padx = 2, pady = 6, bg = "powder blue")
        lblAddress2.grid (row = 6, column = 0, sticky = W)
        txtAddress2 = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.address2_var)
        txtAddress2.grid (row = 6, column = 1)

        # Postal Code
        lblPostCode = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Post Code:", padx = 2, pady = 6, bg = "powder blue")
        lblPostCode.grid (row = 7, column = 0, sticky = W)
        txtPostCode = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.postcode_var)
        txtPostCode.grid (row = 7, column = 1)

        # Mobile Number
        lblMobile = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Contact", padx = 2, pady = 6, bg = "powder blue")
        lblMobile.grid (row = 8, column = 0, sticky = W)
        txtMobile = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.mobile_var)
        txtMobile.grid (row = 8, column = 1)

        # Book Id
        lblBookId = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Book ID:", padx = 2, pady = 6, bg = "powder blue")
        lblBookId.grid (row = 0, column = 2, sticky = W)
        txtBookId = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.bookid_var)
        txtBookId.grid (row = 0, column = 3)

        # Book Title
        lblBookTitle = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Book Title:", padx = 2, pady = 6, bg = "powder blue")
        lblBookTitle.grid (row = 1, column = 2, sticky = W)
        txtBookTitle = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.booktitle_var)
        txtBookTitle.grid (row = 1, column = 3)

        # Author
        lblAuthor = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Author Name:", padx = 2, pady = 6, bg = "powder blue")
        lblAuthor.grid (row = 2, column = 2, sticky = W)
        txtAuthor = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.author_var)
        txtAuthor.grid (row = 2, column = 3)

        # Borrowed Date
        lblDateBorrowed = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Date Borrowed:", padx = 2, pady = 6, bg = "powder blue")
        lblDateBorrowed.grid (row = 3, column = 2, sticky = W)
        txtDateBorrowed = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid (row = 3, column = 3)

        # Due Date
        lblDateDue = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Due Date:", padx = 2, pady = 6, bg = "powder blue")
        lblDateDue.grid (row = 4, column = 2, sticky = W)
        txtDateDue = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.datedue_var)
        txtDateDue.grid (row = 4, column = 3)

        # Days On Book
        lblDaysOnBook = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Days On Book", padx = 2, pady = 6, bg = "powder blue")
        lblDaysOnBook.grid (row = 5, column = 2, sticky = W)
        txtDaysOnBook = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.daysonbook_var)
        txtDaysOnBook.grid (row = 5, column = 3)

        # late Retrun Fine
        lblLateReturnFine = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "ID no.", padx = 2, pady = 6, bg = "powder blue")
        lblLateReturnFine.grid (row = 6, column = 2, sticky = W)
        txtLateReturnFine = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.lateratefine_var)
        txtLateReturnFine.grid (row = 6, column = 3)

        # Date Over Due
        lblDateOverDate = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Date Over Due", padx = 2, pady = 6, bg = "powder blue")
        lblDateOverDate.grid (row = 7, column = 2, sticky = W)
        txtDateOverDate = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.dateoverdue_var)
        txtDateOverDate.grid (row = 7, column = 3)

        # Actual Price
        lblActualPrice = Label (DataFrameLeft, font = ("arial", 12, "bold"), text = "Actual Price", padx = 2, pady = 6, bg = "powder blue")
        lblActualPrice.grid (row = 8, column = 2, sticky = W)
        txtActualPrice = Entry (DataFrameLeft, font = ("arial", 12, "bold"), width = 29, textvariable=self.finalprice_var)
        txtActualPrice.grid (row = 8, column = 3)

        # ========================================== DataFrame Right ==========================================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="black", bd=12, relief=RIDGE, font=("times new roman", 14, "bold"))
        DataFrameRight.place( x = 910, y = 5, width = 540, height = 350)

        self.txtBox = Text (DataFrameRight, font = ("arial", 12, "bold"), width = 32, height = 16, padx = 2, pady = 6)
        self.txtBox.grid (row = 0, column = 2)

        listScrollbar = Scrollbar (DataFrameRight)
        listScrollbar.grid (row  = 0, column = 1, sticky = "ns")

# ++++++++++++++++++++++++++++++++++++++++++ Sample Book Information ++++++++++++++++++++++++++++++++++++++++++++
        listBooks = [
            'Learn Python The Hard Way',
            'Python Programming', 
            'Python Cookbook',
            'Introduction to ML',
            'Computer Architecture',
            'Computer Networks',
            'Computer Organization & Architecture',
            'Scramblind Data With python',
            'Computer Science Distilled',
            'The Art Of Deception',
            'Ghost Inside the Wire',
            'Thirty Days to Kill',
            'Interview Questions with Python',
            'Subtle Art of not giving Sh!t',
            'Ikigai',
            'Work In Progress',
            'Atomic Habits' 
        ]

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()[0]))
            Book = value


            # Time Duration
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2

            if Book == 'Learn Python The Hard Way':
                
                # Book Attributes
                BookId = 'BKID545478'
                BookTitle = Book
                BookAuthor = "Paul McGreary"
                BookPrice = "RS. 780.00"
                # Setting Book Attributes
                self.bookid_var.set(BookId)
                self.booktitle_var.set(BookTitle)
                self.author_var.set(BookAuthor)
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set(BookPrice)
            
            elif Book == 'Python Programming':
                # Book Attributes
                BookId = 'BKID4234432'
                BookTitle = Book
                BookAuthor = "Python.org"
                BookPrice = "RS. 345.00"
                self.bookid_var.set(BookId)
                self.booktitle_var.set(BookTitle)
                self.author_var.set(BookAuthor)
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set(BookPrice)
                
            elif Book == 'Python Cookbook':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book
                    BookAuthor = "O'rielly"
                    BookPrice = "RS. 448.00"
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Introduction to ML':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book
                    BookAuthor = "MS KelKar"
                    BookPrice = "RS. 450.00"
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Computer Architecture':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book
                    BookAuthor = "Leonard Whiteman"
                    BookPrice = "RS. 545.00"
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Computer Networks':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book
                    BookAuthor = "Behrauz Forhujan"
                    BookPrice = "RS. 870.00"
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Computer Organization & Architecture':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Wisely Media'
                    BookPrice = 'RS. 1010.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Scramblind Data With python':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Tessa Thopson'
                    BookPrice = 'RS. 660.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Computer Science Distilled':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'No Starch Press'
                    BookPrice = 'RS. 1080.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'The Art Of Deception':
                # Book Attributes
                BookId = 'BKID545478'
                BookTitle = Book 
                BookAuthor = 'Kevin Mitnick'
                BookPrice = 'RS. 880.00'
                
                self.bookid_var.set(BookId)
                self.booktitle_var.set(BookTitle)
                self.author_var.set(BookAuthor)
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set(BookPrice)
            
            elif Book == 'Ghost Inside the Wire':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Kevin Mitnick'
                    BookPrice = 'RS. 550.00'

                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Thirty Days to Kill':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Prakash Publications'
                    BookPrice = 'RS. 220.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Interview Questions with Python':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'No Starch Press'
                    BookPrice = 'RS. 1400.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Subtle Art of not giving Sh!t':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Ankur Wariko'
                    BookPrice = 'RS. 300.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Ikigai':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Thomas Edison, Tsung Hstan'
                    BookPrice = 'RS. 200.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Work In Progress':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Ankur Wariko'
                    BookPrice = 'RS. 340.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

            elif Book == 'Atomic Habits':
                    # Book Attributes
                    BookId = 'BKID545478'
                    BookTitle = Book 
                    BookAuthor = 'Nicholas Jane'
                    BookPrice = 'RS. 580.00'
                    
                    self.bookid_var.set(BookId)
                    self.booktitle_var.set(BookTitle)
                    self.author_var.set(BookAuthor)
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("RS. 50")
                    self.dateoverdue_var.set("NO")
                    self.finalprice_var.set(BookPrice)

        # List Box
        listBox = Listbox (DataFrameRight,  font = ("arial", 12, "bold"), width = 20, height = 16 )
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid (row  = 0, column = 0, padx = 4)
        listScrollbar.config(command=listBox.yview)

        for book in listBooks:
            listBox.insert(END, book)

        # ========================================  Buttons Frame ============================================

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x = 0, y = 530, width = 1530, height = 70)

        # Add Data
        btnAddData = Button (Framebutton, text = "Add Data", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white", command=self.add_data)
        btnAddData.grid (row = 0, column = 0)

        # Show Data
        btnShowData = Button (Framebutton, text = "Show Data", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white", command=self.show_Data)
        btnShowData.grid (row = 0, column = 1)

        # Update
        btnUpdate = Button (Framebutton, text = "Update", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white", command=self.update_data)
        btnUpdate.grid (row = 0, column = 2)

        # Delete
        btnDelete = Button (Framebutton, text = "Delete", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white", command=self.delete_data)
        btnDelete.grid (row = 0, column = 3)

        # Reset
        btnReset = Button (Framebutton, text = "Reset", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white", command=self.reset)
        btnReset.grid (row = 0, column = 4)

        # Exit
        btnExit = Button (Framebutton, text = "Exit", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white", command=self.iExit)
        btnExit.grid (row = 0, column = 5)

        # ========================================  Information Frame ============================================

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x = 0, y = 600, width = 1530, height = 195)

        Table_frame = Frame(FrameDetails, bd = 6, relief = RIDGE, bg = "powder blue")
        Table_frame.place (x = 0, y = 2, width = 1460, height = 190)

        # ScrollBar
        xscroll = ttk.Scrollbar (Table_frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar (Table_frame, orient = VERTICAL)

        # Horizental View
        self.library_table = ttk.Treeview (Table_frame, column = (
                                                        "membertype", "prnno", "title", "firstname", "lastname", "address1",
                                                        "address2", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed",
                                                        "datedue", "days", "lateretrunfine", "dateoverdue", "finalprice"),
                                                        xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

        # Horizental Scroll Bar
        xscroll.pack(side = BOTTOM, fill = X)
        yscroll.pack(side = RIGHT, fill = Y)

        # Vertical Scroll Bar
        xscroll.config (command = self.library_table.xview)
        yscroll.config (command = self.library_table.yview)

        # Horizontal Options
        self.library_table.heading("membertype", text = "Member Type")
        self.library_table.heading("prnno", text = "PRN No.")
        self.library_table.heading("title", text = "Title")
        self.library_table.heading("firstname", text = "First Name")
        self.library_table.heading("lastname", text = "Last Name")
        self.library_table.heading("address1", text = "Address1")
        self.library_table.heading("address2", text = "Address2")
        self.library_table.heading("postid", text = "Post ID")
        self.library_table.heading("mobile", text = "Mobile Number")
        self.library_table.heading("bookid", text = "Book ID")
        self.library_table.heading("booktitle", text = "Book Tittle")
        self.library_table.heading("author", text = "Author")
        self.library_table.heading("dateborrowed", text = "Date  Borrowed")
        self.library_table.heading("datedue", text = "Date Due")
        self.library_table.heading("days", text = "DaysOnBook")
        self.library_table.heading("lateretrunfine", text = "Later Return Fine")
        self.library_table.heading("dateoverdue", text = "DateOverDue")
        self.library_table.heading("finalprice", text = "Final Price")

        # Displaying Column
        self.library_table ["show"] = "headings"
        self.library_table.pack (fill = BOTH, expand = 1)

        # Setting Column Width
        self.library_table.column ("membertype", width = 100)
        self.library_table.column ("prnno", width = 100)
        self.library_table.column ("title", width = 100)
        self.library_table.column ("firstname", width = 100)
        self.library_table.column ("lastname", width = 100)
        self.library_table.column ("address1", width = 100)
        self.library_table.column ("address2", width = 100)
        self.library_table.column ("postid", width = 100)
        self.library_table.column ("mobile", width = 100)
        self.library_table.column ("bookid", width = 100)
        self.library_table.column ("booktitle", width = 100)
        self.library_table.column ("author", width = 100)
        self.library_table.column ("dateborrowed", width = 100)
        self.library_table.column ("datedue", width = 100)
        self.library_table.column ("days", width = 100)
        self.library_table.column ("lateretrunfine", width = 100)
        self.library_table.column ("dateoverdue", width = 100)
        self.library_table.column ("finalprice", width = 100)

        # Fetching Information
        self.fetch_data()

        self.library_table.bind("<ButtonRelease - 1>", self.get_cursor)


    # Adding Data to DataBase
    def add_data(self):

        conn = mysql.connector.connect(host = "localhost", username = "root", password = "root", database = "library_mgmt")
        my_cursor = conn.cursor()
         
        sql_query = "INSERT INTO library_management (Member, PRN_No, ID, FirstName, LastName, Address1, Address2, PostId, Mobile, BookId, Author, Dateborrowed, datedue, daysofbook, lateretrunfine, dateoverdue, finalprice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
                    self.member_var.get(),          # 1
                    self.prn_var.get(),             # 2
                    self.id_var.get(),              # 3        
                    self.firstname_var.get(),       # 4     
                    self.lastname_var.get(),        # 5  
                    self.address1_var.get(),        # 6
                    self.address2_var.get(),        # 7
                    self.postcode_var.get(),        # 8
                    self.mobile_var.get(),          # 9
                    self.bookid_var.get(),          # 10
                    self.author_var.get(),          # 11
                    self.dateborrowed_var.get(),    # 12
                    self.datedue_var.get(),         # 13
                    self.daysonbook_var.get(),      # 14
                    self.lateratefine_var.get(),    # 15
                    self.dateoverdue_var.get(),     # 16
                    self.finalprice_var.get()       # 17
                )
        my_cursor.execute(sql_query, values)        
        conn.commit()
        self.fetch_data()
        conn.close()

        # Adding prompt
        messagebox.showinfo ("Sucess", "Member Has Been Inserted Sucessfully")

    # Reading Data From Database
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "root", database = "library_mgmt")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from library_management")
        rows = my_cursor.fetchall()

        if len (rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Update The Data
    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="library_mgmt")
        my_cursor = conn.cursor()

        # Assuming you have a unique identifier, e.g., an ID, to identify the record to update
        unique_id = self.id_var.get()

        sql_query = "UPDATE library_management SET Member = %s, PRN_No = %s, FirstName = %s, LastName = %s, Address1 = %s, Address2 = %s, PostId = %s, Mobile = %s, BookId = %s, Author = %s, Dateborrowed = %s, datedue = %s, daysofbook = %s, lateretrunfine = %s, dateoverdue = %s, finalprice = %s WHERE ID = %s"
        values = (
            self.member_var.get(),
            self.prn_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            unique_id  # The unique identifier to identify the record to update
        )

        my_cursor.execute(sql_query, values)
        conn.commit()
        self.fetch_data()
        conn.close()
        # Adding prompt
        messagebox.showinfo ("Sucess", "Member Has Been Updated Sucessfully")

    # Deleting the Data from Database
    def delete_data(self):
        if self.id_var.get() == "" or self.prn_var.get() == "":
            messagebox.showerror("Error", "First Select The Member")
        
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="library_mgmt")
            my_cursor = conn.cursor()

            # Assuming you have a unique identifier, e.g., an ID, to identify the record to delete
            unique_id = self.id_var.get()

            sql_query = "DELETE FROM library_management WHERE ID = %s"
            values = (unique_id,)  # Note the comma to create a single-element tuple

            my_cursor.execute(sql_query, values)
            conn.commit()
            self.fetch_data()
            conn.close()

    # Fill Data
    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content ['values']
        
        self.member_var.set(row[0]),          # 1
        self.prn_var.set(row[1]),             # 2
        self.id_var.set(row[2]),              # 3        
        self.firstname_var.set(row[3]),       # 4     
        self.lastname_var.set(row[4]),        # 5  
        self.address1_var.set(row[5]),        # 6
        self.address2_var.set(row[6]),        # 7
        self.postcode_var.set(row[7]),        # 8
        self.mobile_var.set(row[8]),          # 9
        self.bookid_var.set(row[9]),          # 10
        self.author_var.set(row[10]),         # 11
        self.dateborrowed_var.set(row[11]),   # 12
        self.datedue_var.set(row[12]),        # 13
        self.daysonbook_var.set(row[13]),     # 14
        self.lateratefine_var.set(row[14]),   # 15
        self.dateoverdue_var.set(row[15]),    # 16
        self.finalprice_var.set(row[16])      # 17
          
    # Show Data
    def show_Data(self):
        self.txtBox.insert(END, "Member Type \t\t"   + self.member_var.get()       + "\n")
        self.txtBox.insert(END, "PRN No: \t\t"       + self.prn_var.get()          + "\n")
        self.txtBox.insert(END, "First Name \t\t"    + self.firstname_var.get()    + "\n")
        self.txtBox.insert(END, "Last Name \t\t"     + self.lastname_var.get()     + "\n")
        self.txtBox.insert(END, "Address1 \t\t"      + self.address1_var.get()     + "\n")
        self.txtBox.insert(END, "Address2 \t\t"      + self.address2_var.get()     + "\n")
        self.txtBox.insert(END, "Post Code \t\t"     + self.postcode_var.get()     + "\n")
        self.txtBox.insert(END, "Mobile No \t\t"     + self.mobile_var.get()       + "\n")
        self.txtBox.insert(END, "Book ID \t\t"       + self.bookid_var.get()       + "\n")
        self.txtBox.insert(END, "Book Title \t\t"    + self.booktitle_var.get()    + "\n")
        self.txtBox.insert(END, "Author \t\t"        + self.author_var.get()       + "\n")
        self.txtBox.insert(END, "Date Borrowed \t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Due Date \t\t"      + self.datedue_var.get()      + "\n")
        self.txtBox.insert(END, "Days On Book \t\t"  + self.daysonbook_var.get()   + "\n")
        self.txtBox.insert(END, "LateRateFine \t\t"  + self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverdDue \t\t"  + self.dateoverdue_var.get()  + "\n")
        self.txtBox.insert(END, "Final Price \t\t"   + self.finalprice_var.get()   + "\n")
        
    # Reset
    def reset(self):
        self.member_var.set("")       
        self.prn_var.set("")          
        self.firstname_var.set("")    
        self.lastname_var.set("")     
        self.address1_var.set("")     
        self.address2_var.set("")     
        self.postcode_var.set("")     
        self.mobile_var.set("")       
        self.bookid_var.set("")       
        self.booktitle_var.set("")    
        self.author_var.set("")       
        self.dateborrowed_var.set("") 
        self.datedue_var.set("")      
        self.daysonbook_var.set("")   
        self.lateratefine_var.set("") 
        self.dateoverdue_var.set("")  
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)

    # Exit
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to Exit?")
        if iExit > 0:
            self.root.destroy()
            return

# Running The DashBoard
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
