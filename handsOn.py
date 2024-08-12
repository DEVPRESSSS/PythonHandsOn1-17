from customtkinter import *

app = CTk()

app.geometry("600x400")
app.title("Earthquake")

my_list = [5,4,3,2,1]

def reverse():
    my_list.reverse()

    textBox2.configure(state="normal")
    textBox2.insert("1.0", "\n".join(map(str, my_list))) 

    textBox2.configure(state="disabled")

   



textBox1 = CTkTextbox(master=app, height=100, width=80,font=("Tahoma",10))
textBox1.place(relx=0.3, rely=0.4)

textBox1.configure(state="normal")
textBox1.insert("1.0", "\n".join(map(str, my_list))) 
textBox1.configure(state="disabled")

textBox2 = CTkTextbox(master=app, height=100, width=80,font=("Tahoma",10))
textBox2.place(relx=0.5, rely=0.4)

run_btn = CTkButton(master=app, text="Run", width=75, command=reverse)
run_btn.place(relx=0.3, rely=0.25)

app.mainloop()
