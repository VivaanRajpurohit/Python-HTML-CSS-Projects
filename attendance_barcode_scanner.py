import cv2
from pyzbar.pyzbar import decode
import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import threading
import time
import win32print
import win32ui


csv_file = "students.csv"

def load_attendance_data():
    if os.path.exists(csv_file):
        return pd.read_csv(csv_file)
    else:
        return pd.DataFrame(columns=['ID', 'Name', 'Status', 'Arrival Time'])


def mark_attendance(student_id, df):
    now = datetime.now()
    current_time = now.time()
    arrival_time_str = now.strftime("%H:%M")
    attendance_info = ""

    if student_id in df['ID'].astype(str).values:
        index = df.index[df['ID'].astype(str) == student_id].tolist()[0]

        if datetime.strptime("10:59", "%H:%M").time() <= current_time <= datetime.strptime("11:03", "%H:%M").time():
            df.at[index, 'Status'] = "Present"
        elif datetime.strptime("11:04", "%H:%M").time() <= current_time <= datetime.strptime("11:53", "%H:%M").time():
            df.at[index, 'Status'] = "Tardy"
        else:
            df.at[index, 'Status'] = "Absent"
        
        attendance_info = f"{df.at[index, 'Name']} marked as {df.at[index, 'Status']} at {arrival_time_str}\n"
    else:
        name = f"Student {student_id}"  
        new_row = pd.DataFrame({'ID': [student_id], 'Name': [name], 'Status': ['Absent'], 'Arrival Time': [arrival_time_str]})
        
        if datetime.strptime("10:59", "%H:%M").time() <= current_time <= datetime.strptime("11:03", "%H:%M").time():
            new_row['Status'] = "Present"
        elif datetime.strptime("11:04", "%H:%M").time() <= current_time <= datetime.strptime("11:53", "%H:%M").time():
            new_row['Status'] = "Tardy"
        
        df = pd.concat([df, new_row], ignore_index=True)
        attendance_info = f"{name} added with status {new_row.at[0, 'Status']} at {arrival_time_str}\n"


    update_display(attendance_info)

    return df


def update_display(attendance_info):
    display_area.configure(state='normal')  
    display_area.insert(tk.END, attendance_info)
    display_area.configure(state='disabled')  


def print_attendance():
    printer_name = win32print.GetDefaultPrinter() 
    attendance_text = display_area.get("1.0", tk.END)
    
    if not attendance_text.strip():
        messagebox.showwarning("Warning", "No attendance information to print.")
        return
    

    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)
    

    hdc.StartDoc("Attendance Printout")
    hdc.StartPage()
    

    for line in attendance_text.splitlines():
        hdc.TextOut(100, 100, line)
        hdc.MoveTo(100, hdc.GetTextExtent(line)[1])
    
    hdc.EndPage()
    hdc.EndDoc()
    
    messagebox.showinfo("Print", "Attendance printed successfully.")


def scan_id_card():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the camera.")
        return

    df = load_attendance_data() 

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        barcodes = decode(frame)
        for barcode in barcodes:
            student_id = barcode.data.decode('utf-8')
            df = mark_attendance(student_id, df)

            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            time.sleep(3)

        cv2.imshow('ID Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    

    df.to_csv(csv_file, index=False)
    messagebox.showinfo("Attendance", "Scanning complete. Attendance updated.")


def start_scanning():
    threading.Thread(target=scan_id_card, daemon=True).start()

app = tk.Tk()
app.title("Attendance ID Scanner")
tk.Label(app, text="Welcome to Attendance System", font=("Arial", 16)).pack(pady=10)


display_area = scrolledtext.ScrolledText(app, width=50, height=15, font=("Arial", 12), wrap=tk.WORD)
display_area.pack(pady=10)
display_area.configure(state='disabled') 

tk.Button(app, text="Start Scanning", command=start_scanning, font=("Arial", 12)).pack(pady=20)
tk.Button(app, text="Print Attendance", command=print_attendance, font=("Arial", 12)).pack(pady=10)
tk.Button(app, text="Exit", command=app.quit, font=("Arial", 12)).pack(pady=10)

app.mainloop()