import tkinter as tk
from main import root



root = tk.Tk()
root.wm_geometry("400x700+1000+200")
root.title("Rizzbook")


home_page = tk.Frame(root)
home_page.grid(row=0, column=0, sticky="news")
home_message = tk.Label(home_page, text="Rizzbook").place(anchor="center")



'''login_username = tk.Entry(welcome_page)
login_username.pack()
login_password = tk.Entry(welcome_page, show="*")
login_password.pack()
login_confirm = tk.Button(welcome_page, text="Login", command=login)
login_confirm.pack()
login_forgot_password = tk.Button(welcome_page, text="Forgot Password", command=forgot_password)
login_forgot_password.pack()
login_create_account = tk.Button(welcome_page, text="Create new account", command=create_new_account)
login_create_account.pack()'''


root.mainloop()