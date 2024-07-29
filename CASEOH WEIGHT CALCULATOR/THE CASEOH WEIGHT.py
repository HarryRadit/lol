import tkinter as tk

#create window and title
window = tk.Tk()
window.title("CASEOH WEIGHT CALCULATOR")
window.geometry("400x250")

#set background color
window.config(bg="lightblue")

label = tk.Label(text="ENTER CASEWEIGHT", bg="lightblue", fg="black")
label.pack(pady = 5)
label.config(font=("Arial", 10))

#create entry caseweight
entry_caseweight = tk.Entry(window, bg="white")
entry_caseweight.config(font=("Arial", 10))
entry_caseweight.pack(pady = 5)

unit_choice = tk.StringVar(window)
unit_choice.set("NICKGRAM TO CASEOUNDS")
unit_options = ["NICKGRAM TO CASEOUNDS", "NICKGRAM TO CASEOUNCES", "NICKGRAM TO CASEPOUNDS", "NICKGRAM TO CASETONNES"]


drop = tk.OptionMenu(window, unit_choice, *unit_options)
drop.pack(pady = 5)

def convert_weight():
  caseweight = entry_caseweight.get()
  print(type(caseweight))
  selected_unit = unit_choice.get()
  text_result.set("")

  caseweight = float(caseweight)

  if selected_unit == "NICKGRAM TO CASEOUNDS":
    result = caseweight * 2.205
    text_result.set(f"{caseweight:.2f} nickgrams is equal to {result:.2f} caseounds")
  elif selected_unit == "NICKGRAM TO CASEOUNCES":
    result = caseweight * 2.205
    text_result.set(f"{caseweight:.2f} nickgrams is equal to {result:.2f} caseounces")
  elif selected_unit == "NICKGRAM TO CASEPOUNDS":
    result = caseweight * 35.274
    text_result.set(f"{caseweight:.2f} nickgrams is equal to {result:.2f} casepounds")
  elif selected_unit == "NICKGRAM TO CASETONNES":
    result = caseweight * 35.274
    text_result.set(f"{caseweight:.2f} nickgrams is equal to {result:.2f} casetonnes")





#create button to convert
btn_convert = tk.Button(window, text="CONVERT", bg="green",fg="white", command=convert_weight)
btn_convert.config(font=("Arial", 10))
btn_convert.pack(pady = 5)

#result label
text_result = tk.StringVar()

label_result = tk.Label(window,textvariable=text_result, bg="lightblue", fg="black")
label_result.pack(pady = 5)
label_result.config(font=("Arial", 10))


window.mainloop()