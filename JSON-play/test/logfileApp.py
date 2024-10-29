import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime

# Function to append the submission data to a text file
def save_submission():
    date_selected = cal.get_date()
    job_title = job_title_entry.get()
    company_url = url_entry.get()
    submission_result = result_entry.get()

    # Check if all fields are filled
    if not job_title or not company_url or not submission_result:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    # Create or append to the log file
    with open("job_applications_log.txt", "a") as file:
        file.write(f"Date: {date_selected}, Job Title: {job_title}, Company URL: {company_url}, Submission Result: {submission_result}\n")

    # Clear input fields after saving
    job_title_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Job application data saved!")

# GUI setup
root = tk.Tk()
root.title("Job Application Logger")

# Calendar widget cal = Calendar(root, selectmode='day', date_pattern='y-mm-dd',
#                font=('Helvetica', 12, 'bold', 'underline'),  # Font style
#                foreground='blue')  # Text color (e.g., blue)
cal_label = ttk.Label(root, text="Select Date:", font=('Helvetica', 12, 'bold', 'underline'), foreground='blue' )
cal_label.grid(row=0, column=0, padx=10, pady=10)

# cal = Calendar(root, selectmode='day', date_pattern='y-mm-dd')
# cal.grid(row=0, column=1, padx=10, pady=10)
cal = Calendar(root, selectmode='day', date_pattern='y-mm-dd',
               font=('Helvetica', 12, 'bold'),  # Font for days
               headersforeground='black',  # Bold black for headers (Month/Year)
               foreground='blue',  # Bold black for days
               weekendforeground='red',
               weekendbackground='blue')  # Make weekends also appear in black
cal.grid(row=0, column=1, padx=10, pady=10)

# Job Title input
job_title_label = ttk.Label(root, text="Job Title:")
job_title_label.grid(row=1, column=0, padx=10, pady=10)

job_title_entry = ttk.Entry(root)
job_title_entry.grid(row=1, column=1, padx=10, pady=10)

# URL input
url_label = ttk.Label(root, text="Company URL:")
url_label.grid(row=2, column=0, padx=10, pady=10)

url_entry = ttk.Entry(root)
url_entry.grid(row=2, column=1, padx=10, pady=10)

# Result input
result_label = ttk.Label(root, text="Submission Result:")
result_label.grid(row=3, column=0, padx=10, pady=10)

result_entry = ttk.Entry(root)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Save Button
save_button = ttk.Button(root, text="Save Submission", command=save_submission)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
