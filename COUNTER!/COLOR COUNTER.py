import tkinter as tk

window = tk.Tk()
window.geometry("400x200")


window.title("button event change color")
colors = ["red", "green", "blue", "yellow", "purple"]
count = 0
window.config(bg=colors[count])


def button_click():
    global count
    count += 1
    if count >= len(colors):
        count = 0
    window.config(bg=colors[count])
    print("button click")
def my_function():
    window.configure(bg="pink")


label = tk.Label(window, text = "CLICK HERE TO CHANGE COLOR AND YOU WILL GET 1 MILLION ROBUX!!", bg = "lightblue")
label.pack(pady=20)

button = tk.Button(window, text="click me", command=button_click)
button.pack(side=tk.TOP, expand=True)

button1 = tk.Button(window, text="CLICK TO CHANGE COLOR TO PINK", command=my_function, bg="pink")
button1.pack()





window.mainloop()