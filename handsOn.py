from customtkinter import *
import CTkMessagebox

app = CTk()

app.geometry("600x400")
app.title("Earthquake")

def validate_input(value):
    if value == "" or value.isdigit():
        return True
    return False

def categorize_number(*args):
    grade = grade_input.get()

    if grade:
        grade = float(grade)

        if grade <= 74:
            result_text = "Failed"
        elif grade > 74 and grade <= 76:
            result_text = "3.00"
        elif grade > 76 and grade <= 79 :

            result_text = "2.75"

        elif grade > 79 and grade <= 81 :

            result_text = "2.50"

        elif grade > 81 and grade <= 84:
            result_text = "2.25"

        elif grade > 84 and grade <= 88 :

            result_text = "2.00"

        elif grade > 88 and grade <= 91 :

            result_text = "1.75"

        elif grade > 91 and grade <= 94 :

            result_text = "1.50"

        elif grade > 94 and grade <= 98 :

            result_text = "1.25"

        elif grade > 98 and grade <= 100 :

            result_text = "1.00"
        else:
            result_text = "Invalid Grade"

        result.configure(state="normal")
        result.delete(0, END)
        result.insert(0, result_text)
        result.configure(state="disabled")
    else:
        result.configure(state="normal")
        result.delete(0, END)
        result.configure(state="disabled")

vcmd = app.register(validate_input)

number_label = CTkLabel(master=app, text="Magnitude:")
number_label.place(relx=0.28, rely=0.3)

grade_input = CTkEntry(master=app, width=100, validate="key", validatecommand=(vcmd, '%P'))
grade_input.place(relx=0.4, rely=0.3)
grade_input.bind('<KeyRelease>', categorize_number)  
effect_label = CTkLabel(master=app, text="Effect:")
effect_label.place(relx=0.3, rely=0.43)

result = CTkEntry(master=app, width=100, state="disabled")
result.place(relx=0.4, rely=0.43)

app.mainloop()
