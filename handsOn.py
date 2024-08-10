from customtkinter import*
import CTkMessagebox



app = CTk()

app.geometry("600x400")
app.title("Conversion")



def conversion():

    peso_value = pesoinput.get()

    if peso_value == "":
        dollarinput.delete(0, END)
        msg =CTkMessagebox.CTkMessagebox(title="Error", message="Input is not valid please try again", icon="cancel")

        return
    peso_value = float(peso_value)

    result = float(peso_value / 56.0)
    
    dollarinput.delete(0, END) 
    dollarinput.insert(0, f"{result}")
    dollarinput.configure(state="disabled")


peso= CTkLabel(master=app, text="Peso:")
peso.place(relx= 0.3,rely=0.3)

pesoinput= CTkEntry(master=app,width=100)
pesoinput.place(relx= 0.4 ,rely= 0.3)


dollar= CTkLabel(master=app, text="Dollar:")
dollar.place(relx= 0.3,rely=0.4)

dollarinput= CTkEntry(master=app,width=100)
dollarinput.place(relx= 0.4 ,rely= 0.4)


convert =CTkButton(master=app, text="Convert",width=70,command=conversion)
convert.place(relx=0.45, rely=0.5)

app.mainloop()