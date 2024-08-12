from customtkinter import *
import CTkMessagebox

app = CTk()

app.geometry("600x400")
app.title("Military")

def validate_input(value):
    if value.isalpha() or value == "":
        return True
    return False

def categorize_number(*args):
    ship = ship_input.get()

    if ship:
        ship = ship.lower()

        if ship == "b":
            result_text = "Battleship"
        elif ship == "c":
            result_text = "Cruiship"
        elif ship == "d":
            result_text = "Destroyer"
        else:
            result_text = "No info"

        result.configure(state="normal")
        result.delete(0, END)
        result.insert(0, result_text)
        result.configure(state="disabled")
    else:
        result.configure(state="normal")
        result.delete(0, END)
        result.configure(state="disabled")

vcmd = app.register(validate_input)

number_label = CTkLabel(master=app, text="Letter:")
number_label.place(relx=0.3, rely=0.3)

ship_input = CTkEntry(master=app, width=100, validate="key", validatecommand=(vcmd, '%P'))
ship_input.place(relx=0.4, rely=0.3)
ship_input.bind('<KeyRelease>', categorize_number)  
type_label = CTkLabel(master=app, text="Type:")
type_label.place(relx=0.3, rely=0.43)

result = CTkEntry(master=app, width=100, state="disabled")
result.place(relx=0.4, rely=0.43)

app.mainloop()
