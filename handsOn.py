from customtkinter import *
import CTkMessagebox

app = CTk()

app.geometry("600x400")
app.title("Simple Calculator")

def add():
    perform_operation("+")

def subtract():
    perform_operation("-")

def multiply():
    perform_operation("*")

def divide():
    perform_operation("/")

def perform_operation(operation):
    first_value = pesoinput.get()
    second_value = dollarinput.get()

    if first_value == "" or second_value == "":
        msg = CTkMessagebox.CTkMessagebox(title="Error", message="Please fill in both numbers.", icon="cancel")
        return
    
    try:
        first_value = float(first_value)
        second_value = float(second_value)
        
        if operation == "+":
            result = first_value + second_value
        elif operation == "-":
            result = first_value - second_value
        elif operation == "*":
            result = first_value * second_value
        elif operation == "/":
            if second_value == 0:
                msg = CTkMessagebox.CTkMessagebox(title="Error", message="Division by zero is not allowed.", icon="cancel")
                return
            

            result = first_value / second_value
        result_input.configure(state="normal")
        result_input.delete(0, END)
        result_input.insert(0,result)
        result_input.configure(state="disabled")

    except ValueError:
        msg = CTkMessagebox.CTkMessagebox(title="Error", message="Input is not valid. Please enter numeric values only.", icon="cancel")

peso = CTkLabel(master=app, text="First Number:")
peso.place(relx=0.4, rely=0.25)

pesoinput = CTkEntry(master=app, width=100)
pesoinput.place(relx=0.4, rely=0.3)

dollar = CTkLabel(master=app, text="Second Number:")
dollar.place(relx=0.4, rely=0.38)

dollarinput = CTkEntry(master=app, width=100)
dollarinput.place(relx=0.4, rely=0.43)

convert_plus = CTkButton(master=app, text="-", width=40, command=subtract)
convert_plus.place(relx=0.5, rely=0.52)

convert_minus = CTkButton(master=app, text="+", width=40, command=add)
convert_minus.place(relx=0.4, rely=0.52)

convert_multiply = CTkButton(master=app, text="/", width=40, command=divide)
convert_multiply.place(relx=0.5, rely=0.6)

convert_divide = CTkButton(master=app, text="*", width=40, command=multiply)
convert_divide.place(relx=0.4, rely=0.6)

result_input = CTkEntry(master=app, width=100)
result_input.place(relx=0.4, rely=0.68)

app.mainloop()
