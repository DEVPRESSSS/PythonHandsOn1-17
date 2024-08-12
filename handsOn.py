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

def IdVak(value):
     
     if value.isdigit() or value=="":
          
          return True
     return False


def delete():

    msg = CTkMessagebox.CTkMessagebox(title="Confirmation", message="Do you want to delete this record?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()
    
    if response=="Yes":
   
            text3 = textBox3.get()


            
            if text3:
                try:
                    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                        'SERVER=REJIE\\SQLEXPRESS;'
                                        'DATABASE=cafe;'
                                        'Trusted_Connection=yes;')
                    
                    cursor = conn.cursor()
                    
                    sql = "DELETE FROM Student where Id= ?"
                    cursor.execute(sql,text3)
                    
                    conn.commit()
                    
                    conn.close()

                    CTkMessagebox.CTkMessagebox(title="Success", message="Data deleted successfully!",icon="check")
                    textBox1.delete(0,END)
                    textBox2.delete(0,END)
                    textBox3.delete(0,END)



                except Exception as e:
                    CTkMessagebox.CTkMessagebox(title="Error", message="Something went wrong!",icon="cancel")
            else:
                    msg= CTkMessagebox.CTkMessagebox(title="Error", message="Please input a value",icon="cancel")



vcmd= app.register(validate)
vcmds= app.register(IdVak)



labelID= CTkLabel(master=app, text="ID:")
labelID.place(relx=0.2,rely= 0.1)
textBox3 = CTkEntry(master=app, height=40, width=50, font=("Tahoma", 12),validate="key",validatecommand=(vcmds,'%P'))
textBox3.place(relx=0.3, rely=0.1)


label1= CTkLabel(master=app, text="Name:")
label1.place(relx=0.2,rely= 0.32)
textBox1 = CTkEntry(master=app, height=40, font=("Tahoma", 12),validate="key",validatecommand=(vcmd,'%P'))
textBox1.place(relx=0.3, rely=0.35)



label2= CTkLabel(master=app, text="Program:")
label2.place(relx=0.2,rely=0.48)
textBox2 = CTkEntry(master=app, height=40, font=("Tahoma", 12))
textBox2.place(relx=0.3, rely=0.5)

move_btn = CTkButton(master=app, text="DELETE", width=75, command=delete)
move_btn.place(relx=0.3, rely=0.25)

app.mainloop()
