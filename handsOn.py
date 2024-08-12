from customtkinter import *

app = CTk()

app.geometry("600x400")
app.title("Earthquake")

new_list= []

def reverse():
    for x in range( 1, 9):

        result = x * 3
        new_list.append(result)


    textBox1.configure(state="normal")
    textBox1.insert("1.0", "\n".join(map(str, new_list))) 

    textBox1.configure(state="disabled")

   



textBox1 = CTkTextbox(master=app, height=120, width=100,font=("Tahoma",10))
textBox1.place(relx=0.3, rely=0.4)



run_btn = CTkButton(master=app, text="Run", width=75, command=reverse)
run_btn.place(relx=0.3, rely=0.25)

app.mainloop()
