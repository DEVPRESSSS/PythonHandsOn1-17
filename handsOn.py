from customtkinter import *
import CTkMessagebox

app = CTk()

app.geometry("600x400")
app.title("Earthquake")

def validate_input(value):
    if value == "" or value.replace('.', '', 1).isdigit():
        return True
    return False

def categorize_number(*args):
    magnitude = magnitude_input.get()

    if magnitude:
        magnitude = float(magnitude)

        if magnitude < 4.9:
            result_text = "No damage"
        elif magnitude >= 4.9 and magnitude <=5.5:
            result_text = "Some damage"
        elif magnitude > 5.5 and magnitude <= 6.5 :

            result_text = "Serious damage"

        elif magnitude > 6.5 and magnitude <= 7.4 :

            result_text = "Disaster"
        else:
            result_text = "Catastrophe"

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

magnitude_input = CTkEntry(master=app, width=100, validate="key", validatecommand=(vcmd, '%P'))
magnitude_input.place(relx=0.4, rely=0.3)
magnitude_input.bind('<KeyRelease>', categorize_number)  
effect_label = CTkLabel(master=app, text="Effect:")
effect_label.place(relx=0.3, rely=0.43)

result = CTkEntry(master=app, width=100, state="disabled")
result.place(relx=0.4, rely=0.43)

app.mainloop()
