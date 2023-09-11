import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

# Create a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library_mgmt"
)

# Create a cursor object
cursor = db.cursor()

# Function to check user credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Execute a query to fetch user from the database
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username)
        window.destroy()

        # Execute another Python script here (replace 'script.py' with your script's name)

        import subprocess
        subprocess.Popen(["python", "Library-Management-Dashboard.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the tkinter window
window = tk.Tk()
window.title("Library Management Console")

# Load and display the background image
background_image = Image.open("library_background.png")  # Replace with the path to your background image
background_photo = ImageTk.PhotoImage(background_image)

# Get the image dimensions and set the window size accordingly
window_width, window_height = background_image.size
window.geometry(f"{window_width}x{window_height}")

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

# Create a frame for the login elements and center it on the window
login_frame = tk.Frame(window, bg="white")
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create labels, entry fields, and buttons inside the login frame
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="white")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(login_frame, font=("Arial", 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="white")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(login_frame, text="Login", command=login, font=("Arial", 14))
login_button.grid(row=2, columnspan=2, pady=20)

# Start the tkinter main loop
window.mainloop()

# Close the MySQL connection when the application exits
db.close()
