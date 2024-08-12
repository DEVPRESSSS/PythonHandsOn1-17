import CTkMessagebox
from customtkinter import *

app = CTk()

app.geometry("600x400")
app.title("Earthquake")

new_list = ["hey", "heyss", "heysss"]
move_list = []

def move():
    try:
        selected_text = textBox1.get("sel.first", "sel.last").strip()
    except:
        selected_text = ""

    if selected_text == "":
        msg = CTkMessagebox.CTkMessagebox(title="Error", message="Please select an item to move.", icon="cancel")
        return

    if selected_text in new_list:
        move_list.append(selected_text) 
        new_list.remove(selected_text)   
        
        textBox1.configure(state="normal")
        textBox1.delete("1.0", "end")
        textBox1.insert("1.0", "\n".join(map(str, new_list)))
        textBox1.configure(state="disabled")

        textBox2.configure(state="normal")
        textBox2.delete("1.0", "end")
        textBox2.insert("1.0", "\n".join(map(str, move_list)))
        textBox2.configure(state="disabled")
    else:
        msg = CTkMessagebox.CTkMessagebox(title="Error", message="Selected item not found in the list.", icon="cancel")

textBox1 = CTkTextbox(master=app, height=120, width=100, font=("Tahoma", 12))
textBox1.place(relx=0.3, rely=0.45)
textBox1.insert("1.0", "\n".join(map(str, new_list)))

textBox2 = CTkTextbox(master=app, height=120, width=100, font=("Tahoma", 12), state="disabled")
textBox2.place(relx=0.5, rely=0.45)

move_btn = CTkButton(master=app, text="Move", width=75, command=move)
move_btn.place(relx=0.3, rely=0.25)

app.mainloop()
