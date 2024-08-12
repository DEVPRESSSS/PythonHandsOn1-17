import pyodbc
from customtkinter import *
import CTkMessagebox

app = CTk()

app.geometry("600x400")
app.title("Earthquake")

def validate(value):

    if value.isalpha() or value== "":
        return True
    
    return False
def add():
    text1 = textBox1.get()
    text2 = textBox2.get()


    
    if text1 and text2:
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER=REJIE\\SQLEXPRESS;'
                                  'DATABASE=cafe;'
                                  'Trusted_Connection=yes;')
            
            cursor = conn.cursor()
            
            sql = "INSERT INTO Student (Name, Program) VALUES (?,?)"
            cursor.execute(sql, text1,text2)
            
            conn.commit()
            
            conn.close()

            CTkMessagebox.CTkMessagebox(title="Success", message="Data inserted successfully!",icon="check")
            textBox1.delete(0,END)
            textBox2.delete(0,END)


        except Exception as e:
            CTkMessagebox.CTkMessagebox(title="Error", message="Something went wrong!",icon="cancel")
    else:
            msg= CTkMessagebox.CTkMessagebox(title="Error", message="Please input a value",icon="cancel")



vcmd= app.register(validate)
textBox1 = CTkEntry(master=app, height=40, font=("Tahoma", 12),validate="key",validatecommand=(vcmd,'%P'))
textBox1.place(relx=0.3, rely=0.35)

textBox2 = CTkEntry(master=app, height=40, font=("Tahoma", 12))
textBox2.place(relx=0.3, rely=0.47)

move_btn = CTkButton(master=app, text="INSERT", width=75, command=add)
move_btn.place(relx=0.3, rely=0.25)

app.mainloop()
