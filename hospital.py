import tkinter as tk
from tkinter import messagebox
import sqlite3
# Create the database and table
def create_database():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        disease TEXT)''')
    conn.commit()
    conn.close()
# Add patient function
def add_patient():
    name = name_entry.get()
    age = age_entry.get()
    disease = disease_entry.get()
    # Check if all fields are filled
    if not name or not age or not disease:
        messagebox.showerror("Input Error", "Please fill in all fields")
        return
    
    # Insert patient data into the database
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO patients (name, age, disease) 
                      VALUES (?, ?, ?)''', (name, age, disease))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient added successfully!")
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    disease_entry.delete(0, tk.END)
# View all patients
def view_patients():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    rows = cursor.fetchall()
    conn.close()
    # Display patient records
    records_text.delete(1.0, tk.END)  # Clear previous records
    for row in rows:
        records_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Disease: {row[3]}\n")
# Main GUI window
root = tk.Tk()
root.title("Hospital Management System")
# Create the database when starting the program
create_database()
# Labels and entry fields
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)
tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)
tk.Label(root, text="Disease:").pack(pady=5)
disease_entry = tk.Entry(root)
disease_entry.pack(pady=5)
# Buttons for adding and viewing patients
add_button = tk.Button(root, text="Add Patient", command=add_patient)
add_button.pack(pady=10)
view_button = tk.Button(root, text="View Patients", command=view_patients)
view_button.pack(pady=10)
# Text box to display patient records
records_text = tk.Text(root, height=10, width=50)
records_text.pack(pady=10)
# Start the Tkinter main loop
root.mainloop()
