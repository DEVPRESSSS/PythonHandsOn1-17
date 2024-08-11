from customtkinter import *
import CTkMessagebox

app = CTk()

app.geometry("600x400")
app.title("Aircraft")

def validate_input(value):
    if value.isdigit() or value == "":
        return True
    return False

def categorize_number(*args):
    number = number_input.get()

    if number:
        number = int(number)

        if number <= 499:
            result_text = "Bird"
        elif number >= 500 and number <= 1100:
            result_text = "Military"
        else:
            result_text = "Civilian"

        result.configure(state="normal")
        result.delete(0, END)
        result.insert(0, result_text)
        result.configure(state="disabled")
    else:
        result.configure(state="normal")
        result.delete(0, END)
        result.configure(state="disabled")

vcmd = app.register(validate_input)

number_label = CTkLabel(master=app, text="Number:")
number_label.place(relx=0.3, rely=0.3)

number_input = CTkEntry(master=app, width=100, validate="key", validatecommand=(vcmd, '%P'))
number_input.place(relx=0.4, rely=0.3)
number_input.bind('<KeyRelease>', categorize_number)  
type_label = CTkLabel(master=app, text="Type:")
type_label.place(relx=0.3, rely=0.43)

result = CTkEntry(master=app, width=100, state="disabled")
result.place(relx=0.4, rely=0.43)

app.mainloop()
