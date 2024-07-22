import tkinter as  tk
from tkinter import ttk
from tkinter import messagebox


root = tk.Tk()
root.title("This da form")
root.configure(background="lavender")

#create a style
style = ttk.Style()
style.theme_use("clam")
style.configure("Tentry", foreground="black", background="white")
style.configure("TLabel", foreground="black", background="lavender")
style.configure("TButton", foreground="black", background="lavender")
style.configure("TCombobox", foreground="black", background="white")

def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    country = country_combobox.get()
    bio = bio_textbox.get("1.0", tk.END)
    othercountry = othercountry_entry.get()
    print(name, age, email, gender, password, confirm_password, country, bio, othercountry)

    if not name or not age or not email or not gender or not password or not confirm_password or not country:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    messagebox.showinfo("Success", "Form submitted successfully")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    country_combobox.set("")
    bio_textbox.delete("1.0", tk.END)
    othercountry_entry.delete(0, tk.END)


name_label = ttk.Label(root, text="Name: ")
name_label.grid(row=0, column=0, padx=10, pady=10,  sticky=tk.N)

age_label = ttk.Label(root, text="Age: ")
age_label.grid(row=1, column=0, padx=10, pady=10,  sticky=tk.N)

email_label = ttk.Label(root, text="Email: ")
email_label.grid(row=2, column=0, padx=10, pady=10,  sticky=tk.N)

gender_label = ttk.Label(root, text="Gender: ")
gender_label.grid(row=3, column=0, padx=10, pady=10,  sticky=tk.N)

password_label = ttk.Label(root, text="Password: ")
password_label.grid(row=4, column=0, padx=10, pady=10,  sticky=tk.N)

confirm_password_label = ttk.Label(root, text="Confirm Password: ")
confirm_password_label.grid(row=5, column=0, padx=10, pady=10,  sticky=tk.N)

country_label = ttk.Label(root, text="Country: ")
country_label.grid(row=6, column=0, padx=10, pady=10,  sticky=tk.N)

othercountry_label = ttk.Label(root, text="Other Country: ")
othercountry_label.grid(row=8, column=0, padx=10, pady=10,  sticky=tk.N)

bio_label = ttk.Label(root, text="Bio: ")
bio_label.grid(row=7, column=0, padx=10, pady=10,  sticky=tk.N)

name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10,  sticky=tk.N)

age_entry = ttk.Entry(root, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=10,  sticky=tk.N)

email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=10,  sticky=tk.N)

password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=4, column=1, padx=10, pady=10,  sticky=tk.N)

confirm_password_entry = ttk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=5, column=1, padx=10, pady=10,  sticky=tk.N)

country_combobox = ttk.Combobox(root, width=20)
country_combobox['values'] = ('Indonesia','Malaysia','Singapore','Thailand','Vietnam','Philippines','Other country')
country_combobox.grid(row=6, column=1, padx=10, pady=10,  sticky=tk.N)

othercountry_entry = ttk.Entry(root, width=30)
othercountry_entry.grid(row=8, column=1, padx=10, pady=10,  sticky=tk.N)

bio_textbox = tk.Text(root, width=30, height=10)
bio_textbox.grid(row=7, column=1, padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit", cursor = "hand2", style="TButton", command=submit)
submit_button.grid(row=9, column=1, padx=10, pady=10,  sticky=tk.N)
gender_var = tk.StringVar()
gender_var.set("Male")
male_radio = ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=3, column=1, padx=10, pady=10,  sticky=tk.N)

female_radio = ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=3, column=2, padx=10, pady=10,  sticky=tk.N)



root.mainloop()