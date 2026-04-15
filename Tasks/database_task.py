import tkinter
import pymysql
import tkinter.messagebox

tk = tkinter.Tk()
tk.title("Database Entry Form")
def connect_db():
    pymysql.connect(host="localhost", user="root", password="", database="testdb")


def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    mobile = entry_mobile.get()

    try:
        db = connect_db()
        cr = db.cursor()
        cr.execute(
            "INSERT INTO users (name, email, mobile) VALUES (name, email, mobile)"
        )
        db.commit()
        tkinter.messagebox.showinfo("Success", "Data submitted successfully.")
    except Exception as e:
        tkinter.messagebox.showerror("Error","An error occurred:")
        

tk.geometry("400x500")
tk.config(bg='lightblue')
l1 = tkinter.Label(tk, text="Name", bg='LightBlue', fg='red', font='Courier 15 bold')
l1.grid(row=0, column=0)
l2 = tkinter.Label(tk, text="Email", bg='LightBlue', fg='red', font='Courier 15 bold')
l2.grid(row=1, column=0)
l3 = tkinter.Label(tk, text="Mobile", bg='LightBlue', fg='red', font='Courier 15 bold')
l3.grid(row=2, column=0)

entry_name = tkinter.Entry(tk)
entry_name.grid(row=0, column=1)
entry_email = tkinter.Entry(tk)
entry_email.grid(row=1, column=1)
entry_mobile = tkinter.Entry(tk)
entry_mobile.grid(row=2, column=1)
submit_button = tkinter.Button(tk, text="Submit", command=submit_data)
submit_button.grid(row=3, column=1)

tk.mainloop()