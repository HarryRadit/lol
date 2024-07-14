import tkinter as tk
from playsound import playsound

window = tk.Tk()


window.title("COUNTER App")
window.config(bg="lightblue")

count = 0



def increase():
    global count
    count += 1
    label.config(text = "Counter: " + str(count))
    playsound('blazblue-continuum-shift-ii-counter.mp3')

def decrease():
    global count
    count -= 1
    label.config(text = "Counter: " + str(count))

label = tk.Label(text="COUNTER", bg="red", fg="white", font=("Arial", 20))
label.pack(pady = 10)

increase_button = tk.Button(text="increase", bg="green", fg="white", font=("Arial", 20), command = increase)
increase_button.pack(padx = 10, pady = 20)

decrease_button = tk.Button(text="decrease", bg="blue", fg="white", font=("Arial", 20), command = decrease)
decrease_button.pack(padx = 10, pady = 20)

window.mainloop()