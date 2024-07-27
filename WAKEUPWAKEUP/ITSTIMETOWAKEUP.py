import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pytz



jakarta = pytz.timezone('Asia/Jakarta')

def update_time():
    current_time = datetime.now(jakarta).strftime(time_format.get())
    label.config(text=current_time)
    label.after(1000, update_time)
    check_alarm(current_time)
def set_alarm():
    alarm_time_str = alarm_time.get()
    alarm_datetime = datetime.strptime(alarm_time_str, "%H:%M:%S")
    alarm_hour = alarm_datetime.hour
    alarm_minute = alarm_datetime.minute
    alarm_second = alarm_datetime.second
    print(alarm_time_str, alarm_hour, alarm_minute, alarm_second)
    alarm_label.config(text=f"alarm set for {alarm_time_str}")

def check_alarm(current_time):
    if alarm_time.get() == current_time:
        messagebox.showinfo("wake up", "time to wake up")

root = tk.Tk()
root.title("clock")
root.geometry("400x200")
root.configure(bg="#FFCDCB")

label = tk.Label(root, text="clock", bg="Lightblue", fg="black")
label.config(font=("Arial", 24))
label.pack(pady = 20)

time_format = tk.StringVar()
time_format.set("%H:%M:%S")

alarm_time = tk.StringVar()
alarm_entry = tk.Entry(root, textvariable=alarm_time, width=10)
alarm_entry.pack(pady=10)

#create button to set alarm
btn_set_alarm = tk.Button(root, text="SET ALARM", bg="green",fg="white", command=set_alarm)
btn_set_alarm.config(font=("Arial", 10))
btn_set_alarm.pack(pady = 5)

alarm_activate = tk.BooleanVar()
alarm_activate.set(False)


alarm_label = tk.Label(root, text="alarm", bg="Lightblue", fg="black")
alarm_label.pack(pady = 10)




update_time()

root.mainloop()